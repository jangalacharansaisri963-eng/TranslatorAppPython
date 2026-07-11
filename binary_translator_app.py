import re
import encoders
from base_terminal import BaseTerminalApp

class BinaryTerminalTranslator(BaseTerminalApp):
    def __init__(self):
        # Pass the layout configuration parameters up to the base engine
        super().__init__(
            title_name="Terminal Console - Binary Core",
            syntax_hints="Syntax Layout:\n   - text (func translate to binary)\n   - code (func translate to english)",
            prompt_label="translator@binary:~$ "
        )

    def process_command(self, raw_cmd):
        # Extracted pure Binary regex and execution logic
        match_to_target = re.search(r'\s+\(func translate to binary\)\s*$', raw_cmd, re.IGNORECASE)
        match_to_eng = re.search(r'\s+\(func translate to english\)\s*$', raw_cmd, re.IGNORECASE)

        try:
            if match_to_target:
                payload = raw_cmd[:match_to_target.start()].strip()
                label, res = encoders.process_binary(payload, decode_mode=False)
                self.terminal_display.insert("end", f" >> TARGET LANG: {label}\n >> TRANSLATION : {res}\n\n")
                self.last_result = res  # Cache saved for (func copy)
                
            elif match_to_eng:
                payload = raw_cmd[:match_to_eng.start()].strip()
                label, res = encoders.process_binary(payload, decode_mode=True)
                self.terminal_display.insert("end", f" >> TARGET LANG: {label}\n >> TRANSLATION : {res}\n\n")
                self.last_result = res  # Cache saved for (func copy)
                
            else:
                self.terminal_display.insert("end", " >> SYNTAX ERROR: Expecting (func translate to binary) or (func translate to english)\n\n")
        except Exception as err:
            self.terminal_display.insert("end", f" >> DECODER ERROR: Data stream recovery failed. Info: {err}\n\n")

if __name__ == "__main__":
    BinaryTerminalTranslator().mainloop()
    
