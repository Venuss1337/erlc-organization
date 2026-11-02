#!/usr/bin/env python3
"""Dependency-free Markdown link, formatting and baseline preservation checks."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def atoms(text):
    """Whole paragraphs/lists/tables and whole fences; headings are presentation."""
    parts, pending, fenced = [], [], False
    for line in text.splitlines():
        if line.startswith('```'):
            if not fenced and pending:
                parts.append('\n'.join(pending))
                pending = []
            pending.append(line)
            fenced = not fenced
            if not fenced:
                parts.append('\n'.join(pending))
                pending = []
        elif fenced:
            pending.append(line)
        elif (not line.strip() or line.startswith('#') or line.strip() == '---'
              or re.fullmatch(r'<a id="[^"]+"></a>', line)):
            if pending:
                parts.append('\n'.join(pending))
                pending = []
        else:
            pending.append(line)
    if pending:
        parts.append('\n'.join(pending))
    return parts


def slug(text):
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text).lower()
    return re.sub(r'[^\w\- ]', '', text).replace(' ', '-')


def visible_text(text):
    """Exclude fenced examples and inline code when inspecting live links."""
    result, fenced = [], False
    for line in text.splitlines():
        if line.startswith('```'):
            fenced = not fenced
        elif not fenced:
            result.append(re.sub(r'`[^`]*`', '', line))
    return '\n'.join(result)


def main():
    errors = []
    # Inspect maintained sources, not dependencies, generated content or static output.
    markdown_paths = subprocess.check_output(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z', '--', '*.md'],
        cwd=ROOT).decode('utf-8').split('\0')
    pages = {ROOT / name: (ROOT / name).read_text(encoding='utf-8')
             for name in set(markdown_paths) if name and (ROOT / name).is_file()}
    anchors = {}
    for path, body in pages.items():
        ids, seen, fenced, table_width = set(), {}, False, None
        for number, line in enumerate(body.splitlines(), 1):
            trailing = re.search(r'[ \t]+$', line)
            if trailing and (trailing[0] != '  ' or not line.strip()):
                errors.append(f'{path.relative_to(ROOT)}:{number}: whitespace other than a Markdown hard break')
            if line.startswith('```'):
                fenced = not fenced
            if fenced:
                continue
            for explicit in re.findall(r'<a id="([^"]+)"></a>', line):
                if explicit in ids:
                    errors.append(f'{path.relative_to(ROOT)}:{number}: duplicate anchor {explicit}')
                ids.add(explicit)
            if re.match(r'^#{1,6} ', line):
                name = slug(line.lstrip('#').strip())
                count = seen.get(name, 0)
                seen[name] = count + 1
                # Explicit and generated anchors of the same heading may coexist.
                ids.add(name if not count else f'{name}-{count}')
            if line.startswith('|'):
                width = len(re.split(r'(?<!\\)\|', re.sub(r'`[^`]*`', '', line)))
                if table_width is not None and width != table_width:
                    errors.append(f'{path.relative_to(ROOT)}:{number}: inconsistent table columns')
                table_width = width
            else:
                table_width = None
        if fenced:
            errors.append(f'{path.relative_to(ROOT)}: unclosed code fence')
        if not re.search(r'^# ', body, re.M):
            errors.append(f'{path.relative_to(ROOT)}: missing document title')
        anchors[path.resolve()] = ids

    link_count = 0
    for path, body in pages.items():
        for href in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', visible_text(body)):
            href = href.strip().strip('<>')
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                errors.append(f'{path.relative_to(ROOT)}: use relative paths for repository links: {href}') if parsed.scheme in ('file', 'vscode') else None
                continue
            link_count += 1
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            if not target.is_relative_to(ROOT):
                errors.append(f'{path.relative_to(ROOT)}: link escapes repository: {href}')
            elif not target.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing target: {href}')
            elif parsed.fragment and unquote(parsed.fragment) not in anchors.get(target, set()):
                errors.append(f'{path.relative_to(ROOT)}: missing anchor: {href}')

    manifest = json.loads((ROOT / 'docs/source-map.json').read_text(encoding='utf-8'))
    version, release_date = manifest['project_version'], manifest['release_date']
    metadata = (f'**Project version:** {version} · **Release date:** {release_date}'
                ' · **Status:** Official release.')
    if not re.fullmatch(r'\d+\.\d+\.\d+', version) or manifest['release_status'] != 'Official release':
        errors.append('Invalid official release metadata in source map')
    policy_paths = {entry['destination'] for entry in manifest['segments']} - {'CHANGELOG.md'}
    for name in policy_paths | {'docs/migration-report.md'}:
        if metadata not in pages[ROOT / name]:
            errors.append(f'{name}: missing or inconsistent official release metadata')
    readme = pages[ROOT / 'README.md']
    if (f'# ER:LC Organization — v{version}\n' not in readme
            or f'**Project version:** {version}' not in readme
            or f'**Release date:** {release_date}' not in readme
            or '**Status:** Official release' not in readme):
        errors.append('README release metadata differs from source map')
    changelog = pages[ROOT / 'CHANGELOG.md']
    releases = re.findall(r'^## \[([^]]+)\] - (\d{4}-\d{2}-\d{2})$', changelog, re.M)
    if (not releases or releases[0] != (version, release_date)
            or releases[-1] != ('1.0.0', '2026-11-02')
            or len({v for v, _ in releases}) != len(releases)
            or any(not re.fullmatch(r'\d+\.\d+\.\d+', v) for v, _ in releases)):
        errors.append('Changelog must match current release and preserve unique official history from 1.0.0')
    elif [tuple(map(int, v.split('.'))) for v, _ in releases] != sorted(
            [tuple(map(int, v.split('.'))) for v, _ in releases], reverse=True):
        errors.append('Changelog releases must be newest first')
    for path, body in pages.items():
        if path.is_relative_to(ROOT / 'docs') and metadata not in body:
            errors.append(f'{path.relative_to(ROOT)}: missing current documentation release metadata')
    for path, body in pages.items():
        if re.search(r'\bv3\.\d|\b3\.2\.\d|\*\*Source version:\*\*', body):
            errors.append(f'{path.relative_to(ROOT)}: obsolete project draft metadata')
    executive = manifest.get('executive_reform')
    if executive:
        if not executive.get('authorization'):
            errors.append('Missing R14 engineering authorization')
        for name, change in executive['changes'].items():
            before = subprocess.check_output(['git', 'show', f"{executive['commit']}:{name}"], cwd=ROOT)
            if (hashlib.sha256(before).hexdigest() != change['before_sha256']
                    or hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != change['after_sha256']
                    or not change.get('reason')):
                errors.append(f'Unrecorded R14 amendment: {name}')
        for name, expected in executive.get('additions', {}).items():
            if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected:
                errors.append(f'Unrecorded R14 added specification: {name}')
    reform = manifest.get('reform')
    historical_views = {}
    if reform:
        for name, expected in reform['paths'].items():
            if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected:
                errors.append(f'Unrecorded target amendment: {name}')
            historical_views[name] = subprocess.check_output(
                ['git', 'show', f"{reform['commit']}:{name}"], cwd=ROOT).decode('utf-8')
    # Earlier preservation checks remain on the explicitly superseded immutable design.
    # The usability release adds reading aids without changing v1.1 policy meaning.
    usability = manifest.get('usability_baseline')
    usability_blocks = 0
    if usability:
        for name in usability['paths']:
            try:
                before = subprocess.check_output(
                    ['git', 'show', f"{usability['commit']}:{name}"],
                    cwd=ROOT, stderr=subprocess.PIPE).decode('utf-8')
            except subprocess.CalledProcessError:
                errors.append(f'Usability baseline unavailable: {name}')
                continue
            def policy_blocks(body):
                body = re.sub(r'^\*\*Project version:\*\*.*$', '', body, flags=re.M)
                return Counter(digest(block) for block in atoms(body))
            original = policy_blocks(before)
            current = policy_blocks(historical_views.get(name, pages.get(ROOT / name, '')))
            if original - current:
                errors.append(f'Changed/missing v1.1 policy block: {name}')
            usability_blocks += sum(original.values())
    try:
        source = subprocess.check_output(
            ['git', 'show', f"{manifest['baseline_commit']}:{manifest['source_path']}"],
            cwd=ROOT, stderr=subprocess.PIPE).decode('utf-8')
    except subprocess.CalledProcessError as exc:
        print('FAIL: baseline unavailable; fetch the full Git history before validating.', file=sys.stderr)
        print(exc.stderr.decode('utf-8', errors='replace'), file=sys.stderr)
        return 1
    if digest(source) != manifest['source_sha256']:
        errors.append('Source hash differs from the recorded baseline')
    lines = source.splitlines(keepends=True)
    covered = []
    for entry in manifest['segments']:
        start, end = entry['lines']
        covered.extend(range(start, end + 1))
        if digest(''.join(lines[start - 1:end]).strip()) != entry['source_sha256']:
            errors.append(f'Source range hash mismatch: {start}–{end}')
        if not (ROOT / entry['destination']).is_file():
            errors.append(f'Missing mapped destination: {entry["destination"]}')
    if covered != list(range(1, len(lines) + 1)) or len(lines) != manifest['source_lines']:
        errors.append('Source map has missing, overlapping, out-of-order or invalid line ranges')

    # Reconstruct explicitly recorded release-label edits; policy content is still checked.
    comparable = {p.relative_to(ROOT).as_posix(): historical_views.get(p.relative_to(ROOT).as_posix(), body) for p, body in pages.items()}
    # Authorized policy supersessions are exact, hash-checked and reversible.
    # Additions do not exempt any original block. Never rewrite the original baseline.
    for edit in reversed(manifest.get('policy_amendments', [])):
        dest = edit['destination']
        if (digest(edit['before']) != edit['before_sha256']
                or digest(edit['after']) != edit['after_sha256']
                or not edit.get('reason') or not edit.get('authorization')):
            errors.append(f'Invalid authorized amendment record: {dest}')
        if comparable.get(dest, '').count(edit['after']) != 1:
            errors.append(f'Authorized replacement missing or ambiguous: {dest}')
        else:
            comparable[dest] = comparable[dest].replace(edit['after'], edit['before'], 1)
    for edit in manifest.get('release_baseline_edits', []):
        start, end = edit['source_lines']
        before = ''.join(lines[start - 1:end]).rstrip('\n')
        dest = edit['destination']
        if digest(before) != edit['source_sha256']:
            errors.append(f'Release edit source hash mismatch: {dest}:{start}–{end}')
        if comparable[dest].count(edit['replacement']) != 1:
            errors.append(f'Release edit replacement missing or ambiguous: {dest}:{start}–{end}')
        comparable[dest] = comparable[dest].replace(edit['replacement'], before, 1)

    historical = {path: Counter() for path in comparable}
    for entry in manifest.get('historical_only_sections', []):
        start, end = entry['source_lines']
        before = ''.join(lines[start - 1:end]).strip()
        if digest(before) != entry['source_sha256']:
            errors.append('Historical-only source hash mismatch')
        if entry['replacement'] not in comparable[entry['destination']]:
            errors.append('Historical-only replacement note missing')
        historical[entry['destination']].update(digest(a) for a in atoms(before))

    # Reverse recorded editorial links, then compare whole source content blocks.
    for edit in reversed(manifest['cross_reference_edits']):
        dest = edit['destination']
        if edit['after'] not in comparable[dest]:
            errors.append(f'Recorded link replacement missing: {dest}: {edit["after"]}')
        comparable[dest] = comparable[dest].replace(edit['after'], edit['before'])
    retained = {path: Counter(digest(a) for a in atoms(body))
                for path, body in comparable.items()}
    redirected = {path: Counter() for path in comparable}
    for edit in manifest['summary_redirects']:
        if edit['replacement'] not in comparable[edit['destination']]:
            errors.append(f'Recorded summary redirect missing: {edit["destination"]}')
        redirected[edit['destination']].update(edit['source_atoms_sha256'])
    exact_count, redirect_count, historical_count = 0, 0, 0
    for entry in manifest['segments']:
        start, end = entry['lines']
        destination = entry['destination']
        for atom in atoms(''.join(lines[start - 1:end])):
            key = digest(atom)
            if retained[destination][key]:
                retained[destination][key] -= 1
                exact_count += 1
            elif redirected[destination][key]:
                redirected[destination][key] -= 1
                redirect_count += 1
            elif historical[destination][key]:
                historical[destination][key] -= 1
                historical_count += 1
            else:
                errors.append(f'Unaccounted source block in {destination}: '
                              + atom[:150].replace('\n', ' / '))

    # Code blocks and tables must remain byte-for-byte after recorded link edits.
    source_atoms = atoms(source)
    fence_count = sum(a.startswith('```') for a in source_atoms)
    table_count = sum(a.startswith('|') for a in source_atoms)
    for atom in source_atoms:
        if (atom.startswith('```') or atom.startswith('|')) and not any(
                atom in body for body in comparable.values()):
            errors.append('Changed/missing source fence or table: ' + atom[:80])
    for letter in 'ABCDEFGHI':
        if not any(re.search(r'^## Example ' + letter + r' — ', text, re.M) for text in comparable.values()):
            errors.append(f'Missing worked example {letter}')

    if errors:
        for error in errors:
            print('FAIL: ' + error)
        print(f'{len(errors)} failure(s).')
        return 1
    print(f'PASS: {len(pages)} Markdown files; {link_count} relative links and fragments checked.')
    print(f'PASS: all {len(lines)} baseline lines mapped in {len(manifest["segments"])} ranges.')
    print(f'PASS: v{version} current metadata; {len(releases)} official changelog releases preserved.')
    print(f'PASS: {len(manifest.get("policy_amendments", []))} exact authorized policy amendments checked and reversed for baseline comparison.')
    if usability:
        print(f'PASS: {usability_blocks} v1.1 blocks accounted for in explicitly superseded historical views; target hashes checked separately.')
    print(f'PASS: {exact_count} source blocks retained (with recorded editorial edits); '
          f'{redirect_count} repeated summaries redirected; '
          f'{historical_count} development summaries retained in Git history.')
    print(f'PASS: all {table_count} original tables, {fence_count} fenced blocks and 9 worked examples retained.')
    print('Scope: local links, structure and migration preservation; policy consistency requires human review.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
