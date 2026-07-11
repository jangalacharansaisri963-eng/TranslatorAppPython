# 🌌 Quantum Terminal Console & Travel Suite

A single, unified desktop terminal application built with Python and CustomTkinter. This application acts as an all-in-one console combining **low-level digital data encoders/decoders** with a **live cloud natural language translation suite** optimized for regional travel in India.

---

## 🚀 Key Features

* **Unified Single Window:** No more bouncing between 9 different app windows. One console runs every instruction.
* **Travel-Ready Matrix:** Supports natural language translations into **Hindi, Telugu, Tamil, Spanish, French, and German**.
* **Automatic Reverse Decoding:** Paste binary, hex, octal, ASCII codes, or Base64 into the terminal followed by `(func translate to english)`, and the engine automatically detects the format and decodes it back to plain text.
* **Safe Foreign Pipeline:** Special encoding rules intercept multi-byte characters (like Hindi or Telugu script) and route them through an English correction pipeline before binary/hex processing to completely prevent data corruption or rendering crashes.
* **Global CLI Operations:** Built-in console tools like `clear` / `cls` and an internal clipboard cache hook via `(func copy)`.

---

## 🛠️ Syntax Matrix Reference

To execute a routine, simply type your string followed by the respective instruction flag inside the entry box:

### 📡 Digital Encoders & Hashes
* **Text -> Binary String:** `Hello World (func translate to binary)`
* **Text -> Hexadecimal Notation:** `Quantum Core (func translate to hex)`
* **Text -> Octal Representation:** `System Boot (func translate to octal)`
* **Text -> Raw ASCII Matrices:** `Admin (func translate to ascii)`
* **Text -> Base64 Encoding Block:** `Secure Stream (func translate to base64)`

### 🌍 Global Translation Suite
* **Any Language -> Hindi Script:** `Good morning my friend (func translate to hindi)`
* **Any Language -> Telugu Script:** `Where is the train station? (func translate to telugu)`
* **Any Language -> Tamil Script:** `Thank you for the delicious food (func translate to tamil)`
* **Any Language -> Spanish:** `Welcome home (func translate to spanish)`
* **Any Language -> French:** `Goodbye (func translate to french)`
* **Any Language -> German:** `Emergency exit (func translate to german)`

### 🔄 Dynamic Reverse Routing & Clipboard
* **Any Cipher/Script -> English:** `01001000 01101001 (func translate to english)`
* **Any Cipher/Script -> English:** `नमस्ते (func translate to english)`
* **Clipboard Hook:** `(func copy)` *(Copies the last processed output directly into your OS clipboard)*
* **Flush Screen Log:** `clear` or `cls`

---

## 📂 Codebase Architecture

The project repository relies on exactly three tightly decoupled core Python scripts alongside the build engine:

```text
📁 Project-Repository
 ├── 📁 .github/workflows/
 │    └── 📄 build-exe.yml          # Automated CI/CD PyInstaller compiler pipeline
 ├── 📄 base_terminal.py            # CustomTkinter frame layout, styles, & canvas engine
 ├── 📄 main_terminal_app.py        # Master regex routing controller & command scanner
 └── 📄 encoders.py                 # Heavy-lifting mathematical bit-shifters & cloud APIs



📦 Compilation & Local Deployment
The repository comes integrated with a GitHub Actions CI/CD automation matrix.
Commit changes to the main branch.
The .github/workflows/build-exe.yml pipeline triggers immediately inside a native windows-latest virtual machine.
Dependencies (customtkinter, deep-translator, pyinstaller) are pulled dynamically.
PyInstaller packs the 3 files down into a single, standalone .exe bundle using --onefile compression.
Download your zipped .exe asset straight from the Actions / Artifacts



Email at jangalacharansaisri963@gmail.com for app ideas, updates and downloads.
