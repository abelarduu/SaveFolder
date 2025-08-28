from customtkinter import CTk, set_appearance_mode

class Window(CTk):
    def __init__(self, width: int, height: int, title: str, resizable: bool):
        """Inicializa uma janela personalizada com largura, altura, título e redimensionamento."""
        super().__init__()
        self.title(title)
        self.minsize(width, height)
        self.resizable(resizable, resizable)
        set_appearance_mode("dark")
        
        # Configura o gerenciamento de layout para expansão
        self.columnconfigure(1, weight=5)
        self.rowconfigure(1, weight=5)

        def set_theme(self):
            """Alterna entre os temas da interface."""
            pass

        def show_confirmation_dialog(self):
            """."""
            pass