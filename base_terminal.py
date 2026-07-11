import customtkinter as ctk
from abc import ABC, abstractmethod

class BaseTerminalApp(ctk.CTk, ABC):
    def __init__(self, title_name, syntax_hints, prompt_label):
        super().__init__()
        self.title(title_name)
        self.geometry("680x450")
        self.resizable(False, False)
        self.configure(fg_color="#000000")

        self.prompt_text = prompt_label
        self.last_result = ""

        # Main Display
        self.terminal_display = ctk.CTkTextbox(
            self, font=("Segoe UI", 13), fg_color="#000000", 
            text_color="#00FF33", border_width=0, corner_radius=0
        )
        self.terminal_display.pack(fill="both", expand=True, padx=15, pady=(15, 0))
        
        self.terminal_display.insert("1.0", f"=== {title_name.upper()} ===\n{syntax_hints}\n\n")

        # Bottom Input Area
        self.input_frame = ctk.CTkFrame(self, fg_color="#000000", corner_radius=0)
        self.input_frame.pack(fill="x", padx=15, pady=(0, 15))

        ctk.CTkLabel(self.input_frame, text=prompt_label, font=("Segoe UI", 13, "bold"), 
                     text_color="#00FF33").pack(side="left")

        self.command_entry = ctk.CTkEntry(
            self.input_frame, font=("Segoe UI", 13), fg_color="#000000", 
            text_color="#ffffff", border_width=1, border_color="#00FF33", 
            insert_color="#00FF33", corner_radius=0
        )
        self.command_entry.pack(side="left", fill="x", expand=True)
        self.command_entry.bind("<Return>", self.handle_input)
        self.command_entry.focus_set()

    def handle_input(self, event=None):
        cmd = self.command_entry.get().strip()
        self.command_entry.delete(0, "end")
        if not cmd: return
        
        self.terminal_display.insert("end", f"{self.prompt_text}{cmd}\n")

        if cmd.lower() in ["clear", "cls"]:
            self.terminal_display.delete("1.0", "end")
        elif cmd.lower() == "(func copy)":
            if self.last_result:
                self.clipboard_clear()
                self.clipboard_append(self.last_result)
                self.terminal_display.insert("end", " >> SUCCESS: Copied to clipboard\n\n")
            else:
                self.terminal_display.insert("end", " >> ERROR: Cache empty\n\n")
        else:
            self.process_command(cmd)
        
        self.terminal_display.see("end")

    @abstractmethod
    def process_command(self, raw_cmd):
        """Logic bridge to main_terminal_app.py"""
        pass
        
