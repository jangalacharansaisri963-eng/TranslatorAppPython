import re
import encoders
from base_terminal import BaseTerminalApp

class AsciiTerminalTranslator(BaseTerminalApp):
    def __init__(self):
        # Pass the unique parameters up to the BaseTerminalApp layout engine
        super().__init__(
            title_name="Terminal Console - ASCII Core",
            syntax_hints="Syntax Layout: [string payload] (func translate to ascii)",
            prompt_label="translator@ascii:~$ "
        )

    def process_command(self, raw_cmd):
        # pure ASCII parsing and extraction logic
        match = re.search(r'\s+\(func translate to ascii\)\s*$', raw_cmd, re.IGNORECASE)
        if not match:
            self.terminal_display.insert("end", " >> SYNTAX ERROR: Expecting structure ending with (func translate to ascii)\n\n")
            return

        payload_phrase = raw_cmd[:match.start()].strip()
        if not payload_phrase:
            self.terminal_display.insert("end", " >> INPUT ERROR: Context message parameter index null.\n\n")
            return

        try:
            label, res = encoders.process_ascii(payload_phrase)
            self.terminal_display.insert("end", f" >> TARGET LANG: {label}\n >> TRANSLATION : {res}\n\n")
            
            # Lock the processed data into the base class copy slot
            self.last_result = res
            
        except ValueError as err:
            self.terminal_display.insert("end", f" >> VALUE ERROR: {err}\n\n")
        except Exception as err:
            self.terminal_display.insert("end", f" >> COMPILATION ERROR: {err}\n\n")

if __name__ == "__main__":
    AsciiTerminalTranslator().mainloop()
    
