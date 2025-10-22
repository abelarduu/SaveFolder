from customtkinter import CTk, set_appearance_mode
from tkinter import messagebox

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

    def show_message(self, title: str, message: str):
        """Exibe uma caixa de diálogo de confirmação com título e mensagem."""
        messagebox.showinfo(title, message)