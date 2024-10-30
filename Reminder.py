from tkinter import*
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


def set():# установка напоминания
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


window.mainloop()
