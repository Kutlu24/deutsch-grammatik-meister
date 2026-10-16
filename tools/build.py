#!/usr/bin/env python3
"""Builds the level pages (a1.html ... c1.html) and regeln.json from regeln/*.json.

    python3 tools/build.py && npx pagefind --site . --glob "*.html" --output-path pagefind

regeln.json is the machine-readable rule catalog; the Essay Tutor copies it so that a detected
grammar error can link to the matching rule here (rule ids are stable, never rename them)."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["a1", "a2", "b1", "b2", "c1"]
SITE_URL = "https://kutlu24.github.io/deutsch-grammatik-meister/"
ESSAY_TUTOR_URL = "https://my-essay-tutor.onrender.com/"  # change if the Essay Tutor lives elsewhere


def md(text: str) -> str:
    """Escape, then allow **bold** and *italic* only."""
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)


def rule_html(r: dict) -> str:
    ex = "".join(f"<li>{md(e)}</li>" for e in r["examples"])
    paras = "".join(f"<p>{md(p)}</p>" for p in r["explain"])
    rows = "".join(
        f'<li><span class="q">{md(e["q"])}</span> <details><summary>Lösung</summary>'
        f'<span class="a">{md(e["a"])}</span></details></li>' for e in r["exercises"])
    return (f'<article class="rule" id="{r["id"]}">\n<h3 id="h-{r["id"]}">{md(r["title"])}</h3>\n{paras}\n'
            f'<p class="label">Beispiele</p><ul class="examples">{ex}</ul>\n'
            f'<p class="label">Übung</p><ol class="exercises">{rows}</ol>\n'
            f'<p class="ruleid">Regel-ID: <code>{r["id"]}</code></p>\n</article>')


def page(data: dict, nav: str) -> str:
    level = data["level"]
    toc = "".join(f'<li><a href="#{r["id"]}">{md(r["title"])}</a></li>' for r in data["rules"])
    body = "\n".join(rule_html(r) for r in data["rules"])
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(data["title"])} — DeutschGrammatikMeister</title>
    <meta name="description" content="{html.escape(data["intro"])}">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1><a href="index.html" style="color:inherit;text-decoration:none">DeutschGrammatikMeister</a></h1>
            <nav><ul>{nav}</ul></nav>
        </div>
    </header>
    <main>
        <section class="detail">
            <div class="container">
                <h2 id="h-{level.lower()}">{html.escape(data["title"])}</h2>
                <p>{html.escape(data["intro"])}</p>
                <ul class="toc">{toc}</ul>
                <p class="hint">Schreibst du Texte? Lass sie im <a href="{ESSAY_TUTOR_URL}">Essay Tutor</a> prüfen. Bei jedem Fehler verweist er auf die passende Regel hier.</p>
            </div>
        </section>
        <section class="detail rules">
            <div class="container">
{body}
            </div>
        </section>
    </main>
    <footer><div class="container"><p>&copy; DeutschGrammatikMeister · <a href="index.html" style="color:#fff">Startseite</a></p></div></footer>
</body>
</html>
'''


def main() -> None:
    data = {l: json.loads((ROOT / "regeln" / f"{l}.json").read_text(encoding="utf-8")) for l in LEVELS}
    ids = [r["id"] for d in data.values() for r in d["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule id"
    nav = "".join(f'<li><a href="{l}.html">{l.upper()}</a></li>' for l in LEVELS)
    catalog = []
    for l, d in data.items():
        (ROOT / f"{l}.html").write_text(page(d, nav), encoding="utf-8")
        for r in d["rules"]:
            catalog.append({"id": r["id"], "level": d["level"], "title": r["title"], "url": f"{l}.html#{r['id']}"})
    (ROOT / "regeln.json").write_text(
        json.dumps({"site_url": SITE_URL, "rules": catalog}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(ids)} rules, {len(LEVELS)} pages")


if __name__ == "__main__":
    main()
