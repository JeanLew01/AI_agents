# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| 1. Introduction | Motivation and contributions |
| 2. Related Work | Parent of 2.1 Quadcopter Planning and Control, 2.2 Fixed-Wing Planning and Control (2.2.1 Low angle-of-attack, 2.2.2 Post-stall regime), 2.3 UAV Navigation with Onboard Sensors, 2.4 Control of Multiple Dynamic Aerial Vehicles |
| 3. Approach | Overview of the approach; Figures 1-2; parent of 3.1 and 3.2 |
| 3.1. Dynamics Model | Aircraft dynamics model, equations (1)-(15); Figure 3 |
| 3.2. Control Strategy | Control architecture; Figure 4; parent of 3.2.1-3.2.3 |
| 3.2.1. RRT generation and spline-based smoothing | Under 3.2: equations (16)-(21) |
| 3.2.2. Direct trajectory optimization | Under 3.2: direct trajectory optimisation problem, equations (22)-(23) |
| 3.2.3. Local linear feedback control | Under 3.2: local feedback, equations (24)-(26) |
| 4. Real-time Trajectory Optimization Performance | Computation time and tracking cost versus number of knot points; comparison of Hermite-Simpson and Euler transcriptions |
| 5. Motion Capture Experiments | Figures 5-6; parent of 5.1 Experimental Setup, 5.2 System Identification (Figures 7-8), 5.3 Control Experiments, 5.4 Results (Figures 9-10) |
| 6. Outdoor Experiments with Onboard Processing | Parent of 6.1-6.7 |
| 6.1. Onboard Processor Selection | Under 6: choice of onboard computer |
| 6.2. The ACCIPITER Software Stack | Under 6: software stack; Figure 11 and its processor table (figure-11-table) |
| 6.3. The ACCIPITER Hardware Stack | Under 6: hardware stack; Figure 12 |
| 6.4. System Identification and Controller Configuration | Under 6: identification and controller settings for the outdoor aircraft |
| 6.5. At-Altitude Tests in Simulated Urban Environments | Under 6: Figure 13 |
| 6.6. Flight Tests in Physical Urban Environment | Under 6: Figure 14 |
| 6.7. Wind Compensation | Under 6: Figure 15 |
| 7. Vision-Based Navigation and Feature Detection | Parent of 7.1 Mapping, 7.2 Dynamic RRT Generation (Algorithm 1), 7.3 Collision Constraints for Trajectory Optimization, 7.4 Experimental Setup, 7.5-7.7 |
| 7.5. Simulated Perception Navigation Experiment | Under 7: Figure 16 |
| 7.6. Vision-based Collision-Free Navigation Experiment | Under 7: Figures 17-21 |
| 7.7. Feature Detection at High Speeds and Aggressive Attitudes | Under 7: Figures 22-23 |
| 8. Swarm System Integration for Urban Operations | Figure 24; parent of 8.1-8.6 |
| 8.1. Automatic Take-Off | Under 8: Figure 25 |
| 8.2. Automatic Landing | Under 8: Figure 26 |
| 8.3. Multi-UAV Collision Avoidance | Under 8: Figures 27-28 |
| 8.4. Swarm System Integration | Under 8: integration with the swarm architecture |
| 8.5. Swarm System Integration Experiments | Under 8: Figure 29 |
| 8.6. Future Steps for Swarm System Integration | Under 8: Figures 30-33 are placed here |
| 9. Discussion | Discussion; Figure 34 |
| Acknowledgments | Acknowledgements |
| Appendices | Parent of A. Analysis of Post-Stall Turns and B. Energy Analysis |
| A. Analysis of Post-Stall Turns | Under Appendices: equations (27)-(33) |
| B. Energy Analysis | Under Appendices: equations (34)-(40), Table 1, Figure 35 |
| ORCID | Author ORCID identifiers |
| References | Bibliography, 94 entries in author-year style; followed by 'How to cite this article' and the publisher's note |
| Conversion notes | Source details, transcription method, printed oddities, float placement |

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
