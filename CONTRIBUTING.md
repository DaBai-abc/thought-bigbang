# 贡献指南

这个项目最需要的东西不是代码，是**跑过之后留下的痕迹**。

## 最欢迎的三类

### 1. 真实案例

你用它做完一条内容，把过程里卡住的地方写下来：

- 哪个阶段卡住了，卡在什么地方
- 你当时怎么绕过去的
- 回头看，手册里哪句话让你走了弯路

开一条 issue，标签用 `case`。这类反馈比任何抽象建议都有用——因为这套流程的价值只在真实使用里才能验证。

### 2. 角度类型

`references/s2-angles.md` 现在收录了七种角度结构：反常识、私密自述、工具实用、冲突对立、时间线、拆解、对照实验。

七种不够。你见过某种切口很有效但没被收录，按同样的格式补进去，并说明它适合什么起点类型。

### 3. 失败模式

`references/anti-patterns.md` 现在 22 条，每条含识别信号和修正动作。

你踩过的坑最有价值。补的时候注意：**识别信号要具体**。"内容不够吸引人"是废话，"开头出现『今天想跟大家聊聊』"才是信号。

## 不太欢迎的

- 让它生成得更多、更快、更自动
- 把闸门改成可选，或者加一个「一键全自动」开关
- 增加依赖（目前零依赖，这是特性不是缺陷）

这个项目的价值恰恰在"慢下来想清楚"。想清楚这一点再提 PR。

## 流程

```bash
# 1. 先自检，确保没破坏结构
python3 scripts/validate.py

# 2. 改完再跑一遍，然后提 PR
```

- Fork → 开分支 → 改 → PR
- 一次 PR 只做一件事
- 改了 `SKILL.md` 的行为规则，在 PR 描述里说清为什么
- 新增的 reference 文件必须在 `SKILL.md` 的资源清单里登记

## 提 PR 前的检查

```bash
python3 scripts/validate.py
```

它会检查：frontmatter 必需字段、`name` 与目录名一致、所有引用路径存在、JSON 模板可解析、面板模板占位符完整。

CI 会跑同样的检查，本地过了通常就能过。

## 翻译

`SKILL.md` 正文目前是中文。英文版需要有人做——但不是逐句翻译，是按英语创作者的表达习惯重写。这个工作量大，先在 issue 里认领再动手，避免几个人重复做。

---

# Contributing

The most valuable contribution is not code — it's **the trace of having actually run it**.

- **Real cases**: open an issue labeled `case`. Where you got stuck, how you got around it, which line in the playbook sent you down a wrong path.
- **Angle structures**: `references/s2-angles.md` lists seven. Add the ones you've seen work, in the same format, noting which spark type they suit.
- **Failure modes**: `references/anti-patterns.md` has 22. Signals must be concrete — "the content isn't engaging" is useless, "the opening is 'so today I want to talk about'" is a signal.

Not welcome: making it generate more, faster, or more automatically. Zero dependencies is a feature.

Run `python3 scripts/validate.py` before opening a PR. CI runs the same check.
