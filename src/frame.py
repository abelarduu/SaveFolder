from customtkinter import CTkFrame, CTkScrollableFrame

class Frame:
    def __new__(cls, master, scroll= False, **kwargs):
        if scroll:
            widget = CTkScrollableFrame(master, **kwargs)
        else:
            widget = CTkFrame(master, **kwargs)
        widget.columnconfigure(1, weight=3)

        return widget