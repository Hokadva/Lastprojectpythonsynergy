import sqlite3
from tkinter import *

database = sqlite3.connect("database.db") #создаем базу данных
cursor = database.cursor()#создаем курсор
cursor.execute("CREATE TABLE employer(id, фамилия имя отчество , номер телефона, электронная почта, заработная плата)")#создаем поля

window = Tk() #создаем окно
window.title("Create database") #именуем окно
text1 = Label(window, text="Database created", font=("Comic Sans", 30))#создаем текст
text1.grid(column=0, row=0)#работаем с текстом
window.geometry('1000x1000')  
