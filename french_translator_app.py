import re
import encoders
from base_terminal import BaseTerminalApp

class FrenchTerminalTranslator(BaseTerminalApp):
    def __init__(self):
        # Pass the layout configuration parameters up to the base engine
        super().__init__(
            title_name="Terminal Console - French Core",
            syntax_hints="Syntax Layout:\n   - text (func translate to french)\n   - text (func translate to english)",
            prompt_label="translator@french:~$ "
        )

    def process_command(self, raw_cmd):
        # Extracted pure French translation regex and execution logic
        match_to_french = re.search(r'\s+\(func translate to french\)\s*$', raw_cmd, re.IGNORECASE)
        match_to_english = re.search(r'\s+\(func translate to english\)\s*$', raw_cmd, re.IGNORECASE)

        if match_to_french:
            payload_phrase = raw_cmd[:match_to_french.start()].strip()
            target = "french"
        elif match_to_english:
            payload_phrase = raw_cmd[:match_to_english.start()].strip()
            target = "english"
        else:
            self.terminal_display.insert("end", " >> SYNTAX ERROR: Expecting (func translate to french) or (func translate to english)\n\n")
            return

        if not payload_phrase:
            self.terminal_display.insert("end", " >> INPUT ERROR: Context message parameter index null.\n\n")
            return

        try:
            res = encoders.translate_api(target, payload_phrase)
            self.terminal_display.insert("end", f" >> TARGET LANG: {target.upper()}\n >> TRANSLATION : {res}\n\n")
            self.last_result = res  # Cache saved for (func copy)
        except Exception as err:
            self.terminal_display.insert("end", f" >> NETWORK TIMEOUT: Gateway request refused. Info: {err}\n\n")

if __name__ == "__main__":
    FrenchTerminalTranslator().mainloop()
    
