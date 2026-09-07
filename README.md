# DeutschGrammatikMeister — German Grammar Reference

A static, Turkish-language reference site explaining core German grammar topics (nouns/cases, verb conjugation, adjective declension) to Turkish speakers learning German.

🇩🇪 German version: [README.de.md](README.de.md)

## What it does

- **Nomen (Nouns):** the four German cases (Nominativ/Akkusativ/Dativ/Genitiv) with a full der/die/das declension table.
- **Verben (Verbs):** present-tense conjugation pattern for regular verbs, plus common stem-vowel-change irregulars.
- **Adjektive (Adjectives):** adjective-ending pattern after a definite article, and comparison (positive/comparative/superlative).
- **Übungen (Exercises):** links out to two working vocabulary-practice apps published on this account ([Aspekte Neu C1 Wortschatz](https://github.com/Kutlu24/Aspekte-Neu-C1-Wortschatz), [Sicher! B2 Vokabeltrainer](https://github.com/Kutlu24/HEY-Bist-Du-Sicher-B2)) rather than a fake exercise engine.
- **Glossar:** short definitions of the grammar terms used on the page.
- **Ressourcen:** links to Deutsche Welle, the Goethe-Institut, and Canoonet.

## Tech stack

Plain HTML and CSS, no framework, no build step.

## Running it

Open `index.html` in a browser, or serve the folder with any static file server:

```bash
npx serve .
```

## Notes

The original source was a single landing page with three teaser cards, all linking to `#` — no actual grammar content behind them, and all nav links dead. Real grammar reference sections (with declension/conjugation tables), a glossary, and a resources section were written before publishing. An unused 3.2 MB photo of a German textbook page (copyrighted material, not referenced anywhere in the code) was excluded.
