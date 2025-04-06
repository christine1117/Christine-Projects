import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import os
import pygame
import sys

# 初始化主視窗
window = tk.Tk()
window.title("零壹咖啡師")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.attributes('-fullscreen', True)

# 全螢幕開關
window.bind('<Escape>', lambda event: window.attributes('-fullscreen', False))
window.bind('<f>', lambda event: window.attributes('-fullscreen', True))

# 初始化 pygame 音樂與音效
pygame.mixer.init()
click = pygame.mixer.Sound("audio/click4.wav")
radio = pygame.mixer.Sound("audio/radio9.wav")
pygame.mixer.music.load("audio/mah.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # 無限循環

# 音量控制變數
scale_value = 100

def set_volume(value):
    global scale_value
    scale_value = value
    volume = float(scale_value) / 100
    pygame.mixer.music.set_volume(volume)
    click.set_volume(volume)
    radio.set_volume(volume)

# 自動載入圖片

def load_images(directory="pics", size_normal=None, size_button=(43, 43), size_info=(33, 33)):
    img_dict = {}
    for file in os.listdir(directory):
        if file.endswith(".png"):
            name = os.path.splitext(file)[0]
            path = os.path.join(directory, file)
            if "info" in name:
                size = size_info
            elif any(kw in name for kw in ["arrow", "restart", "back"]):
                size = size_button
            else:
                size = size_normal
            image = Image.open(path).resize(size, Image.LANCZOS)
            img_dict[name] = ImageTk.PhotoImage(image)
    return img_dict

img_dict = load_images(size_normal=(screen_width, screen_height))

# 讀取資料集與圖片對應
image_names = [
    'esp', 'dou', 'ris', 'lun', 'ame', 'cap', 'fla', 'car', 'mac', 'dry',
    'lat', 'lai', 'rom', 'moc', 'pan', 'vie', 'bre', 'iri', 'aff', 'mar'
]
df = pd.read_csv('select.csv')
imgdf = pd.DataFrame()
imgdf["img"] = [img_dict.get(f"{i}-{name}") for i, name in enumerate(image_names)]
df = pd.concat([df, imgdf], axis=1)
filtered_df = 0
index = 0

def add_volume_slider():
    tk.Scale(window, from_=0, to=100, command=set_volume,
             orient='horizontal', length=100, width=7, sliderlength=20,
             showvalue=False, bd=0, bg="#2a3037", troughcolor='#68675e',
             activebackground='#fef9df', relief='flat',
             highlightbackground="#68675e", highlightcolor="#68675e").place(x=62, y=28)

def gui_choose():
    global filtered_df
    label_choose = tk.Label(window, image=img_dict["choose-7"])
    label_choose.image = img_dict["choose-7"]
    label_choose.place(x=0, y=0, relwidth=1, relheight=1)

    time = tk.IntVar()
    sweet = tk.IntVar()
    caffeine = tk.IntVar()
    milk = tk.IntVar()
    foam = tk.IntVar()
    cream = tk.IntVar()

    positions = [308, 363, 418, 473, 528, 583]
    variables = [time, sweet, caffeine, milk, foam, cream]
    values = [
        [2, 1, 0],
        [3, 2, 1, 0],
        [3, 2, 1, 0],
        [2, 1, 0],
        [2, 1, 0],
        [2, 1, 0]
    ]

    for i, (var, y, vals) in enumerate(zip(variables, positions, values)):
        x_start = 455
        x_gap = 265
        for j, val in enumerate(vals):
            tk.Radiobutton(window, text=" ", variable=var, value=val, indicatoron=0,
                           command=radio.play, selectcolor="blanchedalmond",
                           width=2, height=1).place(x=x_start + j * x_gap, y=y)

    def filter_coffee():
        click.play()
        selected = [v.get() for v in variables]
        global filtered_df
        filtered_df = df
        columns = ['time', 'sweetness', 'caffeine', 'milk', 'milk foam', 'fresh cream']
        for col, val in zip(columns, selected):
            if val:
                filtered_df = filtered_df[filtered_df[col] == val]
        if filtered_df.empty:
            gui_sorry()
        else:
            gui_list()

    tk.Button(window, text=' 教我調一杯 ', command=filter_coffee,
              font=("NotoSansTC", 20, "bold"), fg='#522A01', bg="blanchedalmond").place(x=650, y=670)

    add_volume_slider()

def gui_list():
    click.play()
    label_list = tk.Label(window, image=img_dict["list-2"])
    label_list.image = img_dict["list-2"]
    label_list.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Button(window, image=img_dict["restart"], command=gui_choose,
              bd=0, relief=tk.FLAT, highlightthickness=0).place(x=1320, y=700)

    for i in range(filtered_df.shape[0]):
        label = tk.Label(window, text=filtered_df.iat[i, 0], font=("NotoSansTC", 20, "bold"), anchor='w', padx=20,
                         fg="#522A01", bg="#fef9df", width=25, relief="flat")
        label.bind("<Button-1>", lambda e, i=i: gui_recipe(i))
        label.place(x=150 if i % 2 == 0 else 730, y=175 + (i // 2) * 50)

    add_volume_slider()

def gui_sorry():
    click.play()
    label_sorry = tk.Label(window, image=img_dict["sorry"])
    label_sorry.image = img_dict["sorry"]
    label_sorry.place(x=0, y=0, relwidth=1, relheight=1)
    tk.Button(window, text=' 重新調一杯 ', command=gui_choose,
              font=("NotoSansTC", 30, "bold"), fg="#522A01", bg="blanchedalmond").place(x=550, y=450)
    add_volume_slider()

def gui_recipe(i):
    global index
    index = i
    img_obj = filtered_df.iat[i, -1]
    label_recipe = tk.Label(window, image=img_obj)
    label_recipe.image = img_obj
    label_recipe.place(x=0, y=0, relwidth=1, relheight=1)

    def update_recipe(delta):
        nonlocal label_recipe
        global index
        index = (index + delta) % filtered_df.shape[0]
        new_img = filtered_df.iat[index, -1]
        label_recipe.config(image=new_img)
        label_recipe.image = new_img

    tk.Button(window, image=img_dict["left arrow"], command=lambda: update_recipe(-1),
              bd=0, relief=tk.FLAT, highlightthickness=0).place(x=165, y=718)
    tk.Button(window, image=img_dict["back to list"], command=gui_list,
              bd=0, relief=tk.FLAT, highlightthickness=0).place(x=225, y=718)
    tk.Button(window, image=img_dict["restart"], command=gui_choose,
              bd=0, relief=tk.FLAT, highlightthickness=0).place(x=285, y=718)
    tk.Button(window, image=img_dict["right arrow"], command=lambda: update_recipe(1),
              bd=0, relief=tk.FLAT, highlightthickness=0).place(x=345, y=718)

    add_volume_slider()

# 啟動 App
if __name__ == "__main__":
    gui_choose()
    window.mainloop()