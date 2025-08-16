from src.window import Window
from src.frame import Frame
from src.button import Button
from src.assets import *

from pathlib import Path
from customtkinter import *
from tkinter.filedialog import askdirectory
import pyzipper

MASTER= Window(750, 500, "SaveFolder - Organizador de Arquivos", True)