# DNA trials

Lessons this layer has asked a second system to try. Each system's boot check
lists the open trials addressed to it. The system applies a trial as its own
self-change, through its own reviewer, claim and rollback window, and puts the
trial id in its changelog entry. Its verdict there decides whether the lesson
transfers. The rule is in [`../dna.md`](../dna.md).

**Mechanism only.** Nothing here may name a product, ticket, practice or
internal detail of any company. At most one open trial per system at a time.

<!-- Entry format (boot checks parse it):
    ## T-001 · <lesson slug>
    - **To:** <system>
    - **From:** <system where it helped>, change <C-NNN>, verdict <numbers>
    - **Try:** <the mechanism, in two or three sentences>
    - **Claim to test:** <measure> <up|down>
    - **Status:** open | taken up (<C-NNN>) | helped | does not transfer
-->

No trials yet. The first candidates can only appear once a core system's first
self-change has run its window, which is at least 14 days after migration.
