import re
import customtkinter as ctk
import encoders

ctk.set_appearance_mode("dark")

class AsciiTerminalTranslator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Terminal Console - ASCII Core")
        self.geometry("680x450")
        self.resizable(False, False)
        self.configure(fg_color="#000000")

        self.terminal_display = ctk.CTkTextbox(self, font=ctk.CTkFont(family="Consolas", size=13), fg_color="#000000", text_color="#00FF33", insert_color="#00FF33", border_width=0, corner_radius=0)
        self.terminal_display.pack(fill="both", expand=True, padx=15, pady=(15, 0))
        self.terminal_display.insert("end", "====================================================================\n ASCII PARSER HARDWARE LAYER\n====================================================================\n Ready for execution strings.\n Syntax Layout: [string payload] (func translate to ascii)\n\n")

        self.input_frame = ctk.CTkFrame(self, fg_color="#000000", corner_radius=0)
        self.input_frame.pack(fill="x", padx=15, pady=(0, 15))
        ctk.CTkLabel(self.input_frame, text="translator@ascii:~$ ", font=ctk.CTkFont(family="Consolas", size=13, weight="bold"), text_color="#00FF33").pack(side="left")

        self.command_entry = ctk.CTkEntry(self.input_frame, font=ctk.CTkFont(family="Consolas", size=13), fg_color="#000000", text_color="#ffffff", border_width=0, insert_color="#00FF33", corner_radius=0)
        self.command_entry.pack(side="left", fill="x", expand=True)
        self.command_entry.focus_set()
        self.command_entry.bind("<Return>", self.execute_terminal_line)

    def execute_terminal_line(self, event=None):
        raw_cmd = self.command_entry.get().strip()
        self.command_entry.delete(0, "end")
        if not raw_cmd: return
        self.terminal_display.insert("end", f"translator@ascii:~$ {raw_cmd}\n")

        if raw_cmd.lower() in ["clear", "cls"]:
            self.terminal_display.delete("1.0", "end")
            return

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
        except ValueError as err:
            self.terminal_display.insert("end", f" >> VALUE ERROR: {err}\n\n")
        except Exception as err:
            self.terminal_display.insert("end", f" >> COMPILATION ERROR: {err}\n\n")
        self.terminal_display.see("end")

if __name__ == "__main__":
    AsciiTerminalTranslator().mainloop()
  
