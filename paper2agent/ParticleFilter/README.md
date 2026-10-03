# 粒子滤波论文智能体（Paper2Agent）

按 [Paper2Agent](https://github.com/jmiao24/Paper2Agent) 的流程（`~/.claude/skills/paper2agent`），把两篇粒子滤波相关论文
转换成 Claude Code 可用的“论文技能”，并为有可运行公开代码的一篇（diffres）做了 MCP 工具服务。

## 论文技能（已完成）

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

PDF 版权属于作者和出版方；`~/AI_agents` 有 GitHub 远端，`papers/`、`tex-source/`、`dist/.../skill/`（含论文全文）和
`mcp-build/diffres/diffres-env/` 不要提交。
