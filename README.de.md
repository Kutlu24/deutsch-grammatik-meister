# DeutschGrammatikMeister — Deutsche Grammatikreferenz

Eine statische, türkischsprachige Referenzseite, die türkischsprachigen Deutschlernenden die Kerngrammatik erklärt (Substantive/Fälle, Verbkonjugation, Adjektivdeklination).

🇬🇧 English version: [README.md](README.md)

## Was es macht

- **Nomen:** die vier deutschen Fälle (Nominativ/Akkusativ/Dativ/Genitiv) mit vollständiger der/die/das-Deklinationstabelle.
- **Verben:** Präsens-Konjugationsmuster für regelmässige Verben, plus häufige Verben mit Stammvokalwechsel.
- **Adjektive:** Adjektivendungen nach bestimmtem Artikel sowie Steigerung (Positiv/Komparativ/Superlativ).
- **Übungen:** Links zu zwei funktionierenden Vokabeltrainer-Apps auf diesem Account ([Aspekte Neu C1 Wortschatz](https://github.com/Kutlu24/Aspekte-Neu-C1-Wortschatz), [Sicher! B2 Vokabeltrainer](https://github.com/Kutlu24/HEY-Bist-Du-Sicher-B2)) statt einer vorgetäuschten Übungs-Engine.
- **Glossar:** kurze Definitionen der auf der Seite verwendeten Grammatikbegriffe.
- **Ressourcen:** Links zu Deutsche Welle, dem Goethe-Institut und Canoonet.

## Technik

Reines HTML und CSS, kein Framework, kein Build-Prozess.

## Ausführen

`index.html` im Browser öffnen, oder den Ordner mit einem beliebigen statischen Server bereitstellen:

```bash
npx serve .
```

## Hinweise

Die ursprüngliche Quelle war eine einzelne Landingpage mit drei Teaser-Karten, die alle auf `#` verlinkten — ohne echten Grammatikinhalt dahinter, und mit toten Nav-Links. Vor der Veröffentlichung wurden echte Grammatik-Referenzabschnitte (mit Deklinations-/Konjugationstabellen), ein Glossar und ein Ressourcen-Abschnitt verfasst. Ein ungenutztes, 3,2 MB grosses Foto einer Deutsch-Lehrbuchseite (urheberrechtlich geschütztes Material, im Code nirgends referenziert) wurde ausgeschlossen.
