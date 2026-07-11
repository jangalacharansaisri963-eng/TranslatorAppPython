import customtkinter as ctk

class BaseTerminalApp(ctk.CTk):
    def __init__(self, title_name, syntax_hints, prompt_label):
        super().__init__()
        self.title(title_name)
        self.geometry("680x450")
        self.resizable(False, False)
        self.configure(fg_color="#000000")

        # Save prompt label internally so history logger can reference it
        self.prompt_text = prompt_label

        # FIXED: Removed insert_color here to prevent the CustomTkinter crash
        self.terminal_display = ctk.CTkTextbox(
            self, 
            font=ctk.CTkFont(family="Segoe UI", size=13), 
            fg_color="#000000", 
            text_color="#00FF33", 
            border_width=0, 
            corner_radius=0
        )
        self.terminal_display.pack(fill="both", expand=True, padx=15, pady=(15, 0))
        
        self.terminal_display.insert(
            "end", 
            f"====================================================================\n"
            f" {title_name.upper()}\n"
            f"====================================================================\n"
            f" {syntax_hints}\n"
            f"   - (func copy) -> Copies last output matrix\n\n"
        )

        # Bottom Entry Frame
        self.input_frame = ctk.CTkFrame(self, fg_color="#000000", corner_radius=0)
        self.input_frame.pack(fill="x", padx=15, pady=(0, 15))

        # Prompt dynamic text placement
        self.label_widget = ctk.CTkLabel(
            self.input_frame, 
            text=prompt_label, 
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), 
            text_color="#00FF33"
        )
        self.label_widget.pack(side="left")

        # CTkEntry safely supports insert_color, so this remains untouched
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
        self.command_entry.bind("<Return>", self.handle_input)

        # Shared clipboard cache state
        self.last_result = ""

    def handle_input(self, event=None):
        raw_cmd = self.command_entry.get().strip()
        self.command_entry.delete(0, "end")
        if not raw_cmd: 
            return
        
        self.terminal_display.insert("end", f"{self.prompt_text}{raw_cmd}\n")

        # Global System Command: Clear
        if raw_cmd.lower() in ["clear", "cls"]:
            self.terminal_display.delete("1.0", "end")
            return

        # Global System Command: Copy
        if raw_cmd.lower() == "(func copy)":
            if self.last_result:
                self.clipboard_clear()
                self.clipboard_append(self.last_result)
                self.terminal_display.insert("end", " >> SYSTEM NOTIFICATION: Last result copied to clipboard!\n\n")
            else:
                self.terminal_display.insert("end", " >> SYSTEM ERROR: Cache empty. Nothing to copy.\n\n")
            self.terminal_display.see("end")
            return

        # Pass execution control down to sub-module override block
        self.process_command(raw_cmd)
        self.terminal_display.see("end")

    def process_command(self, raw_cmd):
        """ Abstract hook method meant to be explicitly overridden by individual UI modules """
        pass
        
