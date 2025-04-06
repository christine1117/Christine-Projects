import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
import pygame
import os
import sys

window = tk.Tk()
window.title("零壹咖啡師")
window.geometry("1920x1200")

#全螢幕模式與關閉視窗
#region
window.attributes('-fullscreen', True)

label = tk.Label(window, text="這是全螢幕顯示", font=("Arial", 24))
label.pack(expand=True)

def close_window():
    window.destroy()

window.protocol("WM_DELETE_WINDOW", close_window)

window.bind("<Escape>", lambda event: close_window())
#endregion

# 用 pillow 套件載入圖片 
#region
#非食譜
img_choose = Image.open("pics/choose-7.png")
img_list = Image.open("pics/list-2.png")
img_sorry = Image.open("pics/sorry.png") 
#食譜
img_0_esp = Image.open("pics/0-esp.png")
img_1_dou = Image.open("pics/1-dou.png")
img_2_ris = Image.open("pics/2-ris.png")
img_3_lun = Image.open("pics/3-lun.png")
img_4_ame = Image.open("pics/4-ame.png")
img_5_cap = Image.open("pics/5-cap.png")
img_6_fla = Image.open("pics/6-fla.png")
img_7_car = Image.open("pics/7-car.png")
img_8_mac = Image.open("pics/8-mac.png")
img_9_dry = Image.open("pics/9-dry.png")
img_10_lat = Image.open("pics/10-lat.png")
img_11_lai = Image.open("pics/11-lai.png")
img_12_rom = Image.open("pics/12-rom.png")
img_13_moc = Image.open("pics/13-moc.png")
img_14_pan = Image.open("pics/14-pan.png")
img_15_vie = Image.open("pics/15-vie.png")
img_16_bre = Image.open("pics/16-bre.png")
img_17_iri = Image.open("pics/17-iri.png")
img_18_aff = Image.open("pics/18-aff.png")
img_19_mar = Image.open("pics/19-mar.png")
img_0x_esp = Image.open("pics/0x-esp.png")
img_1x_dou = Image.open("pics/1x-dou.png")
#endregion

#按鈕圖
img_left_arrow = Image.open("pics/left arrow.png")
img_right_arrow = Image.open("pics/right arrow.png")
img_resart = Image.open("pics/restart.png")
img_resart2 = Image.open("pics/restart2.png")
img_backtolist = Image.open("pics/back to list.png")
img_info = Image.open("pics/info.png")
img_backtocof = Image.open("pics/back to cof.png")
img_result = Image.open("pics/result.png")


# pil圖片變更大小 
#region
#非食譜
img_choose = img_choose.resize((2133, 1200), Image.LANCZOS)
img_list = img_list.resize((1537, 867), Image.LANCZOS)
img_sorry = img_sorry.resize((1537, 867), Image.LANCZOS)
#食譜
img_0_esp = img_0_esp.resize((1537, 867), Image.LANCZOS)
img_1_dou = img_1_dou.resize((1537, 867), Image.LANCZOS)
img_2_ris = img_2_ris.resize((1537, 867), Image.LANCZOS)
img_3_lun = img_3_lun.resize((1537, 867), Image.LANCZOS)
img_4_ame = img_4_ame.resize((1537, 867), Image.LANCZOS)
img_5_cap = img_5_cap.resize((1537, 867), Image.LANCZOS)
img_6_fla = img_6_fla.resize((1537, 867), Image.LANCZOS)
img_7_car = img_7_car.resize((1537, 867), Image.LANCZOS)
img_8_mac = img_8_mac.resize((1537, 867), Image.LANCZOS)
img_9_dry = img_9_dry.resize((1537, 867), Image.LANCZOS)
img_10_lat = img_10_lat.resize((1537, 867), Image.LANCZOS)
img_11_lai = img_11_lai.resize((1537, 867), Image.LANCZOS)
img_12_rom = img_12_rom.resize((1537, 867), Image.LANCZOS)
img_13_moc = img_13_moc.resize((1537, 867), Image.LANCZOS)
img_14_pan = img_14_pan.resize((1537, 867), Image.LANCZOS)
img_15_vie = img_15_vie.resize((1537, 867), Image.LANCZOS)
img_16_bre = img_16_bre.resize((1537, 867), Image.LANCZOS)
img_17_iri = img_17_iri.resize((1537, 867), Image.LANCZOS)
img_18_aff = img_18_aff.resize((1537, 867), Image.LANCZOS)
img_19_mar = img_19_mar.resize((1537, 867), Image.LANCZOS)
img_0x_esp = img_0x_esp.resize((1537, 867), Image.LANCZOS)
img_1x_dou = img_1x_dou.resize((1537, 867), Image.LANCZOS)
#endregion

#按鈕圖
img_left_arrow = img_left_arrow.resize((43, 43), Image.LANCZOS)
img_right_arrow = img_right_arrow.resize((43, 43), Image.LANCZOS)
img_resart = img_resart.resize((43, 43), Image.LANCZOS)
img_resart2 = img_resart2.resize((60, 60), Image.LANCZOS)
img_backtolist = img_backtolist.resize((43, 43), Image.LANCZOS)
img_backtocof = img_backtocof.resize((43, 43), Image.LANCZOS)
img_info = img_info.resize((33, 33), Image.LANCZOS)
img_result = img_result.resize((387, 103), Image.LANCZOS)


# 將pil載入的圖片轉換成TK可接受的模式 
#region
#非食譜
img_choose = ImageTk.PhotoImage(img_choose)
img_list = ImageTk.PhotoImage(img_list)
img_sorry = ImageTk.PhotoImage(img_sorry)
#食譜
img_0_esp = ImageTk.PhotoImage(img_0_esp)
img_1_dou = ImageTk.PhotoImage(img_1_dou)
img_2_ris = ImageTk.PhotoImage(img_2_ris)
img_3_lun = ImageTk.PhotoImage(img_3_lun)
img_4_ame = ImageTk.PhotoImage(img_4_ame)
img_5_cap = ImageTk.PhotoImage(img_5_cap)
img_6_fla = ImageTk.PhotoImage(img_6_fla)
img_7_car = ImageTk.PhotoImage(img_7_car)
img_8_mac = ImageTk.PhotoImage(img_8_mac)
img_9_dry = ImageTk.PhotoImage(img_9_dry)
img_10_lat = ImageTk.PhotoImage(img_10_lat)
img_11_lai = ImageTk.PhotoImage(img_11_lai)
img_12_rom = ImageTk.PhotoImage(img_12_rom)
img_13_moc = ImageTk.PhotoImage(img_13_moc)
img_14_pan = ImageTk.PhotoImage(img_14_pan)
img_15_vie = ImageTk.PhotoImage(img_15_vie)
img_16_bre = ImageTk.PhotoImage(img_16_bre)
img_17_iri = ImageTk.PhotoImage(img_17_iri)
img_18_aff = ImageTk.PhotoImage(img_18_aff)
img_19_mar = ImageTk.PhotoImage(img_19_mar)
img_0x_esp = ImageTk.PhotoImage(img_0x_esp)
img_1x_dou = ImageTk.PhotoImage(img_1x_dou)
#按鈕圖
img_left_arrow = ImageTk.PhotoImage(img_left_arrow)
img_right_arrow = ImageTk.PhotoImage(img_right_arrow)
img_resart = ImageTk.PhotoImage(img_resart)
img_resart2 = ImageTk.PhotoImage(img_resart2)
img_backtolist = ImageTk.PhotoImage(img_backtolist)
img_info = ImageTk.PhotoImage(img_info)
img_backtocof = ImageTk.PhotoImage(img_backtocof)
img_result = ImageTk.PhotoImage(img_result)
#endregion

# Dataframe處理
#region
list_img_coffee = [
    img_0_esp,
    img_1_dou,
    img_2_ris,
    img_3_lun,
    img_4_ame,
    img_5_cap,
    img_6_fla,
    img_7_car,
    img_8_mac,
    img_9_dry,
    img_10_lat,
    img_11_lai,
    img_12_rom, 
    img_13_moc,
    img_14_pan, 
    img_15_vie, 
    img_16_bre, 
    img_17_iri, 
    img_18_aff, 
    img_19_mar 
]
df = pd.read_csv('select.csv', encoding='Big5')
imgdf = pd.DataFrame()
imgdf['img'] = list_img_coffee
df = pd.concat([df, imgdf], axis=1)
#endregion

# pygame 載入音效
#region
pygame.mixer.init()

# 按鈕音效
click = pygame.mixer.Sound("audio/click4.wav")
start_click = 'off'
radio = pygame.mixer.Sound("audio/radio9.wav")

# 背景音樂
pygame.mixer.music.load("audio/mah.mp3")

# 音量控制 Function
scale_value = 100

def set_volume(value): 
    global scale_value
    scale_value = value
    volume = float(scale_value) / 100
    pygame.mixer.music.set_volume(volume)
    click.set_volume(volume)
    radio.set_volume(volume)
#endregion

# 字體
#region
program_path = os.path.dirname(sys.path[0])
font_file = "NotoSansTC-Bold.otf"
font_path = os.path.join(program_path, font_file)
#endregion

# 頁面 function
#region
def gui_choose():

    global start_click
    if start_click == 'on':
        click.play()
    else:
        start_click = 'on'
    
    label_choose = tk.Label(window, image=img_choose)
    label_choose.place(x=0, y=0, relwidth=1, relheight=1)

    # Radiobuttons
    #region
    time = tk.IntVar()
    tk.Radiobutton(window,text=" ",variable=time,value=2,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=455,y=308)
    tk.Radiobutton(window,text=" ",variable=time,value=1,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=720,y=308)
    tk.Radiobutton(window,text=" ",variable=time,value=0,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=1220,y=308)

    sweet = tk.IntVar()
    tk.Radiobutton(window,text=" ",variable=sweet,value=3,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=455,y=363)
    tk.Radiobutton(window,text=" ",variable=sweet,value=2,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=720,y=363)
    tk.Radiobutton(window,text=" ",variable=sweet,value=1,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=990,y=363)
    tk.Radiobutton(window,text=" ",variable=sweet,value=0,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=1220,y=363)

    caffeine= tk.IntVar()
    tk.Radiobutton(window,text=" ",variable=caffeine,value=3,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=455,y=418)
    tk.Radiobutton(window,text=" ",variable=caffeine,value=2,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=720,y=418)
    tk.Radiobutton(window,text=" ",variable=caffeine,value=1,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=990,y=418)
    tk.Radiobutton(window,text=" ",variable=caffeine,value=0,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=1220,y=418)

    milk= tk.IntVar()
    tk.Radiobutton(window,text=" ",variable=milk,value=2,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=455,y=473)
    tk.Radiobutton(window,text=" ",variable=milk,value=1,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=720,y=473)
    tk.Radiobutton(window,text=" ",variable=milk,value=0,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=1220,y=473)

    foam= tk.IntVar()
    tk.Radiobutton(window,text=" ",variable=foam,value=2,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=455,y=528)
    tk.Radiobutton(window,text=" ",variable=foam,value=1,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=720,y=528)
    tk.Radiobutton(window,text=" ",variable=foam,value=0,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=1220,y=528)

    cream= tk.IntVar()
    tk.Radiobutton(window,text=" ",variable=cream,value=2,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=455,y=583)
    tk.Radiobutton(window,text=" ",variable=cream,value=1,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=720,y=583)
    tk.Radiobutton(window,text=" ",variable=cream,value=0,command=radio.play, indicatoron=0,selectcolor="#ecd7b1",width=2,height=1).place(x=1220,y=583)
    #endregion
    
    # filter function
    def filter_coffee():
        click.play()
        selected_time = time.get()
        selected_sweetness = sweet.get()
        selected_caffeine = caffeine.get()
        selected_milk = milk.get()
        selected_foam = foam.get()
        selected_whipped_cream = cream.get()
        
        global filtered_df #很重要的資料
        filtered_df=df
        
        if selected_time:
            filtered_df = filtered_df[filtered_df['time'] == selected_time]
            
        if selected_sweetness:
            filtered_df = filtered_df[filtered_df['sweetness'] == selected_sweetness]
            
        if selected_caffeine:
            filtered_df = filtered_df[filtered_df['caffeine'] == selected_caffeine]
            
        if selected_milk:
            filtered_df = filtered_df[filtered_df['milk'] == selected_milk]
        
        if selected_foam:
            filtered_df = filtered_df[filtered_df['milk foam'] == selected_foam]
        
        if selected_whipped_cream:
            filtered_df = filtered_df[filtered_df['fresh cream'] == selected_whipped_cream]
        
        if filtered_df.empty:
            gui_sorry()
        else:
            gui_list()

    # Button choose
    button_result = tk.Button(window, image=img_result, command=filter_coffee, 
                              bd=0, relief=tk.FLAT, highlightthickness=0)
    button_result.place(x=579,y=693)

    # Scale choose
    #region
    volume_scale = tk.Scale(window, from_=0, to=100, command=set_volume,
                            orient='horizontal', length=100, width=7, sliderlength=20,
                            sliderrelief='flat', showvalue=False, bd=0,
                            bg="#2a3037", troughcolor='#68675e', activebackground='#fef9df', relief='flat',
                            highlightbackground="#68675e", highlightcolor="#68675e")
    volume_scale.set(scale_value)
    volume_scale.place(x=62, y=28)
    #endregion

def gui_list():
    click.play()

    label_list = tk.Label(window, image=img_list)
    label_list.place(x=0, y=0, relwidth=1, relheight=1)

    # Button list
    button_restart2 = tk.Button(window, image=img_resart2, command=gui_choose, bd=0, relief=tk.FLAT, highlightthickness=0)
    button_restart2.place(x=1398,y=769)

    # Coffee Result Buttons
    for i in range(filtered_df.shape[0]):
        button_result = tk.Button(window, text=filtered_df.iat[i,0], command=lambda num=i:gui_recipe(num), 
                                  font=("NotoSansTC-Bold", 20), anchor='w', padx=20, pady=0,
                                  fg="#522A01", bg="#fef9df", width=31, relief="flat", bd=0)
        if i%2==0:
            button_result.place(x=150, y=175+i*33)
        else:
            button_result.place(x=730, y=175+(i-1)*33)

    # Scale list
    #region
    volume_scale = tk.Scale(window, from_=0, to=100, command=set_volume,
                            orient='horizontal', length=100, width=7, sliderlength=20,
                            sliderrelief='flat', showvalue=False, bd=0,
                            bg="#2a3037", troughcolor='#68675e', activebackground='#fef9df', relief='flat',
                            highlightbackground="#68675e", highlightcolor="#68675e")
    volume_scale.set(scale_value)
    volume_scale.place(x=62, y=28)
    #endregion

def gui_sorry():
    click.play()

    label_sorry = tk.Label(window, image=img_sorry)
    label_sorry.place(x=0, y=0, relwidth=1, relheight=1)
    # Button sorry
    button_again = tk.Button(window, text=' 重新調一杯 ',command=gui_choose, font=('NotoSansTC-Bold', 30), fg="#522A01",bg="#fef9df") #("Nourd Bold",30,"bold")
    button_again.place(x=550,y=450)

    # Scale sorry
    #region
    volume_scale = tk.Scale(window, from_=0, to=100, command=set_volume,
                            orient='horizontal', length=100, width=7, sliderlength=20,
                            sliderrelief='flat', showvalue=False, bd=0,
                            bg="#2a3037", troughcolor='#68675e', activebackground='#fef9df', relief='flat',
                            highlightbackground="#68675e", highlightcolor="#68675e")
    volume_scale.set(scale_value)
    volume_scale.place(x=62, y=28)
    #endregion

def gui_recipe(num):
    click.play()

    global index
    index = num

    global label_recipe
    label_recipe = tk.Label(window, image=filtered_df.iat[index,7])
    label_recipe.place(x=0, y=0, relwidth=1, relheight=1)
    # Buttons recipe
    #region
    button_left_arrow = tk.Button(window, image=img_left_arrow, command=left_arrow, bd=0, relief=tk.FLAT, highlightthickness=0)
    button_left_arrow.place(x=165,y=718)
    button_backtolist = tk.Button(window, image=img_backtolist, command=gui_list, bd=0, relief=tk.FLAT, highlightthickness=0)
    button_backtolist.place(x=225,y=718)
    button_restart = tk.Button(window, image=img_resart, command=gui_choose, bd=0, relief=tk.FLAT, highlightthickness=0)
    button_restart.place(x=285,y=718)
    button_right_arrow = tk.Button(window, image=img_right_arrow, command=right_arrow, bd=0, relief=tk.FLAT, highlightthickness=0)
    button_right_arrow.place(x=345,y=718)

    global button_info
    button_info = tk.Button(window, image=img_info, command=info, bd=0, relief=tk.FLAT, highlightthickness=0)
    if filtered_df.iat[index,0]!='義式濃縮 Espresso' and filtered_df.iat[index,0]!='雙份義式濃縮 Double espresso':
        button_info.place(x=1417,y=770)
    #endregion

    # Scale recipe
    #region
    volume_scale = tk.Scale(window, from_=0, to=100, command=set_volume,
                            orient='horizontal', length=100, width=7, sliderlength=20,
                            sliderrelief='flat', showvalue=False, bd=0,
                            bg="#2a3037", troughcolor='#68675e', activebackground='#fef9df', relief='flat',
                            highlightbackground="#68675e", highlightcolor="#68675e")
    volume_scale.set(scale_value)
    volume_scale.place(x=62, y=28)
    #endregion

def gui_0x_esp():
    click.play()

    label_0x_esp = tk.Label(window, image=img_0x_esp)
    label_0x_esp.place(x=0, y=0, relwidth=1, relheight=1)
    # Buttons
    button_backtocof = tk.Button(window, image=img_backtocof, command=lambda:gui_recipe(index), bd=0, relief=tk.FLAT, highlightthickness=0)
    button_backtocof.place(x=255,y=718)

    # Scale Ox_esp
    #region
    volume_scale = tk.Scale(window, from_=0, to=100, command=set_volume,
                            orient='horizontal', length=100, width=7, sliderlength=20,
                            sliderrelief='flat', showvalue=False, bd=0,
                            bg="#2a3037", troughcolor='#68675e', activebackground='#fef9df', relief='flat',
                            highlightbackground="#68675e", highlightcolor="#68675e")
    volume_scale.set(scale_value)
    volume_scale.place(x=62, y=28)
    #endregion

def gui_1x_dou(): #ame, fla, vie, iri
    click.play()

    label_1x_dou = tk.Label(window, image=img_1x_dou)
    label_1x_dou.place(x=0, y=0, relwidth=1, relheight=1)
    #Buttons
    button_backtocof = tk.Button(window, image=img_backtocof, command=lambda:gui_recipe(index), bd=0, relief=tk.FLAT, highlightthickness=0)
    button_backtocof.place(x=255,y=718)

    # Scale 1x_dou
    #region
    volume_scale = tk.Scale(window, from_=0, to=100, command=set_volume,
                            orient='horizontal', length=100, width=7, sliderlength=20,
                            sliderrelief='flat', showvalue=False, bd=0,
                            bg="#2a3037", troughcolor='#68675e', activebackground='#fef9df', relief='flat',
                            highlightbackground="#68675e", highlightcolor="#68675e")
    volume_scale.set(scale_value)
    volume_scale.place(x=62, y=28)
    #endregion

#endregion

# 特殊按鈕
#region
def left_arrow():
    click.play()
    global index
    index-=1
    if index<0:
        index = filtered_df.shape[0]-1
    label_recipe.config(image=filtered_df.iat[index,7])

    if filtered_df.iat[index,0]=='義式濃縮 Espresso' or filtered_df.iat[index,0]=='雙份義式濃縮 Double espresso':
        button_info.place_forget()
    else:
        button_info.place(x=1417,y=770)

def right_arrow():
    click.play()
    global index
    index+=1
    if index>filtered_df.shape[0]-1:
        index = 0
    label_recipe.config(image=filtered_df.iat[index,7])

    if filtered_df.iat[index,0]=='義式濃縮 Espresso' or filtered_df.iat[index,0]=='雙份義式濃縮 Double espresso':
        button_info.place_forget()
    else:
        button_info.place(x=1417,y=770)

def info():
    click.play()
    if filtered_df.iat[index,0]=='美式咖啡 Americano' or\
    filtered_df.iat[index,0]=='馥列白 Flat White' or\
    filtered_df.iat[index,0]=='維也納咖啡 Vienna' or\
    filtered_df.iat[index,0]=='愛爾蘭咖啡 Irish Coffee':
        gui_1x_dou()
    else:
        gui_0x_esp()
#endregion

# 開始頁面
gui_choose()

# 循環播放背景音樂
pygame.mixer.music.play(-1)

window.mainloop()