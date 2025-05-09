# Copyrights
# olho_mouse_bg.pnh -> png images from pt.pngtree.com / Link for download https://pt.pngtree.com/freepng/scary-eyes-clipart-cartoon-monster-eye-with-spikes-vector_12157833.html
# olho_teclado_bg.pnh -> png images from Lovepik.com / Link for download https://pt.lovepik.com/graphics/png/

from tkinter import *
from PIL import Image, ImageTk
import pyautogui
import time
import threading
import sys

# Caminho da imagem de vidro trincado (ajuste para o caminho correto)
IMG_TRINCADA = "trincado_bg.png"
IMG_OLHO_MOUSE = "olho_mouse_bg.png"
IMG_OLHO_TECLADO = "olho_teclado_bg.png"

def sair(event=None):
    root.destroy()
    sys.exit()

# Fica mudando o mouse de posição
def mover_mouse():
    while True:
        x, y = pyautogui.position()
        screen_width, screen_height = pyautogui.size()

        # Movimento invertido: o mouse tenta ir para o lado oposto ao que foi movido
        target_x = screen_width - x
        target_y = screen_height - y
        pyautogui.moveTo(target_x, target_y, duration=0.1)

        time.sleep(0.1)

def start_mouve_mouse():
    thread = threading.Thread(target=mover_mouse)
    thread.daemon = True
    thread.start()

    time.sleep(2)  # tempo total da brincadeira

# ---------------------------- Janela principal --------------------------
root = Tk()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.configure(bg='black')
root.overrideredirect(True)
root.wm_attributes('-transparentcolor', 'black')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# ---------------------------- Janela com a imagem trincada --------------------------
# Carrega a imagem da tela trincada
img_trincada = Image.open(IMG_TRINCADA)
img_trincada = img_trincada.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
photo_trincada = ImageTk.PhotoImage(img_trincada)

label_trincada = Label(root, image=photo_trincada, bg='black')
label_trincada.image = photo_trincada
label_trincada.pack()

# ---------------------------- Janela com imagem de olho do mouse --------------------------
olho_mouse = Toplevel(root)
olho_mouse.attributes("-topmost", False)
olho_mouse.configure(bg='black')
olho_mouse.wm_attributes('-transparentcolor', 'black')
olho_mouse.overrideredirect(True)

img_mouse = Image.open(IMG_OLHO_MOUSE)
img_mouse = img_mouse.resize((
    int(img_mouse.width * 1.9),
    int(img_mouse.height * 1.9)
), Image.Resampling.LANCZOS)
photo_olho_mouse = ImageTk.PhotoImage(img_mouse)

img_width = photo_olho_mouse.width()
img_height = photo_olho_mouse.height()

# Calcula posição central
x = (screen_width - img_width) // 2
y = (screen_height - img_height) // 2

# Aplica posição
olho_mouse.geometry(f"{img_width}x{img_height}+{x + 30}+{y}")

label_mouse = Label(olho_mouse, image=photo_olho_mouse, bg='black')
label_mouse.image = photo_olho_mouse
label_mouse.pack()

# ---------------------------- Janela com imagem de olho do teclado --------------------------
olho_mouse = Toplevel(root)
olho_mouse.attributes("-topmost", False)
olho_mouse.configure(bg='black')
olho_mouse.wm_attributes('-transparentcolor', 'black')
olho_mouse.overrideredirect(True)

img_mouse = Image.open(IMG_OLHO_MOUSE)
img_mouse = img_mouse.resize((
    int(img_mouse.width * 1.9),
    int(img_mouse.height * 1.9)
), Image.Resampling.LANCZOS)
photo_olho_mouse = ImageTk.PhotoImage(img_mouse)

img_width = photo_olho_mouse.width()
img_height = photo_olho_mouse.height()

# Calcula posição central
x = (screen_width - img_width) // 2
y = (screen_height - img_height) // 2

# Aplica posição
olho_mouse.geometry(f"{img_width}x{img_height}+{x + 30}+{y}")

label_mouse = Label(olho_mouse, image=photo_olho_mouse, bg='black')
label_mouse.image = photo_olho_mouse
label_mouse.pack()

# ---------------------------- Mostra as telas --------------------------

# Fecha com ESC ou após 5 segundos
root.bind("<Escape>", sair)

olho_mouse.after(2000, olho_mouse.withdraw)

olho_mouse.after(4000, olho_mouse.deiconify)

root.lift()
root.after(10000, sair)

root.mainloop()