# DeutschGrammatikMeister — Deutsche Grammatikreferenz

Eine statische, deutschsprachige Referenzseite zur deutschen Grammatik (Fälle, Verbkonjugation, Adjektivdeklination, Satzbau u. v. m) mit einem vollständigen Regelkatalog von A1 bis C1 und interaktiven Übungen.

🇬🇧 English version: [README.md](README.md)

## Was es macht

- **Startseite:** Landingpage mit visuellem Hero (illustrierte Kasus-/Präsens-Karten), Suchfeld, Niveauschaltern (A1–C1) und Themenabschnitten (Nomen, Verben, Adjektive, Satzbau, …).
- **Niveauseiten (`a1.html` … `c1.html`):** 58 Grammatikregeln (11× A1, 12× A2, 13× B1, 12× B2, 10× C1) — jeweils mit deutscher Erklärung, Beispielen und einer Übung mit einblendbarer Lösung.
- **Glossar:** kurze Definitionen der auf der Seite verwendeten Grammatikbegriffe.
- **Ressourcen:** Links zu Deutsche Welle, dem Goethe-Institut und Canoonet.
- **Essay-Tutor-Anbindung:** `regeln.json` ist der maschinenlesbare Regelkatalog; der Essay Tutor übernimmt ihn, damit er gefundene Grammatikfehler direkt auf die passende Regel hier verlinken kann (Regel-IDs sind stabil — niemals umbenennen).

## Technik

Reines HTML und CSS, kein Framework. Die Niveauseiten und `regeln.json` werden von einem kleinen Python-Build-Skript erzeugt; der Suchindex wird mit Pagefind gebaut.

## Ausführen

Den Ordner mit einem beliebigen statischen Server bereitstellen:

```bash
npx serve .
```

## Build

Die Niveauseiten entstehen aus den Regel-Daten — `a1.html` … `c1.html` nicht von Hand bearbeiten:

```bash
python3 tools/build.py && npx pagefind --site . --glob "*.html" --output-path pagefind
```

`regeln/a1.json … c1.json` enthalten die 58 Grammatikregeln (deutsche Erklärungen, Beispiele, Übungen mit Lösungen). `tools/build.py` erzeugt `a1.html … c1.html` und `regeln.json` (Regelkatalog mit stabilen IDs, auf die der Essay Tutor verlinkt). Regel-IDs niemals umbenennen; stattdessen neue Regeln hinzufügen. Danach den Suchindex neu bauen. Die Erklärungen sind KI-entwürfe und sollten von einer Deutschlehrkraft geprüft werden.

## Suche

Das Suchfeld nutzt [Pagefind](https://pagefind.app) (statischer Index, kein Server). Nach Änderungen an einer HTML-Seite den Build-Befehl oben erneut ausführen und den Ordner `pagefind/` mitcommitten.

## Gestaltung

Die Seite wurde visuell überarbeitet: Karten-Layout mit Niveau-Akzentfarben (A1 grün, A2 cyan, B1 blau, B2 violett, C1 pink), illustrierte Hero-Grafiken als Inline-SVG/CSS und ein responsives Layout, das von ~360-px-Handys bis hin zu breiten Desktops funktioniert. Die Niveauseiten haben am Desktop eine sticky Inhaltsverzeichnis-Spalte, die auf mobilen Geräten zu einem horizontalen Scroller wird.

## Hinweise

Die ursprüngliche Quelle war eine türkischsprachige Landingpage mit drei Teaser-Karten, die alle auf `#` verlinkten — ohne echten Grammatikinhalt und mit toten Nav-Links. Vor der Veröffentlichung wurde sie zu einer deutschen Grammatikreferenz mit echten Regeln, Glossar und Ressourcen-Abschnitt umgeschrieben. Ein ungenutztes, 3,2 MB grosses Foto einer Deutsch-Lehrbuchseite (urheberrechtlich geschützt, im Code nirgends referenziert) wurde ausgeschlossen.
