# 扩散语言模型论文智能体（Paper2Agent）

按 [Paper2Agent](https://github.com/jmiao24/Paper2Agent) 的流程（`~/.claude/skills/paper2agent`），把扩散模型相关论文转换成
Claude Code 可用的“论文技能”。约定与同级的 `Reachability/`、`NMPC/`、`ParticleFilter/` 相同。

## 论文技能

位置：`dist/diffusion-agent/skill/<名称>/`，已链接到 `~/.claude/skills/`，在任何目录启动 Claude Code 都能用。

| 技能名 | 论文 | 来源 |
| --- | --- | --- |
| `llada-paper` | Large Language Diffusion Models（LLaDA；Nie, Zhu, You, …, Chongxuan Li；NeurIPS 2025） | arXiv 2502.09992v3，33 页（正文 1–10，参考文献 10–18，附录 A–C 19–33） |

用法：直接提问，Claude 会自动调用技能；也可以点名，例如

```text
用 llada-paper：式 (3) 的 1/t 权重为什么能给出负对数似然的上界？和 MaskGIT 的目标有什么不同？
llada-paper 里低置信度 remasking（Algorithm 5）每一步重新遮住多少个 token？semi-autoregressive 的 block 长度怎么选？
llada-paper 表 1 里 LLaDA 8B Base 和 LLaMA3 8B Base 的 GSM8K、MMLU 各是多少（几 shot）？
```

技能包含 `references/paper.md`（全文，公式为 LaTeX，取自作者 arXiv TeX 源码并与 PDF 逐式核对）、`references/index.md`（章节导航）、
`assets/figure/`（图 1–5、算法框 1–5）、`assets/table/`（表 1–2、4–12、15–19 为 CSV；表 3、13、14 是 token 着色可视化，存为图片并附文字转写）。
文末 “Conversion notes” 写明来源版本、按原样保留的作者笔误、浮动体位置调整和表格约定。

质量：通过 `paper_bundle.py verify --strict`（状态 `reviewed_with_limitations`，“limitations” 指公式写成 LaTeX 后与 PDF 字形的差异，已逐页说明）。
三个审阅代理分段审阅（1–9、10–22、23–33 页），之后两个独立校验代理把成品与 PDF 逐页对比：
公式 (1)–(16)、算法 1–5、所有表格数字、125 条参考文献、中文诗句均无错误；发现 1 个结构错误
（表 16 中两个同名 “Daily life” 对话会被读成一个，已改为 “Daily life (1)/(2)”）和若干格式/说明小问题，均已修复并重新构建。
报告在 `paper-review/llada-paper/reports/`。

值得注意的一点（已写入 Conversion notes，原文未改）：Algorithm 5 第 12 行把 $n_{un}=\lfloor L(1-s)\rfloor$ 定义为时刻 $s$ 的
**未遮住** token 数，第 14–15 行却写“重新遮住置信度最低的 $n_{un}$ 个位置”；按字面读数量是反的，应为 $L-n_{un}$。
第 2.4 节（重新遮住 $s/t$ 比例）和官方代码 `generate.py`（每步解开置信度最高的固定数量 token）都与 $L-n_{un}$ 一致。

## MCP 工具服务：不做（2026-10-14 决定）

官方代码 `ML-GSAI/LLaDA` 的可用接口（`generate()`、`get_log_likelihood()`）都必须加载 8B 模型（bf16 约 16 GB），
本机 8 GB 显存放不下。按你的决定，本集合只交付论文技能。代码克隆保留在 `mcp-build/LLaDA-source-inspection`（commit 9182493）供查看。

## 目录

- `papers/` 源 PDF（`SOURCES.tsv`、`SHA256SUMS`），`tex-source/llada/` 作者 arXiv TeX 源码
- `paper-review/` 审阅工作目录、审阅/校验报告（`llada-paper/reports/`）、协调脚本（`_coord/`，`final.sh llada-paper` 重新构建并严格校验）、
  审阅/校验说明（`_tools/REVIEWER_BRIEF.md`、`VERIFIER_BRIEF.md`、`LLADA_ASSIGNMENT.md`）
- `dist/diffusion-agent/skill/` 交付的论文技能
- `mcp-build/LLaDA-source-inspection/` 官方代码（仅供查看，git 忽略）
- `COORDINATOR_STATE.md` 进度日志

PDF 和 TeX 源码版权属于作者。没有提交或推送到 git。
