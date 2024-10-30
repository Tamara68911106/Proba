from tkinter import*
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


t=0

def set():# установка напоминания
    global t
    rem = sd.askstring ("Время напоминание", "введите время напоминание в формате ЧЧ:ММ (в 24часовом формате)") #получим время в переменную рем, то время, кт-е введет пользователь с помощью simpdialog
    if rem: # если пользователь что-то ввел и перемнная rem не пустая, то начинаем с ней работать
        try:
            hour = int(rem.split(":")[0])  # т.к. чаты нужны в виде целого числа - берем int. Т.Е. строку rem с помощью split делим на 2 части и берем часть с номером 0 и все это делаем целым числом.
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour = hour,minute=minute) # получим то время, на которое должны установить напоминание
            print (dt)
            t=dt.timestamp()# превратили в млрд сек, и сработает наше напоминание
            print(t)
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка {e}")


window = Tk()
window.title("Напомиание")
label = Label(text = "Установите напоминание")
label.pack(pady=10)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack()

def check():
    global t # проверяем переменую Т,чтобы иметь к ней доступ внутри нашей функции
    if t: # чтобы не было ошибок делаем ifю Переменная Т не пустая, в ней что-то есть.
        now= time.time() #создаем отдельную от глобальной перемнную now/ эта функция устанавлямает временную метку текущего времени
        if now>=t: # если now больше или равно t - напоминание
            play_snd()
            t = 0
    window.after(1000,check) #программа проверяет каждые 6 мин

window.mainloop()
