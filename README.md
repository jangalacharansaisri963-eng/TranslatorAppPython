# Translator v3.0

A lightweight, high-performance command-line interface (CLI) terminal engineered for instant text translation, cryptographic payload encoding, and numeric base conversions. 

## Features

- **Robust Language Translation**: Seamlessly translates text payloads into 33 global languages via the Google Translation core.
- **Advanced Low-Level Encoders**: Instantly converts plain text strings to and from Binary, Hexadecimal, Octal, ASCII decimals, and Base64 structures.
- **Fail-Safe Clipboard Subsystem**: Integrated macro hooks safely manage `copy` and `paste` commands, automatically preventing system crashes on environments lacking a native clipboard engine (such as Pydroid 3).
- **Automated Compilation CI/CD**: Packaged with a customized GitHub Actions workflow orchestration (`.github/workflows/build.yml`) to cleanly build cross-compiled Windows static binaries using automated headless PyInstaller runs.

## Supported Operations

### Multi-Language Targets
`ENGLISH`, `SPANISH`, `FRENCH`, `GERMAN`, `ITALIAN`, `PORTUGUESE`, `DUTCH`, `SWEDISH`, `NORWEGIAN`, `DANISH`, `FINNISH`, `POLISH`, `CZECH`, `SLOVAK`, `ROMANIAN`, `HUNGARIAN`, `CROATIAN`, `SLOVENIAN`, `ALBANIAN`, `ESTONIAN`, `LATVIAN`, `LITHUANIAN`, `TURKISH`, `INDONESIAN`, `MALAY`, `FILIPINO`, `VIETNAMESE`, `IRISH`, `WELSH`, `AFRIKAANS`, `SWAHILI`, `LATIN`.

### Low-Level Encoders
- `BINARY` (8-bit binary strings)
- `HEX` (Base-16 capitalized pairs)
- `OCTAL` (Base-8 notation layout)
- `ASCII` (Raw ordinal numerical representations)
- `BASE64` (Standard UTF-8 Base64 byte-to-text array strings)

## Project Architecture & Dependencies

```text
├── translator.py          # Main application loop engine
├── requirements.txt       # Global third-party module declarations
└── .github/
    └── workflows/
        └── build.yml      # Headless Windows automated builder setup
```

The tool leverages the following core external requirements:
* `pyperclip` (Cross-platform clipboard architecture interface)
* `deep-translator` (Highly reliable API endpoint engine)

## Installation & Environment Setup

1. **Clone the Source Tree**:
   ```bash
   git clone https://github.com
   cd translator
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Boot the Console Application**:
   ```bash
   python translator.py
   ```

## Runtime Syntax Guide

All functional operations are executed using a specific regular-expression-mapped macro hook:
```text
[Your alphanumeric payload string here] (func translate to [target_language_or_encoder])
```

### Practical Shell Examples

* **Language Translation Execution**:
  ```text
  core@quantum_matrix:~$ Hello code environment (func translate to french)
  >> OUTPUT (FRENCH): Bonjour l'environnement de code
  ```

* **Binary Byte Serialization**:
  ```text
  core@quantum_matrix:~$ SECURE (func translate to binary)
  >> OUTPUT (BINARY): 01010011 01000101 01000011 01010101 01010010 01000101
  ```

* **Cryptographic Base64 Packing**:
  ```text
  core@quantum_matrix:~\$ AdminAccess! (func translate to base64)
  >> OUTPUT (BASE64): QWRtaW5BY2Nlc3Mh
  ```

### Terminal Management Utilities
* `(func copy)` - Securely copies the last successful terminal buffer payload directly to your system workspace clipboard.
* `(func paste)` - Pulls text out of your global clipboard and safely echoes it into the app window.
* `clear` - Wipes the operational visibility of the script frame for a clean workspace.
* `exit` or `quit` - Cleanly breaks the session interface loop.
* 
