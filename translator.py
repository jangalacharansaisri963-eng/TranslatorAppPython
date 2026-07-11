import base64
import re
import requests

# ==================================================
# MICROSOFT TRANSLATOR CONFIGURATION
# ==================================================

API_KEY = "YOUR_MICROSOFT_TRANSLATOR_KEY"
REGION = "YOUR_RESOURCE_REGION"      # Example: eastus
ENDPOINT = "https://api.cognitive.microsofttranslator.com"

# ==================================================
# SUPPORTED LANGUAGES
# ==================================================

LANGS = {
    "english": "en",
    "hindi": "hi",
    "telugu": "te",
    "tamil": "ta",
    "kannada": "kn",
    "malayalam": "ml",
    "marathi": "mr",
    "gujarati": "gu",
    "bengali": "bn",
    "punjabi": "pa",
    "urdu": "ur",
    "spanish": "es",
    "french": "fr",
    "german": "de",
    "italian": "it",
    "portuguese": "pt",
    "japanese": "ja",
    "korean": "ko",
    "chinese": "zh-Hans",
    "arabic": "ar",
    "russian": "ru"
}

ROMANIZED = {
    "hi", "te", "ta", "kn", "ml",
    "bn", "gu", "pa", "mr",
    "ja", "ko", "zh-Hans", "ar", "ru"
}


def translate(text, target):

    lang = LANGS[target]

    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Ocp-Apim-Subscription-Region": REGION,
        "Content-Type": "application/json"
    }

    params = {
        "api-version": "3.0",
        "to": lang
    }

    if lang in ROMANIZED:
        params["toScript"] = "Latn"

    body = [
        {
            "text": text
        }
    ]

    r = requests.post(
        ENDPOINT + "/translate",
        params=params,
        headers=headers,
        json=body
    )

    r.raise_for_status()

    data = r.json()

    return data[0]["translations"][0]["text"]


print("=== Professional Quantum Terminal v3.0 ===")
print("Supported Languages:")
print(", ".join(LANGS.keys()).upper())
print("Encoders: BINARY HEX OCTAL ASCII BASE64")

while True:

    try:

        cmd = input("\ncore@quantum_matrix:~$ ").strip()

        if cmd.lower() in ("exit", "quit"):
            break

        if cmd.lower() == "clear":
            print("\n" * 100)
            continue

        match = re.search(r"(.*)\(func translate to (.*)\)", cmd)

        if not match:
            print(">> SYNTAX ERROR")
            continue

        payload = match.group(1).strip()
        target = match.group(2).strip().lower()

        if target == "binary":
            result = " ".join(format(ord(c), "08b") for c in payload)

        elif target == "hex":
            result = " ".join(format(ord(c), "02X") for c in payload)

        elif target == "octal":
            result = " ".join(format(ord(c), "03o") for c in payload)

        elif target == "ascii":
            result = " ".join(str(ord(c)) for c in payload)

        elif target == "base64":
            result = base64.b64encode(payload.encode()).decode()

        elif target in LANGS:
            result = translate(payload, target)

        else:
            result = "!! UNKNOWN TARGET ENCODER/LANG !!"

        print(f">> OUTPUT ({target.upper()}): {result}")

    except Exception as e:
        print(">> ERROR:", e)
