from customtkinter import CTkButton

class Button(CTkButton):
    def __init__(self, master, txt, **kwargs):#img,
        super().__init__(master, text=txt, anchor="nsew",**kwargs)#image= img
        self.configure(height=90, anchor="center")