from tkinter import *
import sqlite3
from tkinter import scrolledtext  

database = sqlite3.connect("database.db") #подключаемся к базе данных
cursor = database.cursor() #создаем курсор
records = cursor.fetchall() #создаем записи

def clicked():
    textf='INSERT INTO employer VALUES'+"('"+str(read1.get())+"','"+str(read2.get())+"','"+str(read3.get())+"','"+str(read4.get())+"','"+str(read5.get())+"')"
    database.execute(textf) #добавим сотрудника
    database.commit() #сохраним изменения
def remove():
    delete = """DELETE from employer where id ="""+str(read6.get())
    cursor.execute(delete)
    database.commit()
def plusintoscrolledtext():
    records = cursor.fetchall() #создаем записи
    for i in records():
        scrolledtext.insert(INSERT, 'ID', i[0], 'ФИО', i[1],'Номер телефона', i[2], 'Электронная почта',i[3], 'Заработная плата', i[4])

window = Tk() #создаем окно
window.title("Text of employer company") #именуем окно

text0 = Label(window, text="Добавить сотрудника")  #создаем текст
text0.grid(column=0, row=0)  #редактируем текст
read1 = Entry(window,width=10) #создаем поле ввода для id
read1.grid(column=1, row=0)  #редактируем поле ввода
text1 = Label(window, text="id") #создаем текст id
text1.grid(column=1, row=2)#редактируем текст
read2 = Entry(window,width=30) #создаем поле ввода для ФИО
read2.grid(column=2, row=0) #редактируем поле ввода
text2 = Label(window, text="ФИО") #создаем текст для ФИО
text2.grid(column=2, row=2)#редактируем текст
read3 = Entry(window,width=20) #создаем поле ввода для номера телефона
read3.grid(column=3, row=0) #редактируем поле для номера телефона
text3 = Label(window, text="номер телефона") #создаем текст для номера телефона
text3.grid(column=3, row=2)#редактируем текст
read4 = Entry(window,width=30) #создаем поле ввода для электронной почты
read4.grid(column=4, row=0) #редактируем поле для электронной почты
text4 = Label(window, text="электронная почта") #создаем текст для электронной почты
text4.grid(column=4, row=2)#редактируем текст
read5 = Entry(window,width=20) #создаем поле ввода для заработной платы
read5.grid(column=5, row=0) #редактируем поле для заработной платы
text5 = Label(window, text="заработная плата") #создаем текст для заработной платы
text5.grid(column=5, row=2)#редактируем текст
button = Button(window, text="Добавить сотрудника", command=clicked)  #создаем кнопку
button.grid(column=6, row=0) #редактируем кнопку

text6 = Label(window, text="Удалить сотрудника")  #создаем текст
text6.grid(column=0, row=3)  #редактируем текст
read6 = Entry(window,width=10) #создаем поле ввода для id
read6.grid(column=1, row=3)  #редактируем поле ввода
button = Button(window, text="Удалить сотрудника", command=remove)  #создаем кнопку
button.grid(column=2, row=3) #редактируем кнопку
text6 = Label(window, text="id") #создаем текст id
text6.grid(column=1, row=4)#редактируем текст

text7 = Label(window, text="Список сотрудников:", font=("Comic Sans", 30))#создаем текст
text7.grid(column=0, row=5)#работаем с текстом

scrolledtext = scrolledtext.ScrolledText(window, width=70, height=20)  
scrolledtext.grid(column=0, row=6)
plusintoscrolledtext()

window.geometry('1500x500')


window.mainloop() #выводим окно
