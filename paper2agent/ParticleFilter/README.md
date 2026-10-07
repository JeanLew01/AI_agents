# 粒子滤波论文智能体（Paper2Agent）

按 [Paper2Agent](https://github.com/jmiao24/Paper2Agent) 的流程（`~/.claude/skills/paper2agent`），把粒子滤波相关论文（第一批 2 篇，第二批 7 篇）
转换成 Claude Code 可用的“论文技能”，并为有可运行公开代码的一篇（diffres）做了 MCP 工具服务。

## 第一批论文技能：扩散模型与粒子滤波

位置：`dist/particle-filter-agent/skill/<名称>/`，已链接到 `~/.claude/skills/`，在任何目录启动 Claude Code 都能用。

| 技能名 | 论文 | 来源 |
| --- | --- | --- |
| `diffpf-paper` | DiffPF: Differentiable Particle Filtering with Generative Sampling via Conditional Diffusion Models（Wan & Zhao） | IEEE RA-L 2026 预印本，arXiv 2507.15716v2，8 页 |
| `diffusion-resampling-paper` | Diffusion differentiable resampling（Andersson & Zhao） | ICML 2026，arXiv 2512.10401v3，32 页（含附录 A–P） |

用法：直接提问，Claude 会自动调用对应技能；也可以点名，例如

```text
用 diffusion-resampling-paper：Corollary 1 需要哪些假设？N 和 T 应该怎样随 t 增长？
diffpf-paper 里扩散模型的条件输入 c_t 是怎么构造的？和 diffusion-resampling-paper 的思路有什么不同？
```

每个技能包含 `references/paper.md`（全文，公式为 LaTeX，取自作者 arXiv TeX 源码并与 PDF 核对）、
`references/index.md`（章节导航）、`assets/figure/`（图和算法框）、`assets/table/`（表格 CSV）。
文末 “Conversion notes” 写明了来源版本、按原样保留的作者笔误、以及浮动体位置调整。

质量：两个技能都通过 `paper_bundle.py verify --strict`（状态 `reviewed_with_limitations`，“limitations” 指公式改写成 LaTeX
后与 PDF 字形的差异，已逐页说明）。之后由独立校验代理把成品与原 PDF 逐页对比：DiffPF 0 个错误；
diffusion-resampling 发现 2 个错误（脚注吞掉一段正文；表格里 LaTeX 反斜杠被重复）和若干小问题，均已修复并重新构建。
记录在 `paper-review/<名称>/reports/`。

## 第二批论文技能：鲁棒 / 集员 / 盒粒子滤波（2026-10-05）

来自一份 10 篇的阅读清单；能合法免费获取全文的 7 篇已做成技能（同样的逐页审阅 → 构建 → 独立校验流程），位置和用法同上。

| 技能名 | 论文 | 所用版本 | 独立校验 |
| --- | --- | --- | --- |
| `benavoli-piga-2016-paper` | Benavoli & Piga, A probabilistic interpretation of set-membership filtering（Automatica 2016） | arXiv 1505.01034v2（有 TeX） | 0 错误 |
| `benavoli-lower-previsions-2011-paper` | Benavoli, Zaffalon & Miranda, Robust filtering through coherent lower previsions（IEEE TAC 2011） | 作者稿（2010-10-28） | 0 错误 |
| `greco-vasile-2022-paper` | Greco & Vasile, Robust Bayesian Particle Filter for Space Object Tracking Under Severe Uncertainty（JGCD 2022） | Strathprints 录用稿，44 页 | 1 个符号错误（已修）|
| `raices-cruz-robust-is-mcmc-2022-paper` | Raices Cruz 等, Iterative importance sampling with MCMC in robust Bayesian analysis（CSDA 2022） | arXiv 2206.08728v1（有 TeX） | 0 错误 |
| `gning-box-bernoulli-2012-paper` | Gning, Ristic & Mihaylova, Bernoulli Particle/Box-Particle Filters…（IEEE TSP 2012） | Lancaster EPrints 作者稿 | 0 错误 |
| `haj-chhade-box-messages-2014-paper` | Haj Chhadé 等, Non Parametric Distributed Inference in Sensor Networks Using Box Particles Messages（Mathematics in Computer Science 2014） | Springer 开放获取版 | 0 错误 |
| `andrieu-pmcmc-2010-paper` | Andrieu, Doucet & Holenstein, Particle Markov chain Monte Carlo methods（JRSS-B 2010，含讨论与作者答复，74 页） | 期刊排版 PDF（Doucet 主页） | 1 个图裁剪错误（已修），公式 0 错误 |

说明：除两篇有 arXiv TeX 外，其余公式都是从页面图像转写成 LaTeX，再由独立校验代理逐式对照 PDF。作者稿/预印本与正式发表版的编号、措辞可能略有不同，
每个技能的 Conversion notes 写明了所用版本。区间记号里的 `](` 在公式中写作 `]{}(`（渲染相同，避免被当作链接）。

未做成技能的三篇（需要你提供 PDF，放到 `C:\Users\jixia\OneDrive\Desktop\pf_papers\` 后告诉我即可）：

- Le Gland & Oudjane (2003)，SPA：正式版在 Elsevier 开放存档免费，但网站拦截脚本下载：https://www.sciencedirect.com/science/article/pii/S0304414903000413 （已下载的 INRIA 报告 RR-4431 字体为位图，文字层不可用，暂存于 `papers/legland-oudjane-2003.pdf`）
- Abdallah, Gning & Bonnifait (2008)，Automatica，doi:10.1016/j.automatica.2007.07.024（付费）
- Combastel (2016)，Annual Reviews in Control，doi:10.1016/j.arcontrol.2016.07.002（付费）

来源检索记录：`logs/source-search-batch2.md`；各篇来源见 `papers/SOURCES.tsv`。这一批只做论文技能，没有做 MCP（只有 Raices Cruz 一篇有官方 R/Stan 代码）。

## MCP 工具服务：diffres（diffusion-resampling 论文的代码）

交付包：`dist/particle-filter-agent/mcp/diffres-mcp.zip`（已解压副本在同目录 `diffres-mcp/`；说明见包内 `USAGE.md`）。

五个工具，全部直接调用作者代码 `zgbkdlm/diffres @ 767effe`：

| 工具 | 作用 |
| --- | --- |
| `diffres_resample_particles_diffusion` | 对带权粒子做扩散重采样（论文方法） |
| `diffres_resample_particles_baseline` | multinomial / stratified / systematic / stopped-gradient / 熵正则 OT / soft / Gumbel-softmax 重采样 |
| `diffres_run_lgssm_particle_filter` | 线性高斯状态空间模型上的自举粒子滤波（可选任一重采样器），给出对数似然、ESS、滤波矩、对 F/H 的梯度、与卡尔曼滤波的误差 |
| `diffres_run_lgssm_kalman_filter` | 精确卡尔曼滤波 / RTS 平滑、精确似然与梯度 |
| `diffres_simulate_lgssm_data` | 从 LGSSM 生成状态与观测 |

安装与注册（在解压后的 `diffres-mcp/` 目录里）：

```bash
python3.11 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt
claude mcp add diffres -- "$PWD/.venv/bin/python" "$PWD/src/diffres_mcp.py"
```

验证：作者代码的参考运行全部可从保存的输入逐位复现；三个模块各由独立代理验证（共 223 个测试通过）；
47 个 MCP 验收用例在开发环境、全新安装环境、以及把 ZIP 解压到新位置（路径含空格）后都通过，输出与作者代码的参考结果逐位一致
（`mcp-build/diffres/reports/delivery-validation.json`）。
两个需要注意的上游约定：粒子滤波返回的 `nll` 比真实值小 log N（工具另给 `nll_plus_log_n`）；`kl` 是 2×KL，`bures` 是 W2 的平方。

未做：DiffPF 的 MCP。其仓库只有全局定位实验的原始训练代码，没有训练好的权重，需要外部数据集和 1000 个 epoch 的 GPU
训练，本机（WSL 约 7.5 GB 内存）不可行。diffres 的上游 `tests/test_resampling.py`（N=10000）需要 3 GB 以上内存，未运行。

## 目录

- `papers/` 源 PDF（`SOURCES.tsv`、`SHA256SUMS`），`tex-source/` 作者 arXiv TeX 源码
- `paper-review/` 审阅工作目录、审阅/校验报告、协调脚本（`_coord/`、`_tools/`）
- `dist/particle-filter-agent/skill/` 交付的论文技能
- `mcp-build/diffres/` diffres 的 Paper2MCP 项目（环境 `diffres-env/` 约 1.1 GB、参考运行 `notebooks/`、工具 `src/`、测试 `tests/`、报告 `reports/`、交付 `dist/`）；`mcp-build/heavy.sh` 是带内存保护的 JAX 任务启动器
- `COORDINATOR_STATE.md` 进度日志

PDF 版权属于作者和出版方。按你的决定，整个文件夹（含论文 PDF、TeX 源码和技能全文）已推送到公开仓库 JeanLew01/AI_agents；
环境目录、克隆的上游仓库和临时文件由 `~/AI_agents/.gitignore` 排除。
