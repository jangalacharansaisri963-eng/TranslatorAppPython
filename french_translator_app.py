import re
import customtkinter as ctk
import encoders

ctk.set_appearance_mode("dark")

class FrenchTerminalTranslator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Terminal Console - French Core")
        self.geometry("680x450")
        self.resizable(False, False)
        self.configure(fg_color="#000000")

        self.terminal_display = ctk.CTkTextbox(self, font=ctk.CTkFont(family="Consolas", size=13), fg_color="#000000", text_color="#00FF33", insert_color="#00FF33", border_width=0, corner_radius=0)
        self.terminal_display.pack(fill="both", expand=True, padx=15, pady=(15, 0))
        
        self.terminal_display.insert("end", "====================================================================\n FRENCH TRANSLATION PARSER HARDWARE LAYER\n====================================================================\n Ready for execution strings.\n Syntax Layout:\n   - text (func translate to french)\n   - text (func translate to english)\n\n")

        self.input_frame = ctk.CTkFrame(self, fg_color="#000000", corner_radius=0)
        self.input_frame.pack(fill="x", padx=15, pady=(0, 15))
        ctk.CTkLabel(self.input_frame, text="translator@french:~$ ", font=ctk.CTkFont(family="Consolas", size=13, weight="bold"), text_color="#00FF33").pack(side="left")

        self.command_entry = ctk.CTkEntry(self.input_frame, font=ctk.CTkFont(family="Consolas", size=13), fg_color="#000000", text_color="#ffffff", border_width=0, insert_color="#00FF33", corner_radius=0)
        self.command_entry.pack(side="left", fill="x", expand=True)
        self.command_entry.focus_set()
        self.command_entry.bind("<Return>", self.execute_terminal_line)

    def execute_terminal_line(self, event=None):
        raw_cmd = self.command_entry.get().strip()
        self.command_entry.delete(0, "end")
        if not raw_cmd: return
        self.terminal_display.insert("end", f"translator@french:~$ {raw_cmd}\n")

        if raw_cmd.lower() in ["clear", "cls"]:
            self.terminal_display.delete("1.0", "end")
            return

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
        except Exception as err:
            self.terminal_display.insert("end", f" >> NETWORK TIMEOUT: Gateway request refused. Info: {err}\n\n")
        self.terminal_display.see("end")

if __name__ == "__main__":
    FrenchTerminalTranslator().mainloop()
    
