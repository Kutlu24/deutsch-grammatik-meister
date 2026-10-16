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
SITE_URL = "https://german-trainer-platform.onrender.com/grammatik/"
ESSAY_TUTOR_URL = "https://my-essay-tutor.onrender.com/ui/"  # live on Render

HEADER = """    <header class="site-header">
        <div class="container">
            <a class="brand" href="index.html">
                <span class="brand-mark" aria-hidden="true">G</span>
                <span class="brand-text">DeutschGrammatikMeister<small>Grammatik · A1–C1</small></span>
            </a>
            <nav class="site-nav" aria-label="Hauptnavigation">
                <ul>
                    <li><a href="index.html">Startseite</a></li>
{levels}
                </ul>
            </nav>
        </div>
    </header>"""

FOOTER = """    <footer class="site-footer">
        <div class="container">
            <div class="cols">
                <div>
                    <a class="brand" href="index.html">
                        <span class="brand-mark" aria-hidden="true">G</span>
                        <span class="brand-text">DeutschGrammatikMeister<small>Grammatik · A1–C1</small></span>
                    </a>
                    <p>Visuelle Grammatik-Referenz für Deutschlernende — 58 Regeln mit Erklärung, Beispielen und Übungen samt Lösung.</p>
                </div>
                <div>
                    <h4>Niveaustufen</h4>
                    <ul>
{level_links}
                    </ul>
                </div>
                <div>
                    <h4>Projekt</h4>
                    <ul>
                        <li><a href="{essay}">Essay Tutor</a></li>
                        <li><a href="index.html#glossar">Glossar</a></li>
                        <li><a href="index.html#ressourcen">Ressourcen</a></li>
                    </ul>
                </div>
            </div>
            <div class="bottom">
                <span>© DeutschGrammatikMeister · <a href="index.html">Startseite</a></span>
                <span>58 Regeln · A1 bis C1</span>
            </div>
        </div>
    </footer>"""

LEVEL_TITLES = {
    "a1": "A1 — Erste Schritte",
    "a2": "A2 — Alltag &amp; Vergangenheit",
    "b1": "B1 — Selbstständig kommunizieren",
    "b2": "B2 — Differenziert und genau",
    "c1": "C1 — Souverän und stilsicher",
}


def md(text: str) -> str:
    """Escape, then allow **bold** and *italic* only."""
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)


def rule_html(r: dict, n: int) -> str:
    ex = "".join(f"<li>{md(e)}</li>\n" for e in r["examples"])
    paras = "".join(f"<p>{md(p)}</p>\n" for p in r["explain"])
    rows = "".join(
        f'<li><span class="q">{md(e["q"])}</span> <details><summary>Lösung</summary>'
        f'<span class="a">{md(e["a"])}</span></details></li>\n' for e in r["exercises"])
    return (
        f'<article class="rule" id="{r["id"]}">\n'
        f'<h3>{md(r["title"])}</h3>\n'
        f'{paras}'
        f'<p class="label">Beispiele</p>\n<ul class="examples">{ex}</ul>\n'
        f'<p class="label">Übung · {len(r["exercises"])} Aufgabe'
        f'{"n" if len(r["exercises"]) != 1 else ""}</p>\n<ol class="exercises">{rows}</ol>\n'
        f'<p class="ruleid">Regel-ID <code>{r["id"]}</code> · Regel {n}</p>\n'
        f'</article>'
    )


def page(data: dict, current: str) -> str:
    level = data["level"].upper()
    rules = data["rules"]
    n_rules = len(rules)

    nav_levels = "\n".join(
        f'                    <li><a href="{l}.html"{("", " aria-current=\"page\"")[l == current]}>{l.upper()}</a></li>'
        for l in LEVELS)
    header = HEADER.format(levels=nav_levels)

    toc_rail = "\n".join(
        f'                        <li><a href="#{r["id"]}">{md(r["title"])}</a></li>' for r in rules)
    body = "\n".join(rule_html(r, i + 1) for i, r in enumerate(rules))
    level_links = "\n".join(
        f'                        <li><a href="{l}.html">{LEVEL_TITLES[l]}</a></li>' for l in LEVELS)
    footer = FOOTER.format(level_links=level_links, essay=ESSAY_TUTOR_URL)

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
{header}

    <main>
        <section class="level-hero" data-level="{level}" style="--level: var(--{current})">
            <div class="container">
                <span class="chip">Niveaustufe {level}</span>
                <h1>{html.escape(data["title"])}</h1>
                <p>{html.escape(data["intro"])}</p>
                <div class="meta">
                    <span>{n_rules} Regeln</span>
                    <span>Übungen mit Lösung</span>
                    <span>A1 → C1</span>
                </div>
            </div>
        </section>

        <div class="container">
            <div class="level-layout" style="--level: var(--{current}); --level-soft: color-mix(in srgb, var(--{current}) 12%, #fff)">
                <aside class="toc-rail" data-pagefind-ignore>
                    <div class="rail-title">Inhalt · {n_rules} Regeln</div>
                    <ol>
{toc_rail}
                    </ol>
                </aside>
                <div class="rules">
{body}
                    <p class="hint info" style="margin-top:6px">Schreibst du Texte? Lass sie im <a href="{ESSAY_TUTOR_URL}">Essay Tutor</a> prüfen. Bei jedem Fehler verweist er auf die passende Regel hier.</p>
                    <a class="level-back" href="index.html">← Zurück zur Startseite</a>
                </div>
            </div>
        </div>
    </main>

{footer}
</body>
</html>
'''


def main() -> None:
    data = {l: json.loads((ROOT / "regeln" / f"{l}.json").read_text(encoding="utf-8")) for l in LEVELS}
    ids = [r["id"] for d in data.values() for r in d["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule id"
    catalog = []
    for l, d in data.items():
        (ROOT / f"{l}.html").write_text(page(d, l), encoding="utf-8")
        for r in d["rules"]:
            catalog.append({"id": r["id"], "level": d["level"], "title": r["title"], "url": f"{l}.html#{r['id']}"})
    (ROOT / "regeln.json").write_text(
        json.dumps({"site_url": SITE_URL, "rules": catalog}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(ids)} rules, {len(LEVELS)} pages")


if __name__ == "__main__":
    main()
