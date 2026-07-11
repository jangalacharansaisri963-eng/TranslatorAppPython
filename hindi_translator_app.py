import re
import customtkinter as ctk
import encoders

ctk.set_appearance_mode("dark")

class HindiTerminalTranslator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Terminal Console - Hindi Core")
        self.geometry("680x450")
        self.resizable(False, False)
        self.configure(fg_color="#000000")

        # Text display using Segoe UI so Hindi characters don't turn into boxes
        self.terminal_display = ctk.CTkTextbox(
            self, 
            font=ctk.CTkFont(family="Segoe UI", size=13), 
            fg_color="#000000", 
            text_color="#00FF33", 
            insert_color="#00FF33", 
            border_width=0, 
            corner_radius=0
        )
        self.terminal_display.pack(fill="both", expand=True, padx=15, pady=(15, 0))
        
        self.terminal_display.insert(
            "end", 
            "====================================================================\n"
            " HINDI TRANSLATION PARSER CORE LAYER\n"
            "====================================================================\n"
            " Ready for execution strings.\n"
            " Syntax Layout:\n"
            "   - text (func translate to hindi)\n"
            "   - text (func translate to english)\n"
            "   - (func copy) -> Copies last output matrix\n\n"
        )

        # Bottom Input Area
        self.input_frame = ctk.CTkFrame(self, fg_color="#000000", corner_radius=0)
        self.input_frame.pack(fill="x", padx=15, pady=(0, 15))

        ctk.CTkLabel(
            self.input_frame, 
            text="translator@hindi:~$ ", 
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), 
            text_color="#00FF33"
        ).pack(side="left")

        self.command_entry = ctk.CTkEntry(
            self.input_frame, 
            font=ctk.CTkFont(family="Segoe UI", size=13), 
            fg_color="#000000", 
            text_color="#ffffff", 
            border_width=0, 
            insert_color="#00FF33", 
            corner_radius=0
        )
        self.command_entry.pack(side="left", fill="x", expand=True)
        self.command_entry.focus_set()
        
        # Binds the Return key to the execution process
        self.command_entry.bind("<Return>", self.execute_terminal_line)

        # Internal tracking variable to prevent crashes during copy routine
        self.last_result = ""

    def execute_terminal_line(self, event=None):
        raw_cmd = self.command_entry.get().strip()
        self.command_entry.delete(0, "end")
        if not raw_cmd: return
        
        # Display typed command back onto the terminal screen
        self.terminal_display.insert("end", f"translator@hindi:~$ {raw_cmd}\n")

        # 1. Clear Command Check
        if raw_cmd.lower() in ["clear", "cls"]:
            self.terminal_display.delete("1.0", "end")
            return

        # 2. Clipboard Copy Check
        if raw_cmd.lower() == "(func copy)":
            if self.last_result:
                self.clipboard_clear()
                self.clipboard_append(self.last_result)
                self.terminal_display.insert("end", " >> SYSTEM NOTIFICATION: Last result copied to clipboard!\n\n")
            else:
                self.terminal_display.insert("end", " >> SYSTEM ERROR: Cache empty. Nothing to copy.\n\n")
            self.terminal_display.see("end")
            return

        # 3. Regex Syntax Extraction
        match_to_hindi = re.search(r'\s+\(func translate to hindi\)\s*$', raw_cmd, re.IGNORECASE)
        match_to_english = re.search(r'\s+\(func translate to english\)\s*$', raw_cmd, re.IGNORECASE)

        if match_to_hindi:
            payload_phrase = raw_cmd[:match_to_hindi.start()].strip()
            target = "hindi"
        elif match_to_english:
            payload_phrase = raw_cmd[:match_to_english.start()].strip()
            target = "english"
        else:
            self.terminal_display.insert("end", " >> SYNTAX ERROR: Expecting (func translate to hindi) or (func translate to english)\n\n")
            self.terminal_display.see("end")
            return

        if not payload_phrase:
            self.terminal_display.insert("end", " >> INPUT ERROR: Context message payload null.\n\n")
            self.terminal_display.see("end")
            return

        # 4. Process Through Engine
        try:
            res = encoders.translate_api(target, payload_phrase)
            self.terminal_display.insert("end", f" >> TARGET LANG: {target.upper()}\n >> TRANSLATION : {res}\n\n")
            
            # Safely log output to cache for copying
            self.last_result = res
            
        except Exception as err:
            self.terminal_display.insert("end", f" >> NETWORK TIMEOUT: Request refused. Info: {err}\n\n")
            
        self.terminal_display.see("end")

if __name__ == "__main__":
    HindiTerminalTranslator().mainloop()
          
