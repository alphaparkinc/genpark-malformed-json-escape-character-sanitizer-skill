# genpark-malformed-json-escape-character-sanitizer-skill

Resilient JSON payload cleaner repairing single quotes, markdown backticks, trailing commas, and unescaped characters.

## Architecture

```mermaid
flowchart LR
    Raw["Malformed Raw Model Output: {'cmd': 'ls',}"] --> Cleaner[Regex Cleaner & Syntax Sanitizer]
    Cleaner --> ValidJSON["Valid JSON: {"cmd": "ls"}"]
```

## Features
- **Zero External Parsers**: 100% Python Standard Library.
- **Markdown Stripping**: Strips triple-backtick wrappers.
