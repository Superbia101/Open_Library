# TODO здесь писать код
from tkinter import *
from tkinter import ttk
import os


class ChatGUI:
    """Чат с графической оболочкой
    """

    def check_path(self, file_name: str, file_path: str) -> None:
        """Проверяет переданный путь директории

        :param file_name: Название файла
        :type file_name: str
        :param file_path: Адрес директории расположения
        :type file_path: str

        :raise FileNotFoundError: Завершение программы т.к. передан неверный путь

        :return: Если путь подходит - передаёт в конструктор
        """

        if os.path.exists(os.path.abspath(file_path)) and os.path.isdir(os.path.abspath(file_path)):
            self.path_text = os.path.abspath(os.path.join(file_path, file_name))
        else:
            raise FileNotFoundError('Проверь правильность переданного пути!')

    def __init__(self, file_name: str = 'chat_text.txt', file_path: str = ''):
        """Конструктор создаёт окно авторизации с которым уже может взаимодействовать пользователь.

        """
        self.cached_stamp = 0  # последнее время обновления файла-сервера
        self.lines = 0  # последняя внесённая данным профилем строка в файле-сервере
        self.text_cons = None  # создаём атрибут под будущий виджет
        self.path_text = ''

        # проверка, что переданный путь существует и там есть директория в которой можно создать файл
        self.check_path(file_name, file_path)

        # создание окон
        self.window = Tk()  # создаётся главное окно - Чат
        self.window.withdraw()  # окно чат теперь виджет верхнего уровня (невидим)
        self.name_window = Tk()  # окно авторизации
        self.name_window.title("Авторизация пользователя")  # название окна авторизации
        self.name_window.geometry('400x100+700+500')  # размер и положение окна
        self.name_window.resizable(width=False, height=False)  # запрет изменения размеров окна

        # создание опорного виджета; отступы списком в параметрах
        self.frame = ttk.Frame(self.name_window, padding=[45, 20, 45, 20], relief=SOLID)
        self.frame.pack(expand=True)  # свойства expand=True указывает, что Frame заполняет весь контейнер

        # создание надписи над окном ввода; оформления и размер текста "Helvetica 14"
        self.labels = Label(self.frame, text="Авторизуйтесь: ", font="Helvetica 14 bold")
        self.labels.grid(row=1, column=1, columnspan=3)  # положение надписи в форме (строка, колонка)

        # создание надписи слева от ввода; оформления и размер текста "Helvetica 10", граница объекта "ridge"
        self.label_name = Label(self.frame, text="Ваше Имя: ", font="Helvetica 10 bold", relief="ridge")
        self.label_name.grid(row=3, column=1)  # положение надписи в форме (строка, колонка)

        # привязка переменной к полю ввода
        self.on_off_btn = StringVar(self.frame)  # переменная привязанная к полю ввода
        self.on_off_btn.trace_add("write", self.name_btn_on_off)  # отслеживание изменения переменной(строки поля ввода)

        # создание поля ввода; текст по центру, оформления и размер "Helvetica 10", привязка переменной
        self.chat_tf = Entry(self.frame, justify=CENTER, font="Helvetica 10 bold", textvariable=self.on_off_btn)
        self.chat_tf.grid(row=3, column=2)  # положение поля в форме (строка, колонка)
        self.chat_tf.focus()  # установка фокуса в поле ввода

        # создание кнопки ввода имени; при пустом поле ввода отключена, по нажатию запуск функции ok_button
        self.chat_btn = ttk.Button(self.frame, text="Ok", state="disabled",
                                   command=lambda: self.ok_button(self.chat_tf.get()))
        self.chat_btn.grid(row=3, column=3)  # положение кнопки в форме (строка, колонка)

        self.window.mainloop()  # разрешение на взаимодействие пользователю

    def name_btn_on_off(self, *args: str) -> None:
        """Проверка заполнения поля "имени" - name_tf.

        :param args: Параметры обратного вызова
        :type args: str

        :return: Изменение параметра "state" кнопки "Ok" - name_btn
        """
        check_entry: str = self.on_off_btn.get()  # переменная со значением поля ввода авторизации - name_tf
        if len(check_entry):  # проверка на наличие символов
            self.chat_btn.config(state="normal")  # если поле не пустое - активация кнопки
            if check_entry.lower() == "admin":  # проверка на "admin")
                self.on_off_btn.set("Запрещенное имя!)")  # замена имени одновременно - сообщение
        else:
            self.chat_btn.config(state="disabled")  # если поле пустое - деактивация кнопки

    def ok_button(self, name: str) -> None:
        """Переходная функция, осуществляет закрытие окна авторизации и открытие окна чата.

        :param name: Имя профиля пользователя
        :type name: str

        :return: Переход в окно чата - window
        """
        self.name_window.destroy()  # закрытие окна авторизации - name_window
        self.chat_window(name)  # запуск функции chat_window

    def chat_window(self, name: str) -> None:
        """Создаёт главное чат-окно

        :param name: Имя пользователя
        :type name: str

        :return: Взаимодействие с пользователем посредством GUI
        """
        # показывается главное окно - Чат
        self.window.deiconify()  # становится видимым
        self.window.title("Чат")  # название окна
        # self.window.resizable(width=False, height=False)  # запрет изменения размеров окна
        self.window.configure(width=470, height=550)  # размер окна

        # создание опорного виджета; отступы списком в параметрах
        self.frame = ttk.Frame(self.window, padding=[5, 5, 5, 5])
        self.frame.pack(expand=True)  # свойства expand=True указывает, что Frame заполняет весь контейнер

        # создаётся надпись с именем пользователя в шапке окна
        self.label_name = Label(self.frame, text=name, font="Helvetica 13 bold")
        self.label_name.grid(row=0, column=0, columnspan=2)  # расположение в фрейме

        # создаётся текстовое поле для отображения чата
        self.text_cons = Text(self.frame, width=20, height=2, font="Helvetica 14", wrap="word")
        self.text_cons.grid(row=1, column=0, rowspan=2, columnspan=2, ipady=250, ipadx=150, pady=10)
        self.text_cons.config(cursor="arrow")  # тип курсора при наведении на виджет НЕ меняется
        self.text_cons.config(state=DISABLED)  # поле не заполняемо с клавиатуры
        self.text_cons.bind("<Enter>", self.update_chat)  # обновление чата при наведении курсора на поле отображения
        self.text_cons.bind("<Leave>", self.update_chat)  # обновление чата при уводе курсора с поля отображения

        # создаётся скролбар в текстовом поле
        scroll_bar = Scrollbar(self.text_cons)
        scroll_bar.place(relheight=1, relx=0.974)  # расположение в текстовом поле
        scroll_bar.config(command=self.text_cons.yview)  # привязывает скролбар к текстовому полю

        # создаётся поле ввода сообщений
        self.chat_tf = Entry(self.frame, font="Helvetica 13")
        self.chat_tf.grid(row=3, column=0, ipady=15, ipadx=70, pady=5)
        self.chat_tf.focus()

        # создаётся кнопка отправки; по нажатию запуск функции send_button
        self.chat_btn = ttk.Button(self.frame, text="Отправить", width=20,
                                   command=lambda: self.send_button(self.chat_tf.get(), name))
        self.chat_btn.grid(row=3, column=1, ipady=15, ipadx=15, pady=5, padx=5)
        self.chat_btn.bind("<Enter>", self.update_chat)  # обновление чата при наведении курсора на кнопку "Отправить"
        self.chat_btn.bind("<Leave>", self.update_chat)  # обновление чата при уводе курсора с кнопки "Отправить"

    def update_chat(self, event) -> None:
        """Догружает в поле вывода чата сообщения других пользователей.
        Запускается при наведении или снятии курсора с поля вывода.

        :param event: Параметры события вызова:системные данные, тип, координаты

        :except FileNotFoundError: Если файл предварительно не был найден.
        :except PermissionError: Если создать файл в директории нельзя.
        :except Exception: Прочее

        :return: Обновляет поле вывода
        """
        try:
            try:
                # если время изменения файла не совпадает с сохранённым
                if self.cached_stamp != os.stat(self.path_text).st_mtime:

                    with open(self.path_text, 'r', encoding='utf-8') as file:
                        text: list[str] = file.readlines()  # данные из файла
                        self.text_cons.config(state=NORMAL)  # поле вывода доступно к редактированию

                        for line in text[self.lines:]:  # с последней зарегистрированной строки до конца
                            self.text_cons.insert(END, line)  # записать по строчно в поле вывода

                        self.text_cons.config(state=DISABLED)  # поле вывода не доступно к редактированию

                    self.text_cons.see(END)  # прокручивает скролбар на последнюю строчку
                    self.lines = len(text)  # обновляется последняя зарегистрированная строка
                    self.cached_stamp = os.stat(self.path_text)  # обновляется время изменения файла

            except FileNotFoundError:
                # если файл не найден - создаётся
                with open(self.path_text, 'a+', encoding='utf-8'):
                    pass

        except PermissionError as err:
            print('Нет доступа!', err)
            self.window.destroy()
        except Exception as err:
            print('Что-то не так!', err)
            self.window.destroy()

    def send_button(self, msg: str, name: str) -> None:
        """ Оправка набранного сообщения в окно чата и файл-сервер.

        :param msg: Сообщение написанное в поле ввода и отправленное нажатием кнопки
        :type msg: str
        :param name: Имя профиля
        :type name: str

        :except PermissionError: Если создать файл в директории нельзя.
        :except Exception: Прочее

        :return: Вывод на экран, сохранение в файл
        """
        self.chat_tf.delete(0, END)  # очистка поля ввода
        message: str = "{0}@: {1}\n\n".format(name, msg)  # формирования сообщения

        # запись сообщения в текстовое окно чата
        self.text_cons.config(state=NORMAL)  # поле вывода доступно к редактированию
        self.text_cons.insert(END, message)  # запись сообщения в поле
        self.text_cons.config(state=DISABLED)  # поле вывода не доступно к редактированию
        self.text_cons.see(END)  # прокручивает скролбар на последнюю строчку
        self.chat_tf.focus()  # курсор в полее ввода

        try:
            with open(self.path_text, 'a+', encoding='utf-8') as file:
                file.write(message)  # запись сообщения в файл
                file.seek(0)  # сдвиг курсора в начало
                self.lines = len(file.readlines())  # обновляется последняя зарегистрированная строка
                self.cached_stamp = os.stat(self.path_text).st_mtime  # обновляется время изменения файла

        except PermissionError as err:
            print('Нет доступа!', err)
            self.window.destroy()
        except Exception as err:
            print('Что-то не так!', err)
            self.window.destroy()


# имя файла и путь который будет использоваться вместо сервера передаётся функции
a = ChatGUI('123', '..')  # запуск чата
