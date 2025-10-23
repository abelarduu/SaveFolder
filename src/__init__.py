from src.window import Window
from src.frame import Frame
from src.button import Button
from src.assets import *

from pathlib import Path
from customtkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno
import pyzipper

MASTER= Window(width=750,
               height=500,
               title="SaveFolder - Organizador de Arquivos",
               resizable=True)