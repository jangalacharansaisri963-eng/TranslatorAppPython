import re
import encoders
from base_terminal import BaseTerminalApp

class HexTerminalTranslator(BaseTerminalApp):
    def __init__(self):
        super().__init__(
            title_name="Terminal Console - Hex Core",
            syntax_hints="Syntax Layout:\n   - text (func translate to hex)\n   - 414243 (func translate to english)",
            prompt_label="encoder@hex:~$ "
        )

    def process_command(self, raw_cmd):
        match_to_hex = re.search(r'\s+\(func translate to hex\)\s*$', raw_cmd, re.IGNORECASE)
        match_to_english = re.search(r'\s+\(func translate to english\)\s*$', raw_cmd, re.IGNORECASE)

        if match_to_hex:
            payload_phrase = raw_cmd[:match_to_hex.start()].strip()
            decode_mode = False
        elif match_to_english:
            payload_phrase = raw_cmd[:match_to_english.start()].strip()
            decode_mode = True
        else:
            self.terminal_display.insert("end", " >> SYNTAX ERROR: Mismatched hex routing parameters.\n\n")
            return

        try:
            label, res = encoders.process_hex(payload_phrase, decode_mode=decode_mode)
            self.terminal_display.insert("end", f" >> OPERATION : {label}\n >> RESULT    : {res}\n\n")
            self.last_result = res
        except Exception as err:
            self.terminal_display.insert("end", f" >> SYSTEM FAILURE: Data corruption mismatch. Info: {err}\n\n")
            
