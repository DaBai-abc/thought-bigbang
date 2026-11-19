---
name: thought-bigbang
display_name: 思维大爆炸
display_name_en: Thought Big Bang
description: 内容创作者的分步创作流水线「思维大爆炸」，把模糊念头推到可公开发布的成稿。当用户提出一个点子、一个痛点、一段对话、一个信息差或一个成熟方案，想把它变成短视频、口播视频、图文文案、海报、播客或博客时使用；也适用于「我想做条视频但不知道从哪下手」「这个想法能做成什么内容」「帮我从零策划一条内容」「这痛点怎么写成文案」「用思维大爆炸跑一遍」这类从灵感起步的创作请求。本技能采用闸门式步进，每步产出后停下等用户拍板，不一次性生成成稿。
description_zh: 内容创作者的分步创作流水线。从一个点子、痛点、对话、信息差或成熟方案出发，经接入、人群定位、方向发散、资源评估、文案定稿、素材生产、配音合成七个阶段，产出可直接发布的视频、文案、海报、播客或博客。闸门式步进，每个阶段停下等用户拍板，可随时跳步或回退。
description_en: Step-by-step content creation pipeline for creators, taking a vague idea to a publishable piece. Use it when the user brings a spark — an idea, a pain point, a conversation, an information gap, or a ready plan — and wants a short video, talking-head video, carousel copy, poster, podcast, or blog post. Runs on gated stepping, where every stage pauses for user sign-off instead of generating the final draft in one shot.
agent_created: true
version: 1.1.0
---

# 思维大爆炸 · Thought Big Bang

## 定位

把创作者从"有个模糊的念头"推到"一条敢发、也发得出去的内容"。

真正的难点不在生成环节，在三个决策点：**定位准不准、方向选得对不对、方案配不配得上创作者手里的资源**。生成能力是饱和的，决策质量不是。因此全部设计重量压在第 1 到第 4 步。

## 铁律

违反下列任一条，本次流程视为失败。

1. **一次只推进一步。** 完成当前阶段后必须停下，把产出摆给用户，等其明确表态。不得在用户未回应时连续推进两个阶段，不得用"我顺便把下一步也做了"作为理由。
2. **每步必须落盘。** 每个阶段的产出写入项目目录对应文件，并在 `00-state.md` 更新进度。用户中途离开、隔天回来、换会话，都能从断点续跑。
3. **不替用户拍板。** 定位、方向选择、最终收敛这三处，给出候选、推荐和理由，选择权留给用户。禁止用"我认为你应该做 X"直接锁定。
4. **方向未定不产素材。** 第 4 步（文案定稿）未通过闸门，禁止生成任何图片、视频、配音。素材成本一旦产生就无法回收，而方向错误的概率在这一步之前始终偏高。
5. **全形态不等于同时做四份。** 一次只跑一条主线，其余形态在第 4 步之后按需派生。同时铺开四个形态等于四个都不及格。
6. **每阶段最多问三个问题。** 能推断的不问，能给的直接给默认值并标注"若不对请改"。问题用选择题承载（AskUserQuestion），每个选项带明确后果描述。
7. **文案交付前过去 AI 味。** 第 4 步的文案定稿必须过一遍 `de-ai-flavor` 的四关：主语清晰、的 不省略、双字到位、朗读通顺。念出来像人话才算过。
8. **每个判断都要能追到依据。** 每个阶段的结论写入 `决策链.md`，含决策、依据、反证条件、影响范围。写不出依据的结论直接删掉。这份文件不是为了展示思考过程，是为了让用户能逐条反驳——用户说"感觉不对"时，逐条念依据让他指出哪条不成立，只改那一条。

## 状态机

七个阶段。每个阶段进入前读对应手册，产出写对应文件。

| 阶段 | 名称 | 读 | 产出 | 闸门问题数 |
|---|---|---|---|---|
| S0 | 接入 | `references/s0-intake.md` | `01-intake.md` | 1–2 |
| S1 | 诉求拆解与人群定位 | `references/s1-audience.md` | `02-audience.md` | 2–3 |
| S2 | 方向发散 | `references/s2-angles.md` | `03-angles.md` | 1 |
| S3 | 资源评估与收敛 | `references/s3-feasibility.md` | `04-decision.md` | 2–3 |
| S4 | 文案定稿 | `references/s4-script.md` | `05-script.md` | 1 |
| S5 | 素材生产 | `references/s5-assets.md` | `06-assets.md` + `素材/` | 1 |
| S6 | 配音合成与分发 | `references/s6-produce.md` | `07-production.md` | 1 |

S0 到 S3 是主干，所有内容形态共用。S4 定稿后按目标形态分支：视频走 S5v→S6v，图文/海报走 S5i→S6i，播客/博客走 S5a→S6a。分支细则在各阶段手册内。

## 闸门格式

每个阶段收尾必须输出这个结构，缺项视为未收尾。

```
【S<n> <阶段名>】已完成
产出：<文件相对路径>  <若内容短，直接内联展示关键部分>
这一阶段定下的：<一句话概括核心决策>
仍未确定的：<遗留项，没有就写"无">

下一步是 <S<n+1> 阶段名>，需要你先定这几件事：
1. <问题，附推荐值>
2. <问题，附推荐值>

回「继续」就往下走；要改当前阶段就说哪里不对；想直接跳到某一步也可以说步号。
```

## 项目目录

```
~/内容工坊/<YYYYMMDD>-<短slug>/
├── 00-state.md          进度与已定决策，唯一的状态源
├── 决策链.md            每条判断的依据与反证条件
├── 01-intake.md         起点素材与原始意图
├── 02-audience.md       人群定位卡
├── 03-angles.md         3–5 个方向
├── 04-decision.md       收敛后的执行方案
├── 05-script.md         定稿文案与形态派生稿
├── 06-assets.md         素材清单与来源
├── 07-production.md     生产参数与发布检查
├── panel/
│   └── data.json        面板数据，给 render_panel.py 读
├── panel.html           渲染出的交互面板
└── 素材/                实际图片、音频、视频文件
```

`00-state.md` 用 `assets/state-template.md` 初始化，`panel/data.json` 用 `assets/data-template.json` 初始化。每次推进后立刻回写，不要攒着。

## 面板

三块内容做成可交互面板：S2 的方向墙、S3 的资源评分器、S5 的镜头看板。

**何时渲染。** 只在三个阶段收尾时渲染，不要每步都渲染：

- S2 完成 → 把方向写入 `panel/data.json` 的 `angles`，渲染一次，让用户在墙上直接选和淘汰。
- S3 完成 → 把评分和收敛结果写入 `score` 与 `decision`，渲染一次。评分器只在对话里问不清楚时用，用户能一句话答完就不用开面板。
- S5 完成 → 把镜头写入 `shots`，渲染一次，勾选已就位的镜头。

```
python3 <skill>/scripts/render_panel.py --project <项目目录> --init
```

渲染完用 `present_files` 打开 `panel.html`。面板在右侧预览区运行，可离线。

**面板不改状态。** 用户在面板里勾选、打分、淘汰之后，通过「导出数据 JSON」拿回数据，覆盖 `panel/data.json`，再据此更新 `00-state.md` 和各阶段产出文件。面板是看板，不是唯一状态源。

**不要为了演示而渲染。** 没有真实数据时渲染出来是空壳，反而干扰。

## 首次进入

1. 判断用户是否已给出起点素材。给了就从 S0 直接开始；只给了"我想做内容"这类空话，先问一句"你手里现在有什么——一个点子、一个让你不痛快的事、一段对话、一个别人不知道的信息，还是一个已经想得比较成熟的方案"。
2. 判断是否已有进行中的项目：检查 `~/内容工坊/` 下最近修改的目录，若 `00-state.md` 显示未完成，主动问"上次做到 S<n>，接着走还是重开一条"。
3. 建立项目目录，写 `00-state.md`，然后进入 S0。

## 关于"五六步出成品"

这个承诺成立的前提是创作者本人在每个闸门给出真实判断。如果用户希望完全放手、不要被问，明确告知：那属于另一条路径（一次性生成），本流程不适用，因为跳过决策点的产出大概率不能用。

## 资源

- `references/s0-intake.md` — 五种起点的识别与素材固化
- `references/s1-audience.md` — 诉求拆解与人群定位
- `references/s2-angles.md` — 方向发散的质量标准
- `references/s3-feasibility.md` — 能力资源评估与收敛
- `references/s4-script.md` — 文案定稿与形态派生
- `references/s5-assets.md` — 素材检索与生成
- `references/s6-produce.md` — 配音、合成、分发
- `references/question-bank.md` — 各阶段提问库与推荐默认值
- `references/anti-patterns.md` — 常见失败模式与识别信号
- `references/decision-chain.md` — 决策链格式与各阶段落链要求
- `assets/state-template.md` — 项目状态文件模板
- `assets/data-template.json` — 面板数据模板
- `scripts/render_panel.py` — 把 data.json 渲染成单文件面板，带自检
- `templates/panel.html` — 面板模板，含方向墙、评分器、镜头看板三个标签
