# Copyrights
# olho_mouse_bg.pnh -> png images from pt.pngtree.com / Link for download https://pt.pngtree.com/freepng/scary-eyes-clipart-cartoon-monster-eye-with-spikes-vector_12157833.html
# olho_teclado_bg.pnh -> png images from Lovepik.com / Link for download https://pt.lovepik.com/graphics/png/

from tkinter import *
from PIL import Image, ImageTk
import pyautogui
import time
import threading
import sys
import pygame

# Caminho da imagem de vidro trincado (ajuste para o caminho correto)
IMG_TRINCADA = "images/trincado_bg.png"
IMG_OLHO_MOUSE = "images/olho_mouse_bg.png"
IMG_OLHO_TECLADO = "images/olho_teclado_bg.png"
IMG_ERRO = "images/erro.png"

def sair(event=None):
    root.destroy()
    root.quit()
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

# Começa a função de trocar o mouse
def start_mouve_mouse():
    thread = threading.Thread(target=mover_mouse)
    thread.daemon = True
    thread.start()

    time.sleep(1.5)  # tempo total da brincadeira

# Começa a trocar a música
def start_music():
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/suspense-background.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=-1)

# Para de tocar a música
def stop_music():
    pygame.mixer.music.stop()

def play_effect(path_effect, nivel = 1):
    pygame.mixer.init()
    audio = pygame.mixer.Sound(path_effect)
    audio.set_volume(nivel)
    audio.play()

def fade_in(window, delay=0, step=0.05):
    def _fade():
        alpha = window.attributes("-alpha")
        if alpha < 1:
            alpha = min(alpha + step, 1)
            window.attributes("-alpha", alpha)
            window.after(50, _fade)
    window.attributes("-alpha", 0.0)
    window.deiconify()
    window.after(delay, _fade)

def start_presentation():
    root.after(1000, start_music)
    root.after(3000, lambda: fade_in(olho_mouse, 50))
    root.after(3000, lambda:  play_effect("sounds/voices_tratadas/mouse_1.wav", 1))
    root.after(11100, lambda: play_effect("sounds/voices_tratadas/mouse_2.wav", 1))
    root.after(21800, lambda: fade_out(olho_mouse, 50))
    root.after(21800, lambda: fade_in(olho_teclado, 50))
    root.after(21800, lambda: play_effect("sounds/voices_tratadas/teclado_1.wav", 1))
    root.after(26800, lambda: play_effect("sounds/voices_tratadas/teclado_2.wav", 1))
    root.after(39300, lambda: fade_out(olho_teclado, 50))
    root.after(39300, lambda: fade_in(olho_mouse, 50))
    root.after(39300, lambda: play_effect("sounds/voices_tratadas/mouse_3.wav", 1))
    root.after(46800, lambda: fade_out(olho_mouse, 50))
    root.after(46800, lambda: fade_in(olho_teclado, 50))
    root.after(46800, lambda: play_effect("sounds/voices_tratadas/teclado_3.wav", 1))
    root.after(56200, lambda: fade_out(olho_teclado, 50))
    root.after(56200, lambda: play_effect("sounds/voices_tratadas/guarda_1.wav", 1))
    root.after(60200, lambda: fade_in(olho_mouse, 50))
    root.after(60200, lambda: play_effect("sounds/voices_tratadas/mouse_4.wav", 1))
    root.after(65900, lambda: fade_out(olho_mouse, 50))
    root.after(65900, lambda: fade_in(olho_teclado, 50))
    root.after(65900, lambda: play_effect("sounds/voices_tratadas/teclado_4.wav", 1))
    root.after(67600, lambda: fade_out(olho_teclado, 50))
    root.after(67600, lambda: play_effect("sounds/voices_tratadas/guarda_2.wav", 1))

    root.after(71600, lambda: root.withdraw())
    root.after(71601, lambda: play_effect("sounds/windows-erro.wav", 0.7))
    root.after(72601, lambda: tela_erro.deiconify())
    root.after(73000, lambda: stop_music())
    

def end_presentation():
    sair()

def fade_out(window, delay=0, step=0.05):
    def _fade():
        alpha = window.attributes("-alpha")
        if alpha > 0:
            alpha = max(alpha - step, 0)
            window.attributes("-alpha", alpha)
            window.after(50, _fade)
        else:
            window.withdraw()
    window.attributes("-alpha", 1.0)
    window.after(delay, _fade)

# ---------------------------- Janela principal --------------------------
root = Tk()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.configure(bg='black')
root.overrideredirect(True)
root.wm_attributes('-transparentcolor', 'black')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

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
olho_mouse.withdraw()

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
olho_teclado = Toplevel(root)
olho_teclado.attributes("-topmost", False)
olho_teclado.configure(bg='black')
olho_teclado.wm_attributes('-transparentcolor', 'black')
olho_teclado.overrideredirect(True)
olho_teclado.withdraw()

img_teclado = Image.open(IMG_OLHO_TECLADO)
photo_olho_teclado = ImageTk.PhotoImage(img_teclado)

img_width = photo_olho_teclado.width()
img_height = photo_olho_teclado.height()

# Calcula posição central
x = (screen_width - img_width) // 2
y = (screen_height - img_height) // 2

# Aplica posição
olho_teclado.geometry(f"{img_width}x{img_height}+{x + 30}+{y}")

label_teclado = Label(olho_teclado, image=photo_olho_teclado, bg='black')
label_teclado.image = photo_olho_teclado
label_teclado.pack()

# ---------------------------- Janela de erro --------------------------
tela_erro = Toplevel(root)
tela_erro.attributes("-topmost", True)
tela_erro.configure(bg='black')
tela_erro.wm_attributes('-transparentcolor', 'black')
tela_erro.overrideredirect(True)
tela_erro.withdraw()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

img_erro = Image.open(IMG_ERRO)
img_erro = img_erro.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
photo_erro = ImageTk.PhotoImage(img_erro)

label_erro = Label(tela_erro, image=photo_erro, bg='black')
label_erro.image = photo_erro
label_erro.pack()

# ---------------------------- Mostra as telas --------------------------
root.after(0, lambda: play_effect("sounds/glass-break.wav"))
root.after(0, start_presentation)

root.after(80600, end_presentation)

root.mainloop()