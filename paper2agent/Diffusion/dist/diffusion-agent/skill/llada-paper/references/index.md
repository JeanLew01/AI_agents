# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph summary |
| 1 Introduction | Generative-modelling principle (1) vs autoregressive factorisation (2); claim that scalability, in-context learning and instruction following come from (1), not (2); reversal curse; contributions [equations (1)-(2); figure-1] |
| 2 Approach | Overview of the probabilistic formulation, pre-training, SFT and inference (Figure 2) [figure-2] |
| 2.1 Probabilistic Formulation | Forward masking process, mask predictor, masked cross-entropy loss with 1/t weight (3), upper bound on negative log-likelihood (4), contrast with BERT fixed ratio and MaskGIT (no 1/t) [equations (3)-(4)] |
| 2.2 Pre-training | Transformer without causal mask, 1B/8B variants, vanilla MHA (no KV cache), 2.3T tokens, 4096 length, 0.13M H800 GPU hours, 1% random-length data, Warmup-Stable-Decay schedule (4e-4 -> 1e-4 -> 1e-5), AdamW wd 0.1, batch 1280 |
| 2.3 Supervised Fine-Tuning | Prompt kept unmasked, response masked, SFT loss (5); 4.5M pairs, \|EOS\| padding treated as a normal token, 3 epochs, lr 2.5e-5 [equations (5)] |
| 2.4 Inference | Reverse sampling from a fully masked response, steps and generation length as hyperparameters, remask s/t of predicted tokens, low-confidence remasking, autoregressive / block-diffusion sampling, low-variance conditional likelihood estimator (6) [equations (6)] |
| 3 Experiments | Evaluation overview |
| 3.1 Scalability of LLaDA on Language Tasks | Figure 3 (six benchmarks vs FLOPs, LLaDA vs own ARM baselines, 1e20-1e23 FLOPs), comparison with Nie et al. 16x compute claim [figure-3] |
| 3.2 Benchmark Results | Table 1 (pre-trained LLaDA 8B Base vs LLaMA3/LLaMA2/Qwen/Mistral/Deepseek), Table 2 (post-trained, SFT only), data-leakage check, block-diffusion scores 78.6 GSM8K / 42.2 Math for Instruct [table-1, table-2] |
| 3.3 Reversal Reasoning and Analyses | Reversal poem completion (496 Chinese poem pairs), Table 4 (forward vs reversal: GPT-4o, Qwen2.5-7B, LLaDA-8B), pointers to sampling ablations, efficiency, CFG [table-4] |
| 3.4 Case Studies | Table 3 (sampling-process visualisation and multi-round dialogue) [table-3] |
| 4 Related Work | Continuous text diffusion, discrete diffusion (Austin et al., Lou et al., Shi et al., Sahoo et al., Ou et al.), scaling laws of MDMs (Nie et al. [27]), adapting ARMs (Gong et al. [72]), a concurrent closed-source diffusion code model [73], image and protein MDMs, sampling acceleration |
| 5 Conclusion and Discussion | Summary, limitations (fixed generation length, no KV cache, ARM baseline not scaled to the same compute, no RL alignment), future work |
| Acknowledgements | Funding |
| References | Bibliography [1]-[125] |
| A Formulation of Masked Diffusion Models | Rigorous MDM formulation |
| A.1 Training | Forward kernel (7)-(8), linear schedule rationale, reverse kernel (9)-(10), time-free data-prediction parameterisation (11), mask-predictor loss (12) and likelihood bound (13) [equations (7)-(13)] |
| A.2 Inference | Equivalent loss with exactly l masked tokens (14) and its lower variance (128 vs >1000 Monte Carlo samples), equivalence with any-order autoregressive models (15), unsupervised classifier-free guidance (16) [equations (14)-(16)] |
| A.3 Algorithms | Algorithms 1-5: pre-training, SFT, conditional log-likelihood evaluation, random remasking and low-confidence remasking samplers [Algorithm 1; Algorithm 2; Algorithm 3; Algorithm 4; Algorithm 5; algorithm-1, algorithm-2, algorithm-3, algorithm-4, algorithm-5] |
| B Experiments | Experimental details |
| B.1 Data Collection and Preprocessing | Pre-training corpus mix (11% Chinese, 61% English, 28% code), BERT quality filter, 1M human + 3.5M synthetic SFT samples, \|EOS\| padding, n-turn dialogue split |
| B.2 Details about Model Training | ARM vs MDM baselines (1.5B identical, 7B ARM vs 8B LLaDA), RMSNorm/SwiGLU/RoPE, Table 5 (architectures), learning rates and batch sizes, 6ND FLOPs, Tables 18-19 (data behind Figure 3) [table-5, table-18, table-19] |
| B.3 Ablation on Classifier-free Guidance | Table 6 (with vs without CFG, scale searched in {0.5, 1, 1.5, 2}) [table-6] |
| B.4 Details and Ablation on Sampling Strategies | Figure 4 (autoregressive, block diffusion, block diffusion LLaDA / semi-autoregressive remasking), setup, EOS-confidence fix, Tables 7-8 (strategies, block lengths), Table 9 (random vs low-confidence remasking) [figure-4, table-7, table-8, table-9] |
| B.5 Ablation on Generated Length | Table 10 (lengths 256/512/1024) [table-10] |
| B.6 Standard Benchmarks and Evaluation Details | Benchmark list, likelihood vs generation protocols, lm-evaluation-harness vs internal library, Monte Carlo sample counts, answer lengths per benchmark for Instruct |
| B.7 Analysis of Sampling Efficiency | Figure 5 (quality vs throughput, A100, LLaMA3 with/without KV cache), Table 11 (memory), prompt lengths [figure-5, table-11] |
| B.8 Evaluation on iGSM Dataset | iGSM example and prompt (mod-5 arithmetic), Table 12 (LLaMA3 8B vs LLaDA 8B Base, 4-6 solution steps) [table-12] |
| B.9 Poem Completion Tasks | Two examples of the forward/reversal poem dataset |
| B.10 More Case Studies | Tables 13-17: block-diffusion sampling visualisation, random-remasking multi-turn dialogue, single- and multi-turn dialogue cases, poem reversal cases vs GPT-4o [table-13, table-14, table-15, table-16, table-17] |
| C Impact Statement | Broader impact |

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
