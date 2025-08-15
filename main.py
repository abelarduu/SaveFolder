from src import *

class App:
    def __init__(self):
        """Inicializa a aplicação e define suas variaveis."""
        HEADER_FRAME = Frame(master=MASTER, fg_color="#158af0")
        HEADER_FRAME.grid(row=0, column=0, columnspan=3, sticky="nsew")

        MAIN_FRAME = Frame(master=MASTER, fg_color="#071F33")
        MAIN_FRAME.grid(row=1, column=0, columnspan=3, sticky="nsew")
        
    def select_folder(self):
        """."""
        print("selecione a pasta")

    def organize_folder(self):
        """."""
        print("organizando a pasta")

    def create_zip(self):
        """Gera um arquivo .rar da pasta Compactada."""
        print("compactando a pasta")

    def add_zip_password(self):
        """Adiciona senha n"""
        pass
    
    def run(self):
        """Inicia a aplicação e mantém a interface em execução."""
        MASTER.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()