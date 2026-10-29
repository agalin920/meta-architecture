# Human gate on the irreversible action

**Status:** `proven` — all four systems
**Invented in:** convergent.

## The pattern

Each system identifies the **one action it cannot take back** and puts an
absolute human gate on it. Not a confidence threshold, not an escalation policy
— a hard rule with no exception clause.

| System | The gate |
|---|---|
| zesty-eng-team | **Never merge a PR.** Ever. The Director merges |
| brand-system | **Nothing publishes without the human.** Including a one-word reply |
| personal-university | Architect proposals require student approval |
| media-log | Spec changes need confirmation; data changes do not |

## Why it works

It is what makes everything upstream safe to automate. zesty-eng-team removes
mid-flight checkpoints *because* the gate exists: *"the team runs to a PR
without mid-flight checkpoints. The `reviewer` gate replaces the Director's
mid-flight involvement."* The hard stop at the end buys autonomy everywhere
before it.

The gate must sit at the **irreversible** step, not the important one. Writing a
draft is important and reversible; posting it is not. Gating the wrong step
costs attention and buys nothing.

## Evidence

- `zesty-eng-team/docs/operating-rules.md` — a three-tier structure worth
  copying: pre-authorized / ask every time / **no authorization exists**. The
  third tier is the point. Backed by a settings allowlist, with the honest note
  that the deny patterns *"are prefix matches, not a security boundary"* — the
  documented rule is the real gate.
- `brand-system/agents/cycle-protocol.md` — rule 1 of the rules that outrank the
  protocol. And the reasoning is domain-specific rather than generic caution:
  an agent-run presence that posts autonomously is a reputational liability, and
  the brand's core claim is that a real person is behind it. **The gate is what
  makes the claim true.**

## How it fails

- **Gating too much.** If everything needs approval, the human becomes the
  bottleneck and starts rubber-stamping. brand-system's decision log explicitly
  guards against this: interrupted curation produces *"lazy yeses — which
  poisons the decision log."*
- **A gate with an exception clause.** "Unless it's trivial" is how a gate
  dissolves. Note that zesty-eng-team hit exactly this with *delegation* — the
  "implement trivial tickets yourself" rule ratcheted until the team looked like
  decoration, because trivial is self-assessed by the party who would otherwise
  have to delegate. Same mechanism applies to gates.
