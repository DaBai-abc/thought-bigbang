# 思维大爆炸 · Thought Big Bang

> 从一个模糊念头，到一条敢发的内容。

一个给内容创作者用的分步创作流水线。不是生成器，是**跟你一起做决策**的协作流程。

---

## 它解决什么

现在的内容工具不缺生成能力。你给一个点子，它能给你十版文案——但十版都不能用。

因为它不知道你在跟谁说话，不知道你手里有什么，不知道你能做到什么程度。它只是在猜。

真正卡住创作者的是三个问题：

1. **这条内容到底说给谁听**——大多数人给的是标签（"年轻人""职场人"），不是人。
2. **能从哪个角度切**——想出来的第一个角度，通常是最平庸的那个。
3. **这个方案我做得完吗**——想做的和能做的之间，隔着一个烂尾。

这三个问题都没解决，生成再多文案也没用。

思维大爆炸把所有重量压在这三处，生成放在最后。

---

## 七个阶段

| 阶段 | 做什么 | 产出 |
|---|---|---|
| S0 接入 | 识别起点类型：点子 / 痛点 / 对话 / 信息差 / 成熟方案 | 一份原话记录，一字不改 |
| S1 人群定位 | 追到具体场景、时刻、处境、情绪 | 人群定位卡 |
| S2 方向发散 | 3–5 个**互斥**方向，强制覆盖多种角度类型 | 方向清单 |
| S3 资源评估 | 八维度打分，资源决定形态，不做超出能力的方案 | 执行方案 + 明确不做 |
| S4 文案定稿 | 主线四段 → 按目标形态派生 | 可发文本 |
| S5 素材生产 | 检索 → 生成 → 拍摄，按成本从低到高 | 镜头清单 |
| S6 配音分发 | 配音参数、平台规格、发布检查 | 发布记录 |

S0 到 S3 全形态共用主干，S4 之后按目标形态分支：视频、口播、图文、海报、播客、博客。

---

## 三条机制

### 1. 闸门式步进

每个阶段收尾必须输出固定结构，然后**停下来**：

```
【S2 方向发散】已完成
产出：03-angles.md
这一阶段定下的：五个方向的差异化角度
仍未确定的：哪个方向你最有反应

下一步是 S3 资源评估，需要你先定：
1. 你的出镜意愿、设备、时间这三项
2. 方案规模接受 60 秒口播吗

回「继续」就往下走；要改当前阶段就说哪里不对；想跳到某一步也可以说步号。
```

你没说继续，它不会自己往下跑。

这一条写成了硬规则，不是建议——因为跳过决策点的产出，大概率不能用。

### 2. 决策链

每个判断后面挂可追溯的依据，以及**它什么情况下会失效**：

```markdown
## D-003 · S1

决策：锁定"30 岁上下、被优化过、正在自责的打工人"
依据：用户原话第 2 段出现 4 次"是不是我不行"，情绪指向自责而非经济压力
反证条件：如果受众其实以应届生为主，这条要改成"刚入职就赶上裁员"，S2 全部重做
影响范围：S2 五个方向、S4 钩子语气、S6 发布时间
```

它记录的不是 AI 想了什么——那个拿不到，事后复述的都是编的。它记录的是**你能不能反驳**。

你说「感觉不对」的时候，逐条念依据给你听，你指出哪条不成立，只改那一条。已经对的部分不会被一起冲掉。

### 3. 三块交互面板

S2 之后打开方向墙，五个方向并排，勾选、淘汰、对比。
S3 之后打开评分器，八个维度三档按钮，实时出判定。
S5 之后打开镜头看板，勾掉已就位的，剩下就是还缺什么。

单文件 HTML，可离线，不依赖任何服务。

---

## 安装

克隆到 WorkBuddy 的 skills 目录：

```bash
git clone https://github.com/DaBai-abc/thought-bigbang.git ~/.workbuddy/skills/thought-bigbang
```

Windows 放到 `%USERPROFILE%\.workbuddy\skills\thought-bigbang`。

重启会话后生效。它是纯 Markdown + 一个 Python 脚本，没有依赖需要安装。

---

## 用法

直接说一句话就行，五种起点任选：

- 「我想做条关于 XX 的视频」
- 「这件事让我挺不痛快的，能做成什么内容」
- 「有个人跟我说了句话，我觉得挺有意思」
- 「我发现很多人不知道一个事」
- 「我有个想法已经想挺清楚了，帮我理成内容」

它会先判断你手里是什么，然后从 S0 开始。

**不想被问太多**的话可以直说，它会合并问题、给默认值让你否决。但完全放手不做决策的路径它不提供——那是另一个产品的事。

---

## 目录结构

```
thought-bigbang/
├── SKILL.md                  主控规程：状态机、铁律、闸门格式
├── references/
│   ├── s0-intake.md          S0 接入
│   ├── s1-audience.md        S1 人群定位
│   ├── s2-angles.md          S2 方向发散
│   ├── s3-feasibility.md     S3 资源评估与收敛
│   ├── s4-script.md          S4 文案定稿
│   ├── s5-assets.md          S5 素材生产
│   ├── s6-produce.md         S6 配音分发
│   ├── decision-chain.md     决策链规范
│   ├── question-bank.md      提问库
│   └── anti-patterns.md      22 种失败模式与修正动作
├── scripts/
│   ├── render_panel.py       面板渲染器
│   └── validate.py           独立校验器（不依赖 WorkBuddy）
├── templates/
│   └── panel.html            三标签面板模板
└── assets/
    ├── state-template.md     项目状态模板
    └── data-template.json    面板数据模板
```

---

## 贡献

最有价值的贡献是这三类：

1. **真实跑过的案例**——你用它做完一条内容，把卡住的地方和改法写进 issue。比抽象建议有用十倍。
2. **角度类型库**——`references/s2-angles.md` 里现在列了七种角度结构，不够。你见过有效但没被收录的，加进去。
3. **失败模式**——`references/anti-patterns.md` 现在 22 条。你踩过的坑，识别信号写清楚，加进去。

不适合的贡献：让它生成得更多、更快、更自动。这个项目的价值恰恰在"慢下来想清楚"。

具体流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## License

MIT。拿去用，改了也行，商用也行。

---

# Thought Big Bang

> From a vague idea to something you dare to publish.

A step-by-step creation pipeline for content creators. Not a generator — a collaboration process that **makes decisions with you**.

## The problem

Content tools today don't lack generation. Give one a spark and it hands you ten versions of copy. None of them work, because it doesn't know who you're talking to, what you have on hand, or what you're actually capable of finishing.

Three questions block most creators:

1. **Who is this really for** — most people answer with labels ("young people", "professionals"), not people.
2. **What angle can this take** — the first angle you think of is usually the most forgettable one.
3. **Can I actually finish this** — between what you want to make and what you can make sits an abandoned folder.

Generate more copy and all three remain unsolved. This pipeline puts its weight on those three points and leaves generation for last.

## Seven stages

| Stage | What happens | Output |
|---|---|---|
| S0 Intake | Classify the spark: idea / pain point / conversation / information gap / ready plan | Verbatim notes, unedited |
| S1 Audience | Narrow to a specific moment, situation, emotion | Audience card |
| S2 Angles | 3–5 **mutually exclusive** angles across multiple types | Angle list |
| S3 Feasibility | Eight-dimension scoring; resources decide the format | Plan + explicit non-goals |
| S4 Script | Four-part spine, then adapt to target format | Publishable text |
| S5 Assets | Search → generate → shoot, cheapest first | Shot list |
| S6 Produce | Voiceover, platform specs, publish checklist | Publish record |

S0–S3 are shared across all formats. After S4 it branches into video, talking-head, carousel, poster, podcast, or blog.

## Three mechanisms

**Gated stepping.** Every stage ends with a fixed closing block and stops. No silence, no auto-advance. Skipping decision points produces work that can't be used.

**Decision chain.** Every judgment carries its evidence and, crucially, its *falsification condition*. When you say "something feels off", the evidence gets read back line by line and only the broken one changes — the parts that were right survive.

**Three interactive panels.** Angle wall, resource scorer, shot board. Single-file HTML, works offline, no services.

## Install

```bash
git clone https://github.com/DaBai-abc/thought-bigbang.git ~/.workbuddy/skills/thought-bigbang
```

On Windows, clone into `%USERPROFILE%\.workbuddy\skills\thought-bigbang`. Pure Markdown plus one Python script — nothing to install.

## Contributing

The most valuable contributions are real cases you actually ran, new angle structures for `references/s2-angles.md`, and failure modes for `references/anti-patterns.md`. See [CONTRIBUTING.md](CONTRIBUTING.md).

Not welcome: making it generate more, faster, more automatically. The point of this project is slowing down enough to think.

## License

MIT.
