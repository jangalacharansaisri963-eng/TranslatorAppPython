import re
import tkinter as tk
import customtkinter as ctk
from deep_translator import GoogleTranslator

# Global aesthetic profile overrides for terminal emulation
ctk.set_appearance_mode("dark")

class TerminalTranslator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configurations
        self.title("Terminal Console - Translator Core")
        self.geometry("680x450")
        self.resizable(False, False)
        self.configure(fg_color="#000000") # Pure pitch-black terminal backplate

        # Translation Hardware Engines
        self.to_spanish = GoogleTranslator(source='en', target='es')
        self.to_english = GoogleTranslator(source='es', target='en')

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
            " DIRECT NETWORK LANGUAGE TRANSLATION PARSER HARDWARE LAYER         \n"
            "====================================================================\n"
            " Ready for execution strings.\n"
            " Syntax Layout: [string payload data] (func translate to [target])\n"
            " Supported Targets: 'spanish' | 'english'\n"
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

        # Execute syntax regex separation matrix
        match = re.search(r'\s*\(func translate to ([a-zA-Z]+)\)\s*$', raw_cmd, re.IGNORECASE)

        if not match:
            self.append_to_terminal(" >> SYNTAX ERROR: Invalid execution brackets.\n >> Expected structure: Text message (func translate to spanish)\n\n")
            return

        target_lang = match.group(1).lower().strip()
        split_index = match.start()
        payload_phrase = raw_cmd[:split_index].strip()

        if not payload_phrase:
            self.append_to_terminal(" >> INPUT ERROR: Context message parameter index null.\n\n")
            return

        # Execute background network queries
        try:
            if target_lang == "spanish":
                translated_data = self.to_spanish.translate(payload_phrase)
                self.append_to_terminal(f" >> SOURCE LANG: ENGLISH\n >> TRANSLATION : {translated_data}\n\n")
            elif target_lang == "english":
                translated_data = self.to_english.translate(payload_phrase)
                self.append_to_terminal(f" >> SOURCE LANG: SPANISH\n >> TRANSLATION : {translated_data}\n\n")
            else:
                self.append_to_terminal(f" >> TARGET ERROR: Unsupported direction system '{target_lang}'. Use 'spanish' or 'english'.\n\n")
        except Exception as api_err:
            self.append_to_terminal(f" >> NETWORK TIMEOUT: Gateway request refused. Info: {api_err}\n\n")


if __name__ == "__main__":
    app = TerminalTranslator()
    app.mainloop()
          
