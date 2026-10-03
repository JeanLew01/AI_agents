# NMPC 论文智能体（Paper2Agent）

按 [Paper2Agent](https://github.com/jmiao24/Paper2Agent) 的流程（技能版本 8c2d059），把七篇采样式 NMPC 相关论文
转换成可供 Claude Code 使用的“论文技能”，并为其中两篇有公开代码的论文准备 MCP 工具服务。

## 现在可以用的：七个论文技能

位置：`dist/nmpc-agent/skill/<名称>/`，并已链接到 `~/.claude/skills/`，在任何目录启动 Claude Code 都能用。

| 技能名 | 论文 | 来源 |
| --- | --- | --- |
| `dial-mpc-paper` | DIAL-MPC: Full-Order Sampling-Based MPC via Diffusion-Style Annealing | arXiv 2409.15610v1 |
| `model-based-diffusion-paper` | Model-Based Diffusion for Trajectory Optimization | NeurIPS 2024 |
| `pac-nmpc-paper` | Probably Approximately Correct NMPC (PAC-NMPC) | arXiv 2210.08092v3（RA-L 2023） |
| `pac-nmpc-value-function-paper` | PAC-NMPC with a Learned Value Function | arXiv 2309.13171v3（ACC 2025） |
| `rl-guided-pac-nmpc-paper` | RL-Guided PAC-NMPC | arXiv 2609.39854v1 |
| `post-stall-navigation-paper` | Post-Stall Navigation with Fixed-Wing UAVs using Onboard Vision | arXiv 2201.01186v1（ICRA 2022） |
| `urban-swarm-fixed-wing-paper` | Agile Fixed-Wing UAVs for Urban Swarm Operations | Field Robotics 3:725-765（2023） |

用法：直接提问，Claude 会自动调用对应技能；也可以点名，例如

```text
用 pac-nmpc-paper 技能：PAC-NMPC 的代价上界 (2) 依赖哪些假设？置信项里各个量是什么？
对比 dial-mpc-paper 和 model-based-diffusion-paper：两者的退火/扩散日程分别怎么定义？
```

每个技能包含 `references/paper.md`（全文，公式为 LaTeX）、`references/index.md`（章节导航）、
`assets/figure/`（图和算法框）、`assets/table/`（表格 CSV）。文末 “Conversion notes” 记录了来源版本和转换时的注意事项。

质量状态：七个技能都通过了 `paper_bundle.py verify --strict`（状态 `reviewed_with_limitations`，
“limitations” 指公式改写成 LaTeX 后与 PDF 字形流的差异，已逐页说明）；每篇都由独立的校验代理把成品与原 PDF
逐页对比，正文、公式、表格、参考文献未发现错误。审阅与校验记录在 `paper-review/<名称>/reports/`。

## 尚未完成的：两个代码仓库的 MCP 工具

| 仓库 | 进度 |
| --- | --- |
| LeCAR-Lab/model-based-diffusion @c1eb913 | 环境、工具筛选完成；参考执行部分完成；工具封装和校验未做 |
| LeCAR-Lab/dial-mpc @871c84f | 环境、工具筛选完成；GPU 线性代数库版本问题已定位；仿真一次未跑成 |

卡点是内存：本机 WSL 只有约 7.5 GB，VS Code 常驻约 3.5-4 GB，JAX 仿真与多个代理并行时两次把 WSL 拖死。
`mcp-build/HEAVY_JOBS_DISABLED` 存在期间，所有仿真任务都被 `mcp-build/heavy.sh` 拒绝。
建议在 Windows 的 `C:\Users\<用户名>\.wslconfig` 中提高内存后再继续（见 `COORDINATOR_STATE.md`）。
PAC-NMPC 系列五篇没有公开代码，只有论文技能。

## 目录

- `papers/` 源 PDF（`user-annotated/` 是带高亮的原件），`tex-source/` 作者的 arXiv TeX 源码（转写公式用）
- `paper-review/` 审阅工作目录、审阅与校验报告、协调脚本（`_coord/`、`_tools/`）
- `dist/nmpc-agent/skill/` 交付的论文技能；`dist/nmpc-agent/mcp/` 预留给 MCP 服务
- `mcp-build/` 两个仓库的 Paper2MCP 工作目录（环境、扫描报告、参考执行证据）
- `COORDINATOR_STATE.md` 进度日志与续做说明

`~/AI_agents` 有 GitHub 远端：PDF、TeX 源码和环境目录不要提交（见 `.gitignore`）。
