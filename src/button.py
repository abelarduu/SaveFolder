from customtkinter import CTkButton

class Button(CTkButton):
    def __init__(self, master, txt, img, **kwargs):
        super().__init__(master, text=txt, image= img, compound="top", anchor="nsew",**kwargs)
        self.configure(height=90, anchor="center")