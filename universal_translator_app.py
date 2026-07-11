import re
import base64
import tkinter as tk
import customtkinter as ctk
from deep_translator import GoogleTranslator

# Global aesthetic profile overrides for terminal emulation
ctk.set_appearance_mode("dark")

class UniversalTerminalTranslator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configurations
        self.title("Terminal Console - Universal Translator Core")
        self.geometry("680x450")
        self.resizable(False, False)
        self.configure(fg_color="#000000") # Pure pitch-black terminal backplate

        # Dynamic Engine Mapping Configurations
        self.engines = {
            "spanish": GoogleTranslator(source='en', target='es'),
            "french": GoogleTranslator(source='en', target='fr'),
            "german": GoogleTranslator(source='en', target='de'),
            "english": GoogleTranslator(source='auto', target='en') # Auto-detects input for English targets
        }

        # Main Terminal Output History Screen (Simulates scrolling terminal text)
        self.terminal_display = ctk.CTkTextbox(
            self,
            font=ctk.CTkFont(family="Consolas", size=13),
            fg_color="#000000",
            text_color="#00FF33",       # Classic retro neon Green matrix color
            insert_color="#00FF33",     # Green text cursor
            border_width=0,
            corner_radius=0
        )
        self.terminal_display.pack(fill="both", expand=True, padx=15, pady=(15, 0))
        
        # Print initial system boot screen messages
        self.boot_terminal_display()

        # Bottom Command Line Input Block Layout
        self.input_frame = ctk.CTkFrame(self, fg_color="#000000", corner_radius=0)
        self.input_frame.pack(fill="x", padx=15, pady=(0, 15))

        # Terminal Prompt Token (C:\> style marker)
        self.prompt_label = ctk.CTkLabel(
            self.input_frame,
            text="translator@core:~$ ",
            font=ctk.CTkFont(family="Consolas", size=13, weight="bold"),
            text_color="#00FF33"
        )
        self.prompt_label.pack(side="left")

        # Command Line Entry Field
        self.command_entry = ctk.CTkEntry(
            self.input_frame,
            font=ctk.CTkFont(family="Consolas", size=13),
            fg_color="#000000",
            text_color="#ffffff",       # User types in stark white text for emphasis
            border_width=0,
            insert_color="#00FF33",
            corner_radius=0
        )
        self.command_entry.pack(side="left", fill="x", expand=True)
        
        # Focus keyboard cursor to the entry instantly on startup
        self.command_entry.focus_set()

        # Bind the keyboard 'Return/Enter' key directly to processing
        self.command_entry.bind("<Return>", self.execute_terminal_line)

    def boot_terminal_display(self):
        """Prints diagnostic lines simulating terminal core startup operations."""
        boot_msg = (
            "====================================================================\n"
            " DIRECT NETWORK MULTI-LANGUAGE TRANSLATION PARSER HARDWARE LAYER   \n"
            "====================================================================\n"
            " Ready for execution strings.\n"
            " Syntax Layout: [string payload data] (func translate to [target])\n"
            " Supported Targets: 'spanish' | 'french' | 'german' | 'english'\n"
            " Encoding Targets:  'binary'  | 'hex'    | 'octal'  | 'base64' | 'ascii'\n"
            " Clear Screen: Type 'clear' and press enter.\n\n"
        )
        self.append_to_terminal(boot_msg)

    def append_to_terminal(self, text):
        """Helper to unlock, append system logging lines, and scroll to position."""
        self.terminal_display.insert("end", text)
        self.terminal_display.see("end")

    def execute_terminal_line(self, event=None):
        """Intercepts command entries on Enter key triggers and evaluates patterns."""
        raw_cmd = self.command_entry.get().strip()
        
        # Clear entry line instantly after parsing capture
        self.command_entry.delete(0, "end")

        if not raw_cmd:
            return

        # Print the entered user command to the log history matrix
        self.append_to_terminal(f"translator@core:~$ {raw_cmd}\n")

        # System clearing catch string
        if raw_cmd.lower() in ["clear", "cls"]:
            self.terminal_display.delete("1.0", "end")
            return

        # Enforces at least one space character before the execution function syntax bracket
        match = re.search(r'\s+\(func translate to ([a-zA-Z0-9]+)\)\s*$', raw_cmd, re.IGNORECASE)

        if not match:
            self.append_to_terminal(" >> SYNTAX ERROR: Invalid execution brackets or missing space.\n >> Expected structure: Text message (func translate to [target])\n\n")
            return

        target_lang = match.group(1).lower().strip()
        split_index = match.start()
        payload_phrase = raw_cmd[:split_index].strip()

        if not payload_phrase:
            self.append_to_terminal(" >> INPUT ERROR: Context message parameter index null.\n\n")
            return

        # ─── LOCAL ENCODING PROCESSORS ───
        
        # ASCII Bidirectional Target
        if target_lang == "ascii":
            try:
                # If input is entirely digit numbers spaced out, decode them back to text
                if re.match(r'^[0-9\s]+$', payload_phrase):
                    ascii_codes = payload_phrase.split()
                    decoded_chars = []
                    for code in ascii_codes:
                        val = int(code)
                        if 0 <= val <= 255:
                            decoded_chars.append(chr(val))
                        else:
                            self.append_to_terminal(f" >> VALUE ERROR: Code '{val}' is outside valid ASCII boundaries (0-255).\n\n")
                            return
                    result = "".join(decoded_chars)
                    self.append_to_terminal(f" >> TARGET LANG: ASCII (DECODED CODES)\n >> TRANSLATION : {result}\n\n")
                
                # If it contains standard text characters, encode them into numeric ASCII decimals
                else:
                    ascii_data = ' '.join(str(ord(char)) for char in payload_phrase)
                    self.append_to_terminal(f" >> TARGET LANG: ASCII (CODES OUTPUT)\n >> TRANSLATION : {ascii_data}\n\n")
            except Exception as err:
                self.append_to_terminal(f" >> COMPILATION ERROR: {err}\n\n")
            return

        # Binary Target
        if target_lang == "binary":
            try:
                binary_data = ' '.join(format(ord(char), '08b') for char in payload_phrase)
                self.append_to_terminal(f" >> TARGET LANG: BINARY\n >> TRANSLATION : {binary_data}\n\n")
            except Exception as err:
                self.append_to_terminal(f" >> COMPILATION ERROR: {err}\n\n")
            return

        # Hexadecimal Target
        if target_lang == "hex":
            try:
                hex_data = ' '.join(format(ord(char), '02x') for char in payload_phrase)
                self.append_to_terminal(f" >> TARGET LANG: HEXADECIMAL\n >> TRANSLATION : {hex_data}\n\n")
            except Exception as err:
                self.append_to_terminal(f" >> COMPILATION ERROR: {err}\n\n")
            return

        # Octal Target
        if target_lang == "octal":
            try:
                octal_data = ' '.join(format(ord(char), '03o') for char in payload_phrase)
                self.append_to_terminal(f" >> TARGET LANG: OCTAL\n >> TRANSLATION : {octal_data}\n\n")
            except Exception as err:
                self.append_to_terminal(f" >> COMPILATION ERROR: {err}\n\n")
            return

        # Base64 Target
        if target_lang == "base64":
            try:
                b64_bytes = base64.b64encode(payload_phrase.encode('utf-8'))
                self.append_to_terminal(f" >> TARGET LANG: BASE64\n >> TRANSLATION : {b64_bytes.decode('utf-8')}\n\n")
            except Exception as err:
                self.append_to_terminal(f" >> COMPILATION ERROR: {err}\n\n")
            return

        # ─── TRANSLATION AND DECODING INTERCEPT LOOPS ───
        if target_lang == "english":
            try:
                # Intercept Binary Decoder
                if re.match(r'^[01\s]+$', payload_phrase):
                    clean_binary = payload_phrase.replace(" ", "")
                    byte_chunks = [clean_binary[i:i+8] for i in range(0, len(clean_binary), 8)]
                    decoded_text = "".join([chr(int(b, 2)) for b in byte_chunks if len(b) == 8])
                    self.append_to_terminal(f" >> TARGET LANG: ENGLISH (BINARY DECODED)\n >> TRANSLATION : {decoded_text}\n\n")
                    return

                # Intercept Hexadecimal Decoder
                if re.match(r'^[0-9a-fA-F\s]+$', payload_phrase) and (any(c in payload_phrase for c in 'abcdefABCDEF') or len(payload_phrase.replace(" ", "")) % 2 == 0):
                    clean_hex = payload_phrase.replace(" ", "")
                    decoded_text = bytes.fromhex(clean_hex).decode('utf-8', errors='ignore')
                    self.append_to_terminal(f" >> TARGET LANG: ENGLISH (HEX DECODED)\n >> TRANSLATION : {decoded_text}\n\n")
                    return

                # Intercept Octal Decoder
                if re.match(r'^[0-7\s]+$', payload_phrase) and (" " in payload_phrase or len(payload_phrase) >= 3):
                    octal_chunks = payload_phrase.split()
                    decoded_text = "".join([chr(int(o, 8)) for o in octal_chunks])
                    self.append_to_terminal(f" >> TARGET LANG: ENGLISH (OCTAL DECODED)\n >> TRANSLATION : {decoded_text}\n\n")
                    return

                # Intercept Base64 Decoder
                if re.match(r'^[A-Za-z0-9+/=\s]+$', payload_phrase) and (len(payload_phrase.replace(" ", "")) % 4 == 0 or "=" in payload_phrase):
                    try:
                        decoded_bytes = base64.b64decode(payload_phrase.strip())
                        decoded_text = decoded_bytes.decode('utf-8')
                        self.append_to_terminal(f" >> TARGET LANG: ENGLISH (BASE64 DECODED)\n >> TRANSLATION : {decoded_text}\n\n")
                        return
                    except:
                        pass 

            except Exception as decode_err:
                self.append_to_terminal(f" >> DECODER ERROR: Data stream recovery failed. Info: {decode_err}\n\n")
                return

        # Handle Standard Natural Language Translation Engine Pipelines
        if target_lang in self.engines:
            try:
                translated_data = self.engines[target_lang].translate(payload_phrase)
                self.append_to_terminal(f" >> TARGET LANG: {target_lang.upper()}\n >> TRANSLATION : {translated_data}\n\n")
            except Exception as api_err:
                self.append_to_terminal(f" >> NETWORK TIMEOUT: Gateway request refused. Info: {api_err}\n\n")
        else:
            self.append_to_terminal(f" >> TARGET ERROR: Unsupported language modifier '{target_lang}'.\n >> Options: 'spanish', 'french', 'german', 'english', 'binary', 'hex', 'octal', 'base64', 'ascii'.\n\n")


if __name__ == "__main__":
    app = UniversalTerminalTranslator()
    app.mainloop()
    
