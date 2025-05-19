from tkinter import Tk, Frame, Label, Entry, IntVar, Radiobutton, Button, END

#-----------------------------------------ЗАДАНИЕ РАБОЧЕЙ ФОРМЫ ОКНА ---------------------------------------------------

window = Tk() #Создаём окно приложения.
window.title("Отбор актрис в Голливуд") #Добавляем название приложения.
window.geometry('1200x800') #Задали размер окна

# Фрейм-контейнер для элементов графического интерфейса помещается в окне
frame = Frame(
   window,    #Указываем окно для размещения Frame.
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10  #Задаём отступ по вертикали.
)
frame.pack(expand=True) # указываем, что Frame заполняет весь контейнер, созданный для него.

# Текст вопроса помещается во фрейм
ask_lb = Label(
   frame,
   font=("Cambria", 25)
)
ask_lb.grid(row=1, column=1, sticky="W")

# Создает новое поле ввода
def add_answ_reader(width_p):
    # Поле ввода ответа на вопрос помещается во фрейм
    answ_reader = Entry(
        frame,
        width=width_p,
        font=("Cambria", 25)
    )
    answ_reader.grid(row=1, column=2, sticky="W")
    return answ_reader

# Создали поле ввода
answ_reader = add_answ_reader(3)

# Пересоздает заново поле ввода, т.к. это единственный способ изменить его ширину
def update_answ_reader(width_p):
    global answ_reader
    answ_reader.destroy()
    answ_reader = add_answ_reader(width_p)

    # Активировали элемент ввода Entry
    answ_reader.grid()

    # Очищаем строку ввода элемента Entry
    answ_reader.delete(0, END)
    return answ_reader

# Радиокнопка ввода ответа на вопрос помещается во фрейм
r_var = IntVar()
r_var.set(0)
answ_radio_btn_1 = Radiobutton(frame, text='1 вариант', font=("Cambria", 16), variable=r_var, value=1)
answ_radio_btn_2 = Radiobutton(frame, text='2 вариант', font=("Cambria", 16), variable=r_var, value=2)
answ_radio_btn_1.grid(row=1, column=2, sticky="NW")
answ_radio_btn_2.grid(row=1, column=2, sticky="SW")

# Кнопка ответа помещается во фрейм
answ_btn = Button(
   frame,
   font=("Cambria", 25),
   text='Ответить'
)
answ_btn.grid(row=1, column=3, sticky="E")

# Место для рисунка
img_lb = Label(
   frame
)
img_lb.grid(row=2, columnspan = 5)
