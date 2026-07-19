import base64
import re
import pyperclip
from deep_translator import GoogleTranslator

# -----------------------------
# LANGUAGE CODES
# -----------------------------
def get_lang_code(target):
    mapping = {
        "english": "en",
        "spanish": "es",
        "french": "fr",
        "german": "de",
        "italian": "it",
        "portuguese": "pt",
        "dutch": "nl",
        "swedish": "sv",
        "norwegian": "no",
        "danish": "da",
        "finnish": "fi",
        "polish": "pl",
        "czech": "cs",
        "slovak": "sk",
        "romanian": "ro",
        "hungarian": "hu",
        "croatian": "hr",
        "slovenian": "sl",
        "albanian": "sq",
        "estonian": "et",
        "latvian": "lv",
        "lithuanian": "lt",
        "turkish": "tr",
        "indonesian": "id",
        "malay": "ms",
        "filipino": "tl",
        "vietnamese": "vi",
        "irish": "ga",
        "welsh": "cy",
        "afrikaans": "af",
        "swahili": "sw",
        "latin": "la"
    }
    return mapping.get(target)


# -----------------------------
# MAIN TERMINAL
# -----------------------------
def run_translator():

    print("=== Professional Quantum Terminal v3.0 ===")
    print("Supported Languages:")
    print("ENGLISH, SPANISH, FRENCH, GERMAN, ITALIAN, PORTUGUESE")
    print("DUTCH, SWEDISH, NORWEGIAN, DANISH, FINNISH")
    print("POLISH, CZECH, SLOVAK, ROMANIAN, HUNGARIAN")
    print("CROATIAN, SLOVENIAN, ALBANIAN")
    print("ESTONIAN, LATVIAN, LITHUANIAN")
    print("TURKISH, INDONESIAN, MALAY, FILIPINO")
    print("VIETNAMESE, IRISH, WELSH, AFRIKAANS, SWAHILI, LATIN")
    print("Encoders: BINARY, HEX, OCTAL, ASCII, BASE64")
    print("Commands:")
    print("(func copy)  -> Copy latest output")
    print("(func paste) -> Show clipboard")

    last_result = ""

    while True:

        try:

            cmd = input("\ncore@quantum_matrix:~$ ").strip()

            if cmd.lower() in ("exit", "quit"):
                break

            if cmd.lower() == "clear":
                print("\n" * 100)
                continue

            if cmd.lower() == "(func copy)":
                if last_result:
                    pyperclip.copy(last_result)
                    print(">> Latest output copied to clipboard.")
                else:
                    print(">> Nothing to copy.")
                continue

            if cmd.lower() == "(func paste)":
                try:
                    pasted = pyperclip.paste()
                    print(f">> CLIPBOARD: {pasted}")
                except Exception as e:
                    print(f">> Clipboard Error: {e}")
                continue

            match = re.search(r"(.*)\(func translate to (.*)\)", cmd)

            if not match:
                print(">> SYNTAX ERROR: Use [text] (func translate to [target])")
                continue

            payload = match.group(1).strip()
            target = match.group(2).strip().lower()

            # -----------------------------
            # ENCODERS
            # -----------------------------

            if target == "binary":
                result = " ".join(format(ord(c), "08b") for c in payload)

            elif target == "hex":
                result = " ".join(format(ord(c), "02X") for c in payload)

            elif target == "octal":
                result = " ".join(format(ord(c), "03o") for c in payload)

            elif target == "ascii":
                result = " ".join(str(ord(c)) for c in payload)

            elif target == "base64":
                result = base64.b64encode(payload.encode("utf-8")).decode("utf-8")

            # -----------------------------
            # TRANSLATION
            # -----------------------------

            else:
                lang = get_lang_code(target)

                if lang:
                    result = GoogleTranslator(
                        source="auto",
                        target=lang
                    ).translate(payload)
                else:
                    result = "!! UNKNOWN TARGET ENCODER/LANG !!"

            last_result = result
            print(f">> OUTPUT ({target.upper()}): {result}")

        except Exception as e:
            print(f">> ERROR: {e}")


if __name__ == "__main__":
    run_translator()
