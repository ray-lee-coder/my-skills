# my-skills

> 68 curated AI agent skills, organized in 5 categories.

## 目录

| 分类 | 数量 | 用途 |
|---|---|---|
| `dev/` | 19 | 代码/工程/测试/安全（中文）|
| `doc/` | 5 | 文档/写作/电子表格 |
| `marketing/` | 22 | 内容/品牌/CRO/SEO/视觉 |
| `biz/` | 12 | 电商 5 平台（Amazon/Shopify/TikTok）|
| `meta/` | 10 | 元工具/测试/MCP/学术 |

## 安装

```bash
git clone https://github.com/ray-lee-coder/my-skills.git
cd my-skills
# 每个 skill 目录里有 SKILL.md
# 装到 Hermes/OpenClaw: cp -r dev/*/SKILL.md ~/.hermes/skills/
```

## 评分卡

每个 skill 按 4 维加权（安全性 25% / 有效性 30% / 稳定性 25% / 非重复 20%）入选。详见根目录 SKILL-SCORING.md。

## 来源

5 个 GitHub skill 源仓筛选：
- `laolaoshiren/claude-code-skills-zh`（19）— 中文开发者
- `yizhiyanhua-ai/agent-skills`（19）— 中文办公+视觉+元工具
- `aitytech/agentkits-marketing`（19）— 营销/CRO/SEO
- `nexscope-ai/eCommerce-Skills`（12）— 电商 5 平台
- 1 个 学术/分析 来自 `anbeime/skill` 索引（已砍，因 GitHub 仓库无独立 SKILL.md）

**不收录**：
- `beshuaxian/higgsfield-seedance2-jineng`（无 LICENSE）
- `chanjing-ai/chan-skills`（无 LICENSE + 2.5 月无更新）
- `buluslan/gpt-image2-ecommerce`（强依赖 Codex CLI）
- `helloianneo/awesome-claude-code-skills`（导航非 skill）
- `claude-seo/claude-seo`（与 aitytech 撞 SEO 严重）
- `AgriciDaniel/claude-seo` 完整 25 个（与 aitytech/nexscope 撞 D 维度扣分）

## License

MIT
