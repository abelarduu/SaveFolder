from src import *

class App:
    def __init__(self):
        """Inicializa a aplicação e define suas variaveis."""
        self.HEADER_FRAME = Frame(master=MASTER,
                                  fg_color="#056CF2")
        self.HEADER_FRAME.grid(row=0,
                               column=0,
                               columnspan=3,
                               sticky="nsew")

        self.MAIN_FRAME = Frame(master=MASTER,
                                scroll= True,
                                fg_color="#071F33")
        self.MAIN_FRAME.grid(row=1,
                             column=0,
                             columnspan=3,
                             sticky="nsew")

        self.logo= CTkLabel(self.HEADER_FRAME,
                            text="SaveFolder - Organizador de Arquivos")
        self.logo.grid(row=1,
                       column=0,
                       columnspan=3,
                       padx= 15,
                       pady=15)
        
        self.btn_select_folder = Button(self.HEADER_FRAME,
                                        'Selecionar Pasta',
                                        FOLDER_ICON,
                                        command= self.select_folder)
        self.btn_select_folder.grid(row=2,
                                    column=0,
                                    padx= 15,
                                    pady=15,
                                    sticky="nsew")
        self.btn_select_folder.toggle_state()
        
        self.btn_organize_folder = Button(self.HEADER_FRAME,
                                          'Organizar Pasta',
                                          FOLDER_ICON,
                                          command= self.organize_folder)
        self.btn_organize_folder.grid(row=2,
                                      column=1,
                                      padx= 15,
                                      pady=15,
                                      sticky="nsew")

        self.btn_zip_folder = Button(self.HEADER_FRAME,
                                     'Compactar Pasta',
                                     ZIP_FOLDER_ICON,
                                     command= self.create_zip)
        self.btn_zip_folder.grid(row=2,
                                 column=2,
                                 padx= 15,
                                 pady=15,
                                 sticky="nsew")

        self.selected_folder : Path
        self.list_files= []
        
    def select_folder(self):
        """Abre o seletor de pastas e define a pasta escolhida."""
        folder = askdirectory()
        if Path(folder).is_dir():
            self.selected_folder = Path(folder)
        MASTER.after(10, self.render_folder)

    def get_list_files(self):
        """Carrega os arquivos do diretório selecionado na lista."""
        for file in self.selected_folder.glob("*"):
            self.list_files.append(file)

    def set_file_icon(self, label, file):
        """Define o ícone do label de acordo com a extensão do arquivo."""
        if (".docx" in Path(file).suffix or
            ".odt" in Path(file).suffix):
            label.configure(image= DOCX_FILE_ICON)

        elif ".pdf" in Path(file).suffix:
            label.configure(image= PDF_FILE_ICON)
        
        else:
            label.configure(image= TXT_FILE_ICON)
            
    def render_folder(self):
        """Renderiza os arquivos da pasta selecionada no frame principal."""
        self.refresh_buttons()
        self.get_list_files()

        for index, file in enumerate(self.list_files):
            label= CTkLabel(self.MAIN_FRAME,
                            text= " " + str(file),
                            compound= "left",
                            fg_color="#2f4a59",
                            corner_radius= 25,
                            font=("Arial", 15))
            
            self.set_file_icon(label, file)

            label.grid(row= index,
                       column= 0,
                       columnspan=3,
                       pady=15,
                       sticky="ns")

    def organize_folder(self):
        """Organiza os arquivos da pasta selecionada."""
        if not self.list_files is None:
            for file in self.list_files:

                #Criação de pastas
                new_dir = file.parent / Path(file.suffix[1:])
                new_dir.mkdir(exist_ok=True)
                
                #Move o arquivo
                new_path = new_dir / self.selected_folder.name 
                file.replace(new_path)

    def create_zip(self):
        """Compacta a pasta selecionada em um arquivo .zip com criptografia AES."""
        secret_password = b'admin123'

        # Cria o arquivo ZIP criptografado com AES e compressão LZMA
        with pyzipper.AESZipFile(
            f'{self.selected_folder.name}.zip',
            'w',
            compression=pyzipper.ZIP_LZMA,
            encryption=pyzipper.WZ_AES
        ) as zf:
            
            # Define a senha para o arquivo compactado com criptografia AES 
            zf.setpassword(secret_password)

            # Define o nome base da pasta dentro do arquivo ZIP
            base_folder = self.selected_folder.name

            # Percorre todos os arquivos dentro da pasta selecionada
            # e adiciona cada arquivo ao arquivo ZIP
            for file_path in self.selected_folder.rglob('*'):
                if file_path.is_file():
                    arcname = Path(base_folder) / file_path.relative_to(self.selected_folder)
                    zf.write(file_path, arcname)

    def refresh_buttons(self):
        """Atualiza o estado dos botões de ação."""
        if self.selected_folder is not None:
            self.btn_select_folder.toggle_state()
            self.btn_organize_folder.toggle_state()
            self.btn_zip_folder.toggle_state()
        else:
            self.btn_select_folder.toggle_state()
        
    def run(self):
        """Inicia o loop principal da aplicação."""
        MASTER.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()