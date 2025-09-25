# Search Agent

Ein intelligenter AI-Assistant, der Web-Suchen durchführt und Fragen mit aktuellen Informationen beantwortet.

## Übersicht

Der Search Agent ist ein conversational AI-Agent, der die DuckDuckGo-Suchmaschine nutzt, um aktuelle Informationen aus dem Web zu finden und Benutzerfragen zu beantworten. Er kombiniert die Leistungsfähigkeit von Amazon Bedrock's Claude Sonnet 4 mit Web-Suche-Funktionalitäten.

## Features

- 🔍 **Web-Suche**: Durchsucht das Web nach aktuellen Informationen
- 🌍 **Multi-Region Support**: Unterstützt verschiedene Suchregionen (us-en, uk-en, ru-ru, etc.)
- 🎯 **Flexible Ergebnisse**: Konfigurierbare maximale Anzahl von Suchergebnissen
- 🤖 **KI-gestützte Antworten**: Nutzt Claude Sonnet 4 für intelligente Antworten
- 💬 **Interaktive Konsole**: Einfache Chat-Oberfläche für Benutzerinteraktionen
- ⚡ **Fehlerbehandlung**: Robuste Behandlung von Rate-Limits und Exceptions

## Voraussetzungen

- Python 3.8+
- AWS-Berechtigung für Amazon Bedrock
- Internetzugang für Web-Suchen

## Installation

1. **Repository klonen und in das Verzeichnis wechseln:**
   ```bash
   cd search-agent
   ```

2. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **AWS-Konfiguration:**
   Stellen Sie sicher, dass Ihre AWS-Credentials konfiguriert sind, um auf Amazon Bedrock zugreifen zu können:
   ```bash
   aws configure
   ```

## Verwendung

### Interaktiver Modus

Den Agent im interaktiven Modus starten:

```bash
python search_agent.py
```

Dann können Sie Fragen stellen wie:
- "Was sind die neuesten Nachrichten über KI?"
- "Wie ist das Wetter heute in Berlin?"
- "Erkläre mir die aktuellen Entwicklungen bei OpenAI"

### Programmatische Verwendung

```python
from search_agent import search_agent

# Frage stellen
response = search_agent("Was ist die aktuelle Version von Python?")
print(response)
```

### Web-Suche Tool direkt verwenden

```python
from search_agent import websearch

# Direkte Web-Suche
results = websearch(
    keywords="Python 3.13 release date",
    region="us-en",
    max_results=5
)
print(results)
```

## Konfiguration

### Suchregionen

Der Agent unterstützt verschiedene Suchregionen:
- `wt-wt`: Weltweit
- `us-en`: USA (Englisch)
- `uk-en`: Vereinigtes Königreich (Englisch)
- `de-de`: Deutschland (Deutsch)
- `ru-ru`: Russland (Russisch)

### Modell-Konfiguration

Das verwendete Bedrock-Modell kann angepasst werden:

```python
from strands.models import BedrockModel

custom_model = BedrockModel(
    model_id="eu.anthropic.claude-sonnet-4-20250514-v1:0"
)
```

## API-Referenz

### websearch()

Führt eine Web-Suche durch und gibt die Ergebnisse zurück.

**Parameter:**
- `keywords` (str): Suchbegriffe
- `region` (str, optional): Suchregion (Standard: "us-en")
- `max_results` (int, optional): Maximum Anzahl der Ergebnisse

**Rückgabe:**
- Liste von Dictionaries mit Suchergebnissen oder Fehlermeldung

**Beispiel:**
```python
results = websearch("Machine Learning trends 2024", region="us-en", max_results=10)
```

## Fehlerbehandlung

Der Agent behandelt verschiedene Fehlertypen:

- **RatelimitException**: Tritt auf, wenn zu viele Anfragen gestellt werden
- **DDGSException**: Allgemeine DuckDuckGo-Suchfehler
- **Exception**: Andere unerwartete Fehler

## Abhängigkeiten

- `strands-agents`: Framework für AI-Agenten
- `strands-agents-tools`: Zusätzliche Tools für Agenten
- `ddgs`: DuckDuckGo-Suchbibliothek

## Lizenz

Siehe LICENSE-Datei für Details.

## Mitwirken

Beiträge sind willkommen! Bitte erstellen Sie Issues oder Pull Requests für Verbesserungen.

## Support

Bei Problemen oder Fragen erstellen Sie bitte ein Issue im Repository.