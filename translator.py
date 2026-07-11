import base64
import re
from deep_translator import GoogleTranslator

# --- ENGINE CONFIGURATION ---
def get_lang_code(target):
    # Mapping for translation APIs
    mapping = {
        "hindi": "hi", "telugu": "te", "tamil": "ta", 
        "spanish": "es", "french": "fr", "german": "de", "english": "en"
    }
    return mapping.get(target)

def run_translator():
    print("--- Professional Quantum Terminal v2.0 ---")
    print("Supported: HINDI, TELUGU, TAMIL, SPANISH, FRENCH, GERMAN, ENGLISH")
    print("Encoders: BINARY, HEX, OCTAL, ASCII, BASE64")
    
    while True:
        try:
            cmd = input("\ncore@quantum_matrix:~$ ").strip()
            if cmd.lower() in ['exit', 'quit']: break
            if cmd.lower() == 'clear':
                print("\n" * 100)
                continue
            
            match = re.search(r'(.*)\(func translate to (.*)\)', cmd)
            if not match:
                print(" >> SYNTAX ERROR: Use [text] (func translate to [target])")
                continue
                
            payload, target = match.group(1).strip(), match.group(2).strip().lower()
            res = ""

            # 1. Digital Encoder Logic
            if target == "binary": res = ' '.join(format(ord(c), '08b') for c in payload)
            elif target == "hex": res = ' '.join(format(ord(c), '02x') for c in payload)
            elif target == "octal": res = ' '.join(format(ord(c), '03o') for c in payload)
            elif target == "ascii": res = ' '.join(str(ord(c)) for c in payload)
            elif target == "base64": res = base64.b64encode(payload.encode('utf-8')).decode('utf-8')
            
            # 2. Natural Language Translation Logic
            else:
                lang_code = get_lang_code(target)
                if lang_code:
                    res = GoogleTranslator(source='auto', target=lang_code).translate(payload)
                else:
                    res = "!! UNKNOWN TARGET ENCODER/LANG !!"
            
            print(f" >> OUTPUT ({target.upper()}): {res}")
                
        except Exception as e:
            print(f" >> DECODE ERROR: {e}")

if __name__ == "__main__":
    run_translator()
  
