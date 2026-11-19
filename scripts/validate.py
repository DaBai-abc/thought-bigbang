#!/usr/bin/env python3
"""思维大爆炸 —— 独立结构校验器。

不依赖 WorkBuddy，任何装了 python3 的机器都能跑，供贡献者本地自查和 CI 使用。

用法：
    python3 scripts/validate.py
    python3 scripts/validate.py --verbose

退出码：0 全部通过（可能有警告），1 有错误。
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["name", "description"]
RECOMMENDED = ["display_name", "display_name_en", "description_zh", "description_en"]

errors = []
warns = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warns.append(msg)


def read_frontmatter():
    path = ROOT / "SKILL.md"
    if not path.exists():
        err("缺少 SKILL.md")
        return None, None
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        err("SKILL.md 开头缺少 YAML frontmatter")
        return None, text
    return m.group(1), text


def field(block, key):
    m = re.search(rf"^{re.escape(key)}:\s*(.+)$", block, re.M)
    return m.group(1).strip() if m else None


def check_frontmatter(block):
    if block is None:
        return
    values = {}
    for key in REQUIRED:
        val = field(block, key)
        values[key] = val
        if not val:
            err(f"frontmatter 缺少必需字段 {key}")
    for key in RECOMMENDED:
        val = field(block, key)
        values[key] = val
        if not val:
            warn(f"建议补充字段 {key}（用于中英文展示）")

    name = values.get("name")
    if name:
        if not re.match(r"^[a-z0-9-]+$", name):
            err(f"name '{name}' 必须是 hyphen-case：小写字母、数字、连字符")
        elif name.startswith("-") or name.endswith("-") or "--" in name:
            err(f"name '{name}' 不能以连字符开头/结尾，也不能有连续连字符")
        elif name != ROOT.name:
            err(f"name '{name}' 与目录名 '{ROOT.name}' 不一致")

    desc = values.get("description") or ""
    if desc and len(desc) < 30:
        warn(f"description 只有 {len(desc)} 字，太少，模型可能判断不出何时该用")

    ver = field(block, "version")
    if not ver:
        warn("建议加 version 字段，便于使用者判断是否需要更新")
    return values


def check_references(text):
    if not text:
        return
    refs = set(re.findall(r"`((?:references|assets|scripts|templates)/[A-Za-z0-9_.\-]+)`", text))
    if not refs:
        warn("SKILL.md 里没有引用任何资源文件")
    for ref in sorted(refs):
        if not (ROOT / ref).exists():
            err(f"SKILL.md 引用了不存在的文件：{ref}")
    return refs


def check_json_template():
    path = ROOT / "assets" / "data-template.json"
    if not path.exists():
        warn("缺少 assets/data-template.json，面板无法初始化")
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"data-template.json 格式错误：第 {e.lineno} 行 {e.msg}")
        return
    for key in ("project", "angles", "score", "shots"):
        if key not in data:
            err(f"data-template.json 缺少顶层字段 {key}")
    if not isinstance(data.get("angles"), list):
        err("data-template.json 的 angles 必须是数组")
    if not isinstance(data.get("shots"), list):
        err("data-template.json 的 shots 必须是数组")


def check_panel_template():
    path = ROOT / "templates" / "panel.html"
    if not path.exists():
        warn("缺少 templates/panel.html，面板无法渲染")
        return
    html = path.read_text(encoding="utf-8")
    if "/*__PIPELINE_DATA__*/" not in html:
        err("panel.html 缺少数据占位符 /*__PIPELINE_DATA__*/")
    if "const DATA = " not in html:
        err("panel.html 缺少 const DATA = 声明")
    # 占位符后紧跟 ; 才对。若写成 /*占位*/ {}; 替换后会变成相邻两个对象
    m = re.search(r"const DATA = /\*__PIPELINE_DATA__\*/([^\n]{0,10})", html)
    if m and not m.group(1).lstrip().startswith(";"):
        err("panel.html 占位符后有多余字符，替换后会导致 JS 语法错误"
            "（写 const DATA = /*__PIPELINE_DATA__*/; 即可）")
    external = re.findall(r'(?:src|href)="https?://', html)
    if external:
        warn(f"panel.html 含 {len(external)} 个外部链接，离线打开会失效")


def check_markdown_dir():
    ref_dir = ROOT / "references"
    if not ref_dir.exists():
        warn("缺少 references 目录")
        return
    for md in sorted(ref_dir.glob("*.md")):
        txt = md.read_text(encoding="utf-8").strip()
        if len(txt) < 200:
            warn(f"{md.relative_to(ROOT)} 内容过短（{len(txt)} 字符），可能只是占位")


def check_render_script():
    path = ROOT / "scripts" / "render_panel.py"
    if not path.exists():
        warn("缺少 scripts/render_panel.py，面板无法生成")
        return
    src = path.read_text(encoding="utf-8")
    if "def verify" not in src:
        warn("render_panel.py 缺少渲染后自检，可能静默产出白屏")


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    block, text = read_frontmatter()
    values = check_frontmatter(block)
    check_references(text)
    check_json_template()
    check_panel_template()
    check_markdown_dir()
    check_render_script()

    print("")
    print(f"  校验目录  {ROOT}")
    if values:
        print(f"  名称      {values.get('display_name') or '—'} / {values.get('display_name_en') or '—'}")
        print(f"  slug      {values.get('name')}")

    if warns:
        print("")
        print(f"  警告 {len(warns)} 项")
        for w in warns:
            print(f"    · {w}")

    if errors:
        print("")
        print(f"  错误 {len(errors)} 项")
        for e in errors:
            print(f"    ✗ {e}")
        print("")
        print("  校验未通过。")
        return 1

    print("")
    print("  ✓ 全部通过")
    print("")
    return 0


if __name__ == "__main__":
    sys.exit(main())
