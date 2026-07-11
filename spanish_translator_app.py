import re
import encoders
from base_terminal import BaseTerminalApp

class SpanishTerminalTranslator(BaseTerminalApp):
    def __init__(self):
        super().__init__(
            title_name="Terminal Console - Spanish Core",
            syntax_hints="Syntax Layout:\n   - text (func translate to spanish)\n   - text (func translate to english)",
            prompt_label="translator@spanish:~$ "
        )

    def process_command(self, raw_cmd):
        match_to_spanish = re.search(r'\s+\(func translate to spanish\)\s*$', raw_cmd, re.IGNORECASE)
        match_to_english = re.search(r'\s+\(func translate to english\)\s*$', raw_cmd, re.IGNORECASE)

        if match_to_spanish:
            payload_phrase = raw_cmd[:match_to_spanish.start()].strip()
            target = "spanish"
        elif match_to_english:
            payload_phrase = raw_cmd[:match_to_english.start()].strip()
            target = "english"
        else:
            self.terminal_display.insert("end", " >> SYNTAX ERROR: Mismatched routing brackets.\n\n")
            return

        try:
            res = encoders.translate_api(target, payload_phrase)
            self.terminal_display.insert("end", f" >> TARGET LANG: {target.upper()}\n >> TRANSLATION : {res}\n\n")
            self.last_result = res
        except Exception as err:
            self.terminal_display.insert("end", f" >> SYSTEM ERROR: Info: {err}\n\n")
            
