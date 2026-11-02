// Preserve the existing dependency-free Python audit behind one portable Bun command.
const candidates = process.platform === 'win32'
  ? [['py', '-3'], ['python3'], ['python']]
  : [['python3'], ['python']];
const command = candidates.find(([executable]) => Bun.which(executable));
if (!command) throw new Error('Install Python 3.9 or newer to run the repository preservation audit.');
const child = Bun.spawn([...command, 'scripts/validate_docs.py'], {
  stdin: 'inherit', stdout: 'inherit', stderr: 'inherit',
});
process.exit(await child.exited);
