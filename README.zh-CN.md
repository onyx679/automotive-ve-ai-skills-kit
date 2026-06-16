# Automotive VE AI Skills Kit

[![test](https://github.com/onyx679/automotive-ve-ai-skills-kit/actions/workflows/test.yml/badge.svg)](https://github.com/onyx679/automotive-ve-ai-skills-kit/actions/workflows/test.yml)

[English](./README.md) | [中文](./README.zh-CN.md)

面向汽车价值工程（VE/VAVE）提效场景的 AI Skill 模板与轻量级工作流工具包。

本仓库是一个可公开展示的作品集级 demo，不包含赛力斯、供应商或任何真实车型项目的保密数据。

作品页：https://onyx679.github.io/automotive-ve-ai-skills-kit/

补充电商流程 demo：https://github.com/onyx679/ecommerce-ops-ai-workflow-kit

## 为什么做这个项目

汽车价值工程团队有大量重复、文档密集型工作：

- BOM 与报价信息标准化
- VAVE 降本机会池起草
- 成本评审会议纪要整理
- SOP 与最佳实践文档沉淀
- AI Skill 使用反馈与迭代

本项目展示如何把这些流程转化为可复用的 AI agent Skills，同时把工程、质量、供应商和成本决策保留在人工审核链路中。

## 仓库内容

```text
automotive-ve-ai-skills-kit/
  CONTRIBUTING.md
  skills/
    ve-scenario-miner/
    vave-cost-opportunity/
    ve-manual-writer/
    skill-adoption-feedback/
    ve-evidence-auditor/
    ve-skill-benchmark-adapter/
  src/ve_ai_skills_kit/
    scoring.py
    adoption.py
    readiness.py
    evidence.py
    adaptation.py
  scripts/
    score_skill_candidates.py
    generate_adoption_report.py
    check_bom_quote_readiness.py
    generate_evidence_matrix.py
    adapt_skill_benchmarks.py
  examples/
    scenario_candidates.csv
    adoption_metrics.csv
    bom_quote_readiness.csv
    evidence_claims.csv
    skill_benchmarks.csv
    output/
  tests/
```

## Skills

| Skill | 用途 |
|---|---|
| `ve-scenario-miner` | 从访谈或会议纪要中提取高频价值工程任务和 Skill 候选场景。 |
| `vave-cost-opportunity` | 将 BOM、报价、benchmark 和会议信息整理为 VAVE 机会池草稿。 |
| `ve-manual-writer` | 将流程笔记转化为 SOP、FAQ、检查清单和最佳实践文档。 |
| `skill-adoption-feedback` | 分析 Skill 使用、用户反馈、提效效果和迭代优先级。 |
| `ve-evidence-auditor` | 审计简历、作品集、release 和汇报中的 claim，确保每个表述都有证据和边界。 |
| `ve-skill-benchmark-adapter` | 对社区 AI Skill 模式进行 benchmark，并在注明来源边界的前提下改造为 VE/VAVE 场景实现。 |

## 脚本

场景候选评分：

```bash
python scripts/score_skill_candidates.py examples/scenario_candidates.csv
```

生成 adoption report：

```bash
python scripts/generate_adoption_report.py examples/adoption_metrics.csv
```

检查 BOM 与报价行是否适合进入 AI 辅助 VAVE 起草：

```bash
python scripts/check_bom_quote_readiness.py examples/bom_quote_readiness.csv
```

生成证据化 claim 矩阵：

```bash
python scripts/generate_evidence_matrix.py examples/evidence_claims.csv
```

生成社区 Skill 改造评估报告：

```bash
python scripts/adapt_skill_benchmarks.py examples/skill_benchmarks.csv
```

示例输出：

- [Skill candidate ranking](./examples/output/skill_candidate_ranking.md)
- [Adoption report](./examples/output/adoption_report.md)
- [BOM and quotation readiness report](./examples/output/bom_quote_readiness_report.md)
- [Evidence claim matrix](./examples/output/evidence_claim_matrix.md)
- [Skill benchmark adaptation report](./examples/output/skill_benchmark_adaptation_report.md)

运行测试：

```bash
python -m unittest discover -s tests
```

## 证据类型

对成本和供应商敏感流程，本项目将结论拆分为：

- `Fact`：源材料中直接存在的事实
- `Calculation`：由明确数字和可见公式推导出的计算
- `Hypothesis`：合理但未验证的假设
- `Needs confirmation`：必须人工确认的事项

AI 助手不能编造成本、供应商、质量或工程可行性结论。

## Readiness Gate

在起草 VAVE 机会前，先用 BOM/报价 readiness check 找出缺少供应商、年用量、税费口径或证据来源的行。缺少目标成本、材料或工艺信息的行会进入业务复核队列，而不是直接交给 AI 起草。

## 方法论

详见 [docs/methodology.md](./docs/methodology.md)。项目采用六步工作流：

0. 检查输入就绪度
1. 挖掘业务流程
2. 评分 Skill 候选场景
3. 产品化 Skill
4. 保留人工审核
5. 衡量 adoption
6. 负责任地改造社区模式

## 作品集定位

本项目支撑的候选人定位是：

> 面向汽车价值工程团队的 AI 提效 BP / Skill 产品经理。

它展示业务流程分析、AI Skill 设计、VAVE 流程理解、文档沉淀能力和 adoption 指标设计能力。

补充电商流程工具包展示同一套工作方式在另一个业务场景中的迁移：把商品、订单、库存、客服和复盘工作标准化为 CSV 输入、Markdown 风险周报、行动项队列、测试和人工审核边界。它用于证明流程提效方法可迁移，不用于冒充汽车领域业务经历。

## License

MIT
