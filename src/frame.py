from customtkinter import CTkFrame

class Frame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configura o gerenciamento de layout para expansão
        self.columnconfigure(1, weight=3) 
        self.rowconfigure(1, weight=3)