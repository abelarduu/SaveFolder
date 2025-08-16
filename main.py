from src import *

class App:
    def __init__(self):
        """Inicializa a aplicação e define suas variaveis."""
        self.HEADER_FRAME = Frame(master=MASTER, fg_color="#158af0")
        self.HEADER_FRAME.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.MAIN_FRAME = Frame(master=MASTER, fg_color="#071F33")
        self.MAIN_FRAME.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.logo= CTkLabel(self.HEADER_FRAME, text="SaveFolder - Organizador de Arquivos")
        self.logo.grid(row=1, column=0, columnspan=3, padx= 15, pady=15)
        
        self.btn_select_folder = Button(self.HEADER_FRAME,'Selecionar Pasta', FOLDER_ICON, command= self.select_folder)
        self.btn_select_folder.grid(row=2, column=0, padx= 15, pady=15, sticky="nsew")
        self.btn_select_folder.toggle_state()
        
        self.btn_organize_folder = Button(self.HEADER_FRAME,'Organizar Pasta', FOLDER_ICON,command= self.organize_folder)
        self.btn_organize_folder.grid(row=2, column=1, padx= 15, pady=15,  sticky="nsew")


        self.btn_zip_folder = Button(self.HEADER_FRAME,'Compactar Pasta', ZIP_FOLDER_ICON, command= self.create_zip)
        self.btn_zip_folder.grid(row=2, column=2, padx= 15, pady=15, sticky="nsew")

        self.selected_folder = None
        
    def select_folder(self):
        """Seleciona uma pasta e atualiza a aplicação com as imagens dessa pasta."""
        folder = askdirectory()
        if Path(folder).is_dir():
            self.selected_folder = Path(folder)
        MASTER.after(10, self.render_folder)

    def render_folder(self):
        self.refresh_buttons()

    def organize_folder(self):
        """."""
        print("organizando a pasta")

    def create_zip(self):
        """Gera um arquivo .rar da pasta Compactada."""
        print("compactando a pasta")

    def add_zip_password(self):
        """Adiciona senha no arquivo compactado"""
        pass
    
    def refresh_buttons(self):
        if self.selected_folder is not None:
            self.btn_select_folder.toggle_state()
            self.btn_organize_folder.toggle_state()
            self.btn_zip_folder.toggle_state()
        else:
            self.btn_select_folder.toggle_state()
        
    def run(self):
        """Inicia a aplicação e mantém a interface em execução."""
        MASTER.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()