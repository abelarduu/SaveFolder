from customtkinter import CTkButton

class Button(CTkButton):
    def __init__(self, master, txt, img, **kwargs):
        super().__init__(master, text=txt, image= img, state="disabled", compound="top", anchor="nsew",**kwargs)
        self.configure(height=90, anchor="center")

    def toggle_state(self):
        state= self.cget("state")
        if state == "normal":
            self.configure(state="disabled")
        else:
            self.configure(state="normal")