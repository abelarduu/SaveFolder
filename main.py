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
        
        # atualiza/Limpa os arquivos da tela
        self.clear_files_display()
        MASTER.after(10, self.render_folder)

    def clear_files_display(self):
        """Remove os arquivos do MAIN_FRAME e limpa a lista de arquivos."""
        self.list_files.clear()
        for widget in self.MAIN_FRAME.winfo_children():
            if isinstance(widget, CTkLabel):
                widget.destroy()

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
                            font=("Arial", 20))
            
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
                if (file.is_file() 
                    and  file.name != 'desktop.ini'):
                    #Criação de pastas
                    new_dir = file.parent / file.suffix[1:]
                    new_dir.mkdir(exist_ok=True)
                    
                    #Move o arquivo
                    new_path = new_dir/ file.name 
                    file.replace(new_path)

        self.btn_organize_folder.toggle_state()
        MASTER.show_message("Organizar Pasta", "A pasta foi organizada com sucesso!")
        MASTER.after(1000, self.render_folder)
            
    def create_zip(self):
        """Compacta a pasta selecionada em um arquivo .zip com criptografia AES."""

        zip_path = self.selected_folder / f'{self.selected_folder.name}.zip'
        zip_password = self.ask_zip_password()
        if zip_password:
            encryption = pyzipper.WZ_AES
        else:
            encryption = None
        
        # Cria o arquivo ZIP criptografado com AES e compressão LZMA
        with pyzipper.AESZipFile(
            zip_path,
            'w',
            compression= pyzipper.ZIP_LZMA,
            encryption= encryption
        ) as zf:
            
            # Se Definiu uma senha foi defenida criptografia do arquivo
            # adiciona senha com criptografia AES no arquivo compactado  
            if zip_password:
                zf.setpassword(zip_password)

            # Define o nome base da pasta dentro do arquivo ZIP
            base_folder = self.selected_folder.name

            # Percorre todos os arquivos dentro da pasta selecionada
            # e adiciona cada arquivo ao arquivo ZIP
            for file_path in self.selected_folder.rglob('*'):

                if (file_path.is_file() 
                    and file_path.name != 'desktop.ini'
                    and file_path != zip_path):
                    arcname = Path(base_folder) / file_path.relative_to(self.selected_folder)
                    zf.write(file_path, arcname)

            self.btn_zip_folder.toggle_state()
            MASTER.show_message("Compactar Pasta", "A pasta foi compactada com criptografia AES com sucesso!")

    def ask_zip_password(self) -> bytes | None:
        """Obtem e retorna a senha definida em bytes se o usuário quiser proteger o .ZIP."""
        is_password_protected = askyesno("Adicionar senha", "Deseja proteger o ZIP com senha? 🔒")

        if is_password_protected:
            # Obtem a senha e converte em numeros binarios
            dialog = CTkInputDialog(text="Defina a senha:", title="Adicionar senha")
            password = dialog.get_input().encode('utf-8') 
            if password:
                return password
        return None
    
    def refresh_buttons(self):
        """Atualiza o estado dos botões de ação."""
        if self.selected_folder is not None:
            self.btn_organize_folder.configure(state="normal")
            self.btn_zip_folder.configure(state="normal")
    
    def run(self):
        """Inicia o loop principal da aplicação."""
        MASTER.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()