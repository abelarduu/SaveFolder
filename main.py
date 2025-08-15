from src import *

class App:
    def __init__(self):
        """Inicializa a aplicação e define suas variaveis."""
        HEADER_FRAME = Frame(master=MASTER, fg_color="#158af0")
        HEADER_FRAME.grid(row=0, column=0, columnspan=3, sticky="nsew")

        MAIN_FRAME = Frame(master=MASTER, fg_color="#071F33")
        MAIN_FRAME.grid(row=1, column=0, columnspan=3, sticky="nsew")

        logo= CTkLabel(HEADER_FRAME, text="SaveFolder - Organizador de Arquivos")
        logo.grid(row=1, column=0, columnspan=3, padx= 15, pady=15)
        
        btn_select_folder = Button(HEADER_FRAME,'Selecionar Pasta', FOLDER_ICON, command= self.select_folder)
        btn_select_folder.grid(row=2, column=0, padx= 15, pady=15, sticky="nsew")
        
        btn_organize_folder = Button(HEADER_FRAME,'Organizar Pasta', FOLDER_ICON, command= self.organize_folder)
        btn_organize_folder.grid(row=2, column=1, padx= 15, pady=15, sticky="nsew")

        btn_zip_folder = Button(HEADER_FRAME,'Compactar Pasta', ZIP_FOLDER_ICON, command= self.create_zip)
        btn_zip_folder.grid(row=2, column=2, padx= 15, pady=15, sticky="nsew")
        
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