# Rubric

Critics score each idea on six axes (1 = poor, 5 = strong) and apply three gates. The total is not a sum: an idea
that fails a gate is revised or dropped whatever its scores.

## Gates

- **G1 Evidence.** The idea is compatible with every entry of the brief's failure ledger, or says which entry it
  overturns and how the kill test would show it.
- **G2 Falsifiable claim.** The idea states one claim that a specific experiment could refute (method X beats
  baseline Y on metric Z in regime R), and names that experiment.
- **G3 Nearest work.** The closest prior work is identified by title, and the difference is stated in one sentence
  that a reviewer would accept.

- **G4 Definitions.** The idea opens with complete definitions and preliminaries: system and assumptions, random
  objects and their laws, every symbol, the target statement with all quantifiers, and the problem in "Given … find
  … such that …" form.

## Axes

| Axis | 1 | 3 | 5 |
|---|---|---|---|
| Unity | Components glued, each with its own job | Two components share an object or a schedule | One sampler or one target; the ingredients are its limits or factors |
| Novelty | The combination exists (found by search) | Known pieces, new coupling with a clear reason | New object, identity or guarantee not found in search |
| Guarantee | None, or one that a Clopper–Pearson check on the final plan already gives | A guarantee with a clear scope, standard proof | A guarantee that addresses what simple checks cannot (closed loop, misspecification, rare events, uniformity over sets) |
| Regime | No setting where the strong baseline loses | A plausible setting, untested | A setting with evidence (pilot, theory, or literature) where the baseline fails |
| Feasibility | Needs months or hardware the project does not have | Doable with the project's code and compute in weeks | A first test runs in hours on the project's machine |
| Venue fit | Off-topic for the venue | Fits, incremental | Fits, with the depth the venue expects (theory plus experiments, hardware when possible) |

## Verdicts

- **advance**: passes the gates, no axis below 3, and Unity or Novelty at 4 or more.
- **revise**: a fixable gate failure or a weak axis; the critic proposes a specific mutation.
- **drop**: glue with no regime, or the combination already exists.

## Venue notes

- IEEE T-RO: method plus theory plus convincing experiments, ideally hardware; long-form; robotics relevance must be
  explicit; real-time feasibility is checked by reviewers.
- RA-L / ICRA / IROS: a single clear contribution with experiments; theory optional.
- CDC / L-CSS / Automatica: guarantee first; experiments can be simulations.
