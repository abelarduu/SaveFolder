from pathlib import Path
from customtkinter import CTkImage
from PIL import Image

ASSETS_PATH = Path(__file__).parent

def create_image(image_path):
    """Carrega e redimensiona uma imagem para uso com CTkImage."""
    img = Image.open(image_path)
    if img.size > (90, 90):
        size = (img.size[0] // 10, img.size[1] // 10)
    else:
        size = img.size
    return CTkImage(light_image=img, size=size)
 
#IMGs
FOLDER_ICON = create_image(ASSETS_PATH / "images/folder-icon.png")
ZIP_FOLDER_ICON = create_image(ASSETS_PATH / "images/zip-folder-icon.png")