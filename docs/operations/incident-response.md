# Incident response and emergency command

**Project version:** 1.1.0 · **Release date:** 2026-11-02 · **Status:** Official release.

**Procedure specification; GOV-04 adoption and actual qualification/access checks are not verified.** Existing qualified responders retain their existing safety authority; this page does not grant unapproved powers. See the [activation register](../proposals/review-register.md). Emergency command coordinates a bounded response, not discipline or independent investigations.

## Declare, classify and take command

Anyone may raise an incident alert. A qualified Session Commander, T&S Duty Incident Commander or authorized technical emergency maintainer may **declare within their domain**, without prior executive approval, when routine work cannot safely contain an immediate threat. Record ID, UTC time, scope, severity, observed risk, commander and actual available capabilities. A person without qualification alerts responders and may pause their own unsafe activity; they cannot invent enforcement powers.

| Level | Trigger | Command and notification |
|---|---|---|
| S1 local | Contained disruption in one session/channel; normal permissions suffice | Qualified Session Commander for session logistics; qualified moderator retains enforcement remit. Log and tell owning lead by shift handoff. |
| S2 major | Coordinated disruption, multiple teams, suspected privileged compromise, serious active abuse or evidence compromise | Available qualified Duty Incident Commander coordinates; technical maintainer leads containment work. Notify T&S, Live Operations and Technology as relevant, and COO/acting COO as soon as safely possible, target within 30 minutes when contactable. Notify OIO for staff abuse/evidence risk. |
| S3 critical safety/platform | Credible imminent real-world danger, suspected child exploitation, widespread privileged loss or Owner account compromise | Available qualified commander coordinates safety referrals/containment; notify Owner and COO immediately through verified safe contact. Platform/emergency reporting proceeds without waiting for them. No staffed commander: suspend affected service, take only already-authorized protective action and escalate. |

Qualification is documented by the relevant Director: incident scenario exercise, domain limits, communication/handover, privacy and evidence basics. T&S validates enforcement competency; Technology validates technical competency; Live Operations validates session competency. A general IC qualification does not confer the others. Maintain consenting duty contacts and a backup, with explicit unavailable status; no mandatory on-call hours.

For S2/S3 the first available qualified Duty Incident Commander records acceptance and owns coordination. If none exists, the qualified domain responder is provisional coordinator **within existing domain authority only**, calls for a qualified IC and records unfilled capabilities. Different declarations merge into one incident record; higher rank does not take command automatically. COO resolves competing qualified command claims if reachable; until then the first recorded qualified command coordinates, while each specialist keeps their domain safety limits. No executive can demand unsafe execution beyond qualification.

## Powers and boundaries

| Role | May do within existing access/delegation | Must not do through emergency title |
|---|---|---|
| Session Commander | Pause/end their session, change session logistics, request qualified support, temporarily remove active disruptors if separately qualified | Issue permanent global bans, command unrelated teams outside accepted emergency scope |
| Incident Commander | Set containment objectives, coordinate accepted responders, suspend unsafe affected operations, allocate consenting available responders, request communications/evidence support | Compel absent volunteers, grant credentials, decide staff guilt, override IA/Appeals or amend policy |
| T&S enforcement responder | Apply qualified immediate enforcement, document basis and refer lasting action to ordinary authorized T&S decision owner | Treat emergency removal as a permanent ban without normal evidence and appeal |
| Technical emergency maintainer | Revoke compromised tokens/access within actual permissions, isolate unsafe integrations, preserve safe logs and restore within approved recovery scope | Access private case files without case authority, bypass native hierarchy, transfer ownership |
| OIO investigator | Independently assess staff misconduct/evidence interference after conflict screening | Direct live restoration or accept incident command as proof of misconduct |

Immediate threat reduction needs **no fresh approval** when already within the responder's mandate. Log first when feasible, afterward when delay would increase harm. New privileged access and restoration follow [technical controls](discord-permissions.md#security-containment-and-recovery); enduring staff consequences follow [case adjudication](../oversight/case-handling.md). Do not wait through the management ladder to stop an unsafe session.

## Practical response checklist

1. **Protect:** Pause unsafe sessions/channels; use least disruptive authorized containment. Report platform danger promptly. Do not download suspected illegal material for an internal evidence pack.
2. **Declare:** One incident ID and restricted operational log; name commander, domain responders, severity, objectives and next update. Separate confidential case evidence from general incident updates.
3. **Coordinate:** At small scale commander may keep the log and send updates. Split operations/comms/log tasks only if workload requires and willing qualified people exist. Community Experience sends approved factual status without allegations; if unavailable commander sends it. Technical and enforcement leads execute their own scopes.
4. **Preserve:** Collector records relevant IDs/links, UTC times, actions and safe originals under the [records procedure](discord-permissions.md#records-retention-and-deletion). Containment outranks perfect collection. Note evidence gaps; no credentials or private case attachments in an incident chat. Suspected evidence tampering goes to unconflicted IA and a new access custodian.
5. **Review:** Reassess risk and responder availability at material changes; for S2/S3 set a next update, normally 30 minutes during active response. This is an incident coordination target, not continuous volunteer coverage or guaranteed response time.
6. **Transfer:** Incoming qualified commander explicitly accepts. Record outgoing/incoming IDs, time, situation, objectives, actions, risks, access limits and pending notifications; announce one current commander. Rank alone or a CoS message is not transfer. If no relief, pause unsafe service and notify leadership rather than silently abandon command.
7. **Stand down:** Commander verifies immediate threat contained, evidence assigned, remaining work owned, restrictions reviewed and safe operating coverage. Relevant technical maintainer confirms technical recovery conditions; qualified enforcement lead confirms outstanding safety restrictions. If they cannot verify, keep that service paused. Record time and return normal task authority; notify responders and leadership.
8. **Learn:** Owning Director leads a short blameless operational review, target within seven days of stand-down when staffed. Record facts, failures, one action owner per fix and review date in the shared register. IA independently handles alleged misconduct; an unconflicted Assurance assessor reviews systemic defects. Never let a post-incident meeting replace a fair case.

```text
Immediate threat → qualified containment / platform report
       ↓
Declare scope + IC → specialists act within separate mandates
       ↓
Risk still active or coverage missing? → keep affected service paused
       ↓ no
Explicit handover OR stand-down → ordinary owners + independent case referral
```

## Serious safety and platform escalation

T&S is the internal safety-routing owner; any witness may report directly without its permission. Use Discord's in-app report on the specific message/profile and Roblox's Report Abuse for the relevant experience/content. Do not organize mass reports. Credible imminent danger warrants local emergency services where appropriate; staff are not emergency responders and must not promise rescue or investigate a person's location themselves. Offer a trusted adult/guardian or appropriate professional help when safe; do not automatically contact someone alleged to be the source of harm.

For suspected child sexual exploitation, grooming, credible threats or illegal content: stop public exposure within existing authority, preserve minimum message/account identifiers and reporting receipt, report through official platform routes, and seek appropriate professional/authority guidance where necessary. Do not request intimate images, government IDs, real names, home addresses, passwords, medical details or proof of victimhood; do not forward, download or reproduce suspected illegal sexual material. Do not interview minors as amateur criminal investigators or promise absolute secrecy. Platform decisions remain platform decisions; internal review may address community access and staff conduct without impeding reporting.

Verified platform constraints and source links are in the [implementation evidence](../readiness-v1-1.md#research-and-design-basis); local controls remain untested until the implementation register says otherwise.
