import re
import base64
from deep_translator import GoogleTranslator

def translate_api(target_lang, text):
    """
    Handles bidirectional natural language translations routing.
    Uses source='auto' to cleanly accept input in any language and convert it
    strictly to the language specified by the UI app handler.
    """
    if target_lang == "spanish":
        return GoogleTranslator(source='auto', target='es').translate(text)
    elif target_lang == "french":
        return GoogleTranslator(source='auto', target='fr').translate(text)
    elif target_lang == "german":
        return GoogleTranslator(source='auto', target='de').translate(text)
    elif target_lang == "english":
        return GoogleTranslator(source='auto', target='en').translate(text)
    raise ValueError(f"Unsupported core language target: {target_lang}")

def process_ascii(payload_phrase):
    if re.match(r'^[0-9\s]+$', payload_phrase):
        ascii_codes = payload_phrase.split()
        decoded_chars = []
        for code in ascii_codes:
            val = int(code)
            if 0 <= val <= 255:
                decoded_chars.append(chr(val))
            else:
                raise ValueError(f"Code '{val}' is outside valid ASCII boundaries (0-255).")
        return "ASCII (DECODED CODES)", "".join(decoded_chars)
    else:
        return "ASCII (CODES OUTPUT)", ' '.join(str(ord(char)) for char in payload_phrase)

def process_binary(payload_phrase, decode_mode=False):
    if decode_mode:
        if not re.match(r'^[01\s]+$', payload_phrase):
            raise ValueError("Data stream corrupt: Non-binary content detected.")
        clean_binary = payload_phrase.replace(" ", "")
        byte_chunks = [clean_binary[i:i+8] for i in range(0, len(clean_binary), 8)]
        return "ENGLISH (BINARY DECODED)", "".join([chr(int(b, 2)) for b in byte_chunks if len(b) == 8])
    return "BINARY", ' '.join(format(ord(char), '08b') for char in payload_phrase)

def process_hex(payload_phrase, decode_mode=False):
    if decode_mode:
        if not (re.match(r'^[0-9a-fA-F\s]+$', payload_phrase) and (any(c in payload_phrase for c in 'abcdefABCDEF') or len(payload_phrase.replace(" ", "")) % 2 == 0)):
            raise ValueError("Data stream corrupt: Non-hex content detected.")
        clean_hex = payload_phrase.replace(" ", "")
        return "ENGLISH (HEX DECODED)", bytes.fromhex(clean_hex).decode('utf-8', errors='ignore')
    return "HEXADECIMAL", ' '.join(format(ord(char), '02x') for char in payload_phrase)

def process_octal(payload_phrase, decode_mode=False):
    if decode_mode:
        if not (re.match(r'^[0-7\s]+$', payload_phrase) and (" " in payload_phrase or len(payload_phrase) >= 3)):
            raise ValueError("Data stream corrupt: Non-octal content detected.")
        octal_chunks = payload_phrase.split()
        return "ENGLISH (OCTAL DECODED)", "".join([chr(int(o, 8)) for o in octal_chunks])
    return "OCTAL", ' '.join(format(ord(char), '03o') for char in payload_phrase)

def process_base64(payload_phrase, decode_mode=False):
    if decode_mode:
        if not (re.match(r'^[A-Za-z0-9+/=\s]+$', payload_phrase) and (len(payload_phrase.replace(" ", "")) % 4 == 0 or "=" in payload_phrase)):
            raise ValueError("Data stream corrupt: Non-base64 content detected.")
        decoded_bytes = base64.b64decode(payload_phrase.strip())
        return "ENGLISH (BASE64 DECODED)", decoded_bytes.decode('utf-8')
    return "BASE64", base64.b64encode(payload_phrase.encode('utf-8')).decode('utf-8')
    
