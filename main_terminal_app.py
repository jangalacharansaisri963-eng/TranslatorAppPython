import re
import encoders
from base_terminal import BaseTerminalApp

class UnifiedTerminalConsole(BaseTerminalApp):
    def __init__(self):
        super().__init__(
            title_name="Terminal Console - Unified Quantum Core",
            syntax_hints=(
                "Global Syntax Routines:\n"
                "   - [text] (func translate to binary/hex/octal/ascii/base64)\n"
                "   - [text] (func translate to hindi/spanish/french/german)\n"
                "   - [code] (func translate to english)"
            ),
            prompt_label="core@quantum_matrix:~$ "
        )

    def process_command(self, raw_cmd):
        # 1. Check for Language Decode back to English
        match_to_eng = re.search(r'\s+\(func translate to english\)\s*$', raw_cmd, re.IGNORECASE)
        if match_to_eng:
            payload = raw_cmd[:match_to_eng.start()].strip()
            self._execute_decoding_routing(payload)
            return

        # 2. Check for Encoders / Foreign Pipeline Targets
        match_binary = re.search(r'\s+\(func translate to binary\)\s*$', raw_cmd, re.IGNORECASE)
        match_hex = re.search(r'\s+\(func translate to hex\)\s*$', raw_cmd, re.IGNORECASE)
        match_octal = re.search(r'\s+\(func translate to octal\)\s*$', raw_cmd, re.IGNORECASE)
        match_ascii = re.search(r'\s+\(func translate to ascii\)\s*$', raw_cmd, re.IGNORECASE)
        match_base64 = re.search(r'\s+\(func translate to base64\)\s*$', raw_cmd, re.IGNORECASE)

        # 3. Check for Natural Language Translation Targets
        match_hindi = re.search(r'\s+\(func translate to hindi\)\s*$', raw_cmd, re.IGNORECASE)
        match_spanish = re.search(r'\s+\(func translate to spanish\)\s*$', raw_cmd, re.IGNORECASE)
        match_french = re.search(r'\s+\(func translate to french\)\s*$', raw_cmd, re.IGNORECASE)
        match_german = re.search(r'\s+\(func translate to german\)\s*$', raw_cmd, re.IGNORECASE)

        try:
            # --- Handle Digital Encoders ---
            if match_binary:
                payload = raw_cmd[:match_binary.start()].strip()
                label, res = encoders.process_foreign_to_encoder(payload, "binary") if encoders.is_foreign_text(payload) else encoders.process_binary(payload, decode_mode=False)
            elif match_hex:
                payload = raw_cmd[:match_hex.start()].strip()
                label, res = encoders.process_foreign_to_encoder(payload, "hex") if encoders.is_foreign_text(payload) else encoders.process_hex(payload, decode_mode=False)
            elif match_octal:
                payload = raw_cmd[:match_octal.start()].strip()
                label, res = encoders.process_foreign_to_encoder(payload, "octal") if encoders.is_foreign_text(payload) else encoders.process_octal(payload, decode_mode=False)
            elif match_ascii:
                payload = raw_cmd[:match_ascii.start()].strip()
                label, res = encoders.process_foreign_to_encoder(payload, "ascii") if encoders.is_foreign_text(payload) else encoders.process_ascii(payload)
            elif match_base64:
                payload = raw_cmd[:match_base64.start()].strip()
                label, res = encoders.process_foreign_to_encoder(payload, "base64") if encoders.is_foreign_text(payload) else encoders.process_base64(payload, decode_mode=False)
            
            # --- Handle Natural Languages ---
            elif match_hindi:
                payload = raw_cmd[:match_hindi.start()].strip()
                label, res = "HINDI", encoders.translate_api("hindi", payload)
            elif match_spanish:
                payload = raw_cmd[:match_spanish.start()].strip()
                label, res = "SPANISH", encoders.translate_api("spanish", payload)
            elif match_french:
                payload = raw_cmd[:match_french.start()].strip()
                label, res = "FRENCH", encoders.translate_api("french", payload)
            elif match_german:
                payload = raw_cmd[:match_german.start()].strip()
                label, res = "GERMAN", encoders.translate_api("german", payload)
            else:
                self.terminal_display.insert("end", " >> SYNTAX ERROR: Command instruction label unrecognized.\n\n")
                return

            self.terminal_display.insert("end", f" >> TARGET LANG: {label}\n >> TRANSLATION : {res}\n\n")
            self.last_result = res

        except Exception as err:
            self.terminal_display.insert("end", f" >> DECODER ERROR: Execution operation rejected. Info: {err}\n\n")

    def _execute_decoding_routing(self, payload):
        """ Internal smart router to safely map numeric/hash formats back to text strings """
        try:
            if re.match(r'^[01\s]+$', payload):
                label, res = encoders.process_binary(payload, decode_mode=True)
            elif re.match(r'^[0-7\s]+$', payload) and (" " in payload or len(payload) >= 3):
                label, res = encoders.process_octal(payload, decode_mode=True)
            elif re.match(r'^[0-9\s]+$', payload):
                label, res = encoders.process_ascii(payload)
            elif re.match(r'^[A-Za-z0-9+/=\s]+$', payload) and (len(payload.replace(" ", "")) % 4 == 0 or "=" in payload):
                label, res = encoders.process_base64(payload, decode_mode=True)
            else:
                label, res = encoders.process_hex(payload, decode_mode=True)
            
            self.terminal_display.insert("end", f" >> TARGET LANG: {label}\n >> TRANSLATION : {res}\n\n")
            self.last_result = res
        except Exception as err:
            try:
                res = encoders.translate_api("english", payload)
                self.terminal_display.insert("end", f" >> TARGET LANG: ENGLISH (AUTO DETECTED)\n >> TRANSLATION : {res}\n\n")
                self.last_result = res
            except Exception:
                self.terminal_display.insert("end", f" >> DECODER ERROR: Reverse analysis failed. Info: {err}\n\n")

if __name__ == "__main__":
    UnifiedTerminalConsole().mainloop()
              
