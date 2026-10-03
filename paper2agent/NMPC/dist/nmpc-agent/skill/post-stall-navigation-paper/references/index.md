# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| I. INTRODUCTION | Motivation and contributions: vision-based post-stall navigation for fixed-wing UAVs; Figure 1 |
| II. RELATED WORK | Prior work on onboard-sensing navigation, fixed-wing planning and control |
| III. APPROACH | Overview of the control strategy; parent of A. Mapping, B. RRT Generation, C. Direct Trajectory Optimization |
| A. Mapping | Under III. APPROACH: NanoMap point-cloud mapping and the modifications made to it |
| B. RRT Generation | Under III. APPROACH: Algorithm 1, RRT constrained to known map regions with frontier nodes |
| C. Direct Trajectory Optimization | Under III. APPROACH: equations (1)-(5), direct NMPC problem, obstacle distance and collision-probability constraints |
| IV. REAL-TIME SIMULATION STUDY | Parent of the simulation subsections; Figures 2-4 |
| A. Simulation Setup | Under IV. REAL-TIME SIMULATION STUDY: simulator, environments, sensor model |
| B. Experiment 1: Use of NanoMap History | Under IV. REAL-TIME SIMULATION STUDY: effect of depth-measurement history |
| C. Experiment 3: Noise | Under IV. REAL-TIME SIMULATION STUDY: state-noise experiment and constraint comparison (heading printed as 'Experiment 3') |
| V. HARDWARE EXPERIMENTS | Parent of the hardware subsections; Figures 5-10 |
| A. Experimental Set-up | Under V. HARDWARE EXPERIMENTS: aircraft, sensors, onboard computer |
| B. Simulated Perception | Under V. HARDWARE EXPERIMENTS: flights with simulated depth perception |
| C. Control Experiment | Under V. HARDWARE EXPERIMENTS: flights with onboard stereo vision |
| VI. DISCUSSION | Limitations and future work |
| VII. ACKNOWLEDGEMENT | Acknowledgements |
| REFERENCES | Bibliography, 30 entries |

For long sections, search a narrower subsection or prompt. Headings inside fenced quotations are source content, not document section boundaries.

## Supplementary information — [supplement.md](supplement.md)

| Exact heading | Look here for |
| --- | --- |
| Document beginning | Source text or supplied-material notes |

For long sections, search a narrower subsection or prompt. Headings inside fenced quotations are source content, not document section boundaries.

## Assets

Figure and table captions in the documents link to the files below. Open only the needed image; for a table, read its header and relevant rows first.

- `assets/figure/`: main figures (JPEG).
- `assets/supp_figs/`: supplementary and extended-data figures (JPEG).
- `assets/table/`: main tables (CSV, or JPEG when transcription is unreliable).
- `assets/supp_table/`: supplementary tables (CSV, or JPEG fallback).

Asset paths are relative to the skill root. CSVs retain internal blank rows; captions and merged headers may also occupy rows. Consult the document notes before treating every row as data.
