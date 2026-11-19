#!/usr/bin/env python3
"""思维大爆炸 —— 面板渲染器。

读项目目录下的 panel/data.json，注入单文件 HTML 模板，输出可离线打开的 panel.html。
不修改任何数据文件，只做渲染。

用法：
    python3 render_panel.py --project ~/内容工坊/20261119-foo
    python3 render_panel.py --project ~/内容工坊/20261119-foo --init   # 首次生成数据模板
    python3 render_panel.py --project ~/内容工坊/20261119-foo --open   # 渲染后直接打开
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL_DIR / "templates" / "panel.html"
DATA_TEMPLATE = SKILL_DIR / "assets" / "data-template.json"
PLACEHOLDER = "/*__PIPELINE_DATA__*/"

SCALES = [
    (12, 16, "完整制作", "可以做完整形态：实拍 + 剪辑 + 配音。"),
    (8, 11, "轻量口播", "单场景、单机位、口播或图文为主，靠文案质量取胜。"),
    (4, 7, "图文海报", "做图文、海报或纯文字。不要碰需要多镜头的视频。"),
    (0, 3, "纯文字验证", "先做一条纯文字发出去，验证有没有人看，别投入制作。"),
]


def fail(msg: str) -> None:
    print(f"[错误] {msg}", file=sys.stderr)
    sys.exit(1)


def scale_of(total: int) -> str:
    for lo, hi, name, _ in SCALES:
        if lo <= total <= hi:
            return name
    return "未评分"


def init_data(project_dir: Path) -> Path:
    panel_dir = project_dir / "panel"
    panel_dir.mkdir(parents=True, exist_ok=True)
    target = panel_dir / "data.json"
    if target.exists():
        print(f"[跳过] 数据文件已存在：{target}")
        return target
    if not DATA_TEMPLATE.exists():
        fail(f"找不到数据模板：{DATA_TEMPLATE}")
    target.write_text(DATA_TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"[创建] {target}")
    return target


def load_data(data_path: Path) -> dict:
    if not data_path.exists():
        fail(f"找不到数据文件：{data_path}\n先加 --init 生成模板。")
    try:
        raw = data_path.read_text(encoding="utf-8")
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        fail(f"data.json 格式错误，第 {e.lineno} 行第 {e.colno} 列：{e.msg}")
    if not isinstance(data, dict):
        fail("data.json 顶层必须是对象。")
    return data


def render(data: dict, out_path: Path) -> None:
    if not TEMPLATE.exists():
        fail(f"找不到模板：{TEMPLATE}")
    html = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in html:
        fail(f"模板缺少数据占位符 {PLACEHOLDER}")
    # ensure_ascii=False 保留中文；转义 </ 防止提前闭合 script 标签
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = html.replace(PLACEHOLDER, payload)
    verify(html, payload)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    size_kb = out_path.stat().st_size / 1024
    print(f"[渲染] {out_path}  ({size_kb:.1f} KB)")


def verify(html: str, payload: str) -> None:
    """渲染后自检，避免静默产出白屏。"""
    if PLACEHOLDER in html:
        fail("渲染后仍残留数据占位符，检查模板。")
    if "const DATA = " not in html:
        fail("模板缺少 const DATA = 声明。")
    tail = html.split("const DATA = ", 1)[1]
    if not tail.startswith(payload):
        fail("数据未成功注入模板。")
    after = tail[len(payload):len(payload) + 8].strip()
    if not after.startswith(";"):
        # 典型事故：占位符后面还留着兜底的 {} ，替换后变成相邻两个对象
        fail(f"占位符后存在多余字符 {after[:8]!r}，检查模板是否残留了 {{}}。")


def summarize(data: dict) -> None:
    proj = data.get("project", {})
    score = data.get("score", {})
    filled = [v for k, v in score.items() if k != "note" and isinstance(v, int)]
    total = sum(filled) if filled else 0
    angles = data.get("angles", [])
    shots = data.get("shots", [])
    done = sum(1 for s in shots if s.get("done"))

    print("")
    print(f"  项目    {proj.get('name') or '(未命名)'}")
    print(f"  阶段    {proj.get('stage') or 'S0'}")
    print(f"  方向    {len(angles)} 个")
    if filled:
        print(f"  评分    {total}/16  →  {scale_of(total)}   已填 {len(filled)}/8 项")
    else:
        print("  评分    未开始")
    print(f"  镜头    {done}/{len(shots)} 已就位")
    print("")


def main() -> None:
    ap = argparse.ArgumentParser(description="渲染思维大爆炸面板")
    ap.add_argument("--project", required=True, help="项目目录，如 ~/内容工坊/20261119-foo")
    ap.add_argument("--out", default=None, help="输出路径，默认 <项目目录>/panel.html")
    ap.add_argument("--init", action="store_true", help="数据文件不存在时按模板创建")
    ap.add_argument("--open", action="store_true", help="渲染后用默认浏览器打开")
    args = ap.parse_args()

    project_dir = Path(args.project).expanduser().resolve()
    if not project_dir.exists():
        if args.init:
            project_dir.mkdir(parents=True, exist_ok=True)
        else:
            fail(f"项目目录不存在：{project_dir}")

    data_path = project_dir / "panel" / "data.json"
    if args.init or not data_path.exists():
        init_data(project_dir)

    data = load_data(data_path)
    out_path = Path(args.out).expanduser() if args.out else project_dir / "panel.html"
    render(data, out_path)
    summarize(data)

    if args.open:
        subprocess.run(["open", str(out_path)], check=False)


if __name__ == "__main__":
    main()
