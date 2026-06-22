import re
import tkinter as tk
from tkinter import messagebox
import os
import webbrowser
from PIL import Image, ImageTk
try:
    with open("README.txt", "w", encoding="utf-8") as file:
        file.write(
            "Привет! Это инструкция пользования программой.\n"
            "Для начала работы закройте этот файл.\n"
            'Если у вас не установлена библиотека "Pillow" то можете в командной строке написать:"pip install pillow".\n'
            "Для получения информации обо мне, нажмите на кликабельный блок с названием.\n"
            "Весь репозиторий записан на моём Github.\n"
            "После закрытия нажмите Enter в консоли."
        )

    os.startfile("README.txt")  # Открывает файл в Блокноте

    input("После закрытия README.txt нажмите Enter...")
except FileNotFoundError:
    print("Файл не найден")

BUTTON_STYLE = {
    "font": ("Segoe UI", 12, "bold"),
    "width": 22,
    "height": 2,
    "bg": "#5C6B7A",      # серо-синий
    "fg": "white",
    "activebackground": "#44505D",
    "activeforeground": "white",
    "bd": 0,
    "cursor": "hand2"
}

class Bilal:

    def __init__(self):
        self.name = "Билал"
        self.age = "14"
        self.birthday = "16.09.2011"

    def bio(self):
        label.config(text =
            f'\n'
            f"Меня зовут {self.name}, мне {self.age} лет, родился я {self.birthday}.\n"
            f"Я занимаюсь музыкальным творчеством! А именно фортепиано и вокалом.\n"
            f"Факт №1: Ещё в младенчестве, когда я по особым обстоятельствам попал в больницу, врачи рассказывали моей маме, что я пел в палате.\n"
            f"После этого мама начала развивать мой музыкальный талант и поддерживать мой интерес к музыке.\n"
            f"Факт №2: Я начал пользоваться компьютером ещё в 4 года. Тётя подарила компьютер моим родителям, но тогда он был им не нужен, поэтому они отдали его мне.\n"
            f"С тех пор я продолжаю активно пользоваться компьютером и различными программами, а также начал развиваться в направлении программирования на Python.\n"
        )

    def objective(self):
        label.config(text =
            f'\n'
            f"Моя цель в программировании заключается в том, что мне интересно программировать.\n"
            f"Кроме того, этот навык поможет мне в будущей работе, поскольку человеческая логика остаётся важной и не может быть полностью заменена искусственным интеллектом.\n"
        )

    def history(self):
        label.config(text =
            f'\n'
            f'Моя история знакомства с программированием началась с того, что в интернете я нашёл школу программирования „Алгоритмика“, где начал изучать программирование на платформе Roblox.\n '
            f'Позже, когда я прошёл курс по программированию в Roblox, меня заинтересовал курс по HTML и CSS. После его прохождения у меня появился ещё больший интерес к программированию.\n'
        )

    def mentor(self):
        label.config(text =
            f"\n"
            f"Нашего ментора зовут Каракат. Каракат мне и моим одногрупникам часто помогает с трудностями, благодаря чему у нас появляется стимвул и интерес к учебе в программирование.\n"
            f"Лично мне Каракат помогла с модулем Random, хорошо объяснив работу и команды этого модуля!\n"
        )

    def A_to_B(self):
        label.config(text =
            f"\n"
            f"Когда я только пришел в школу CAP Education, я имел очень маленький опыт в программировании\n"
            f"Однако на данный момент я уже изучил не так уж и мало модулей! Такие как:Random, Sys, Turtle, Pygame, Time\n"
            f"Владею я ими не идеально, но и не так уж и плохо!\n"
        )

    def Hobby_and_passion(self):
        label.config(text =
            f"\n"
            f"У меня имеются хобби такие как: Музыка, Велоспорт, Программирование\n"
            f"Мои увлеченности это: Игры, Катание на электросамокате\n"
        )

    def best_work1(self):
        label.config(text ="\nНазвание: Продолжение работы в Pygame\nОписание:В этой работе мне предстоялось создать игру под названием 'Пинг-понг' в модуле Pygame, и реализовать систему перезапуска раундов и начисления очков игрокам.\nСсылка на работу в Getcourse: https://capeducation.getcourse.ru/pl/teach/control/lesson/view?id=335941296\n")

    def best_work2(self):
        label.config(text ="\nНазвание: Симуляция банкомата в Python\nОписание: Эта работа заключается в том чтобы создать систему банкомата и его клиентов. В работе мне нужно было реализовать систему пин-кодов, а также определенного лимита на снятие суммы за одну операцию!\nСсылка на работу в Getcourse: https://capeducation.getcourse.ru/pl/teach/control/lesson/view?id=335941292&editMode=0\n")

    def best_works(self):
        for widget in works_frame.winfo_children():
            widget.destroy()

        tk.Button(
            works_frame,
            text="Лучшая работа №1",
            command=self.best_work1,
            **BUTTON_STYLE
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            works_frame,
            text="Открыть",
            command=lambda: webbrowser.open(
                "https://capeducation.getcourse.ru/pl/teach/control/lesson/view?id=335941296"
            ),
            bg="#8A9AA5",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=12,
            bd=0,
            cursor="hand2"
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            works_frame,
            text="Лучшая работа №2",
            command=self.best_work2,
            **BUTTON_STYLE
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            works_frame,
            text="Открыть",
            command=lambda: webbrowser.open(
                "https://capeducation.getcourse.ru/pl/teach/control/lesson/view?id=335941292&editMode=0"
            ),
            bg="#8A9AA5",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=12,
            bd=0,
            cursor="hand2"
        ).grid(row=1, column=1, padx=5)

        works_frame.pack(pady=10)

    def Github(self):
        webbrowser.open("https://github.com/tailer-beliy/Bilal-s-Portfolio/tree/main")


bilal = Bilal()

root = tk.Tk()
root.title("Портфолио Билала")
root.geometry("1200x800")
root.resizable(False, False)

bg_image = Image.open("background.png")  # имя файла с фоном
bg_image = bg_image.resize(
    (root.winfo_screenwidth(), root.winfo_screenheight())
)

bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.image = bg_photo

background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()

root.bind("<Escape>", lambda event: root.destroy())

label = tk.Label(
    root,
    text="Выберите раздел",
    font=("Segoe UI", 14),
    bg="#F8F8F8",
    fg="#333333",
    justify="left",
    wraplength=900,
    padx=25,
    pady=20,
    relief="flat",
    bd=0
)
label.pack(pady=20, fill="x", padx=50)

buttons_frame = tk.Frame(root, bg="#F5F3F0")
buttons_frame.pack(pady=20)

works_frame = tk.Frame(root, bg="#F5F3F0")
works_frame.pack()

btn1 = tk.Button(
    buttons_frame,
    text="Биография",
    command=bilal.bio,
    **BUTTON_STYLE
)
btn1.grid(row=0, column=0, padx=10, pady=10)

btn2 = tk.Button(
    buttons_frame,
    text="Цель",
    command=bilal.objective,
    **BUTTON_STYLE
)

btn2.grid(row=0, column=1, padx=10, pady=10)

btn3 = tk.Button(
    buttons_frame,
    text="История",
    command=bilal.history,
    **BUTTON_STYLE
)
btn3.grid(row=1, column=0, padx=10, pady=10)

btn4 = tk.Button(
    buttons_frame,
    text="Ментор",
    command=bilal.mentor,
    **BUTTON_STYLE
)
btn4.grid(row=1, column=1, padx=10, pady=10)

btn5 = tk.Button(
    buttons_frame,
    text="Точка А в точку Б",
    command=bilal.A_to_B,
    **BUTTON_STYLE
)
btn5.grid(row=2, column=0, padx=10, pady=10)

btn6 = tk.Button(
    buttons_frame,
    text="Хобби и увлечения",
    command=bilal.Hobby_and_passion,
    **BUTTON_STYLE
)
btn6.grid(row=2, column=1, padx=10, pady=10)

btn7 = tk.Button(
    buttons_frame,
    text="Лучшие работы",
    command=bilal.best_works,
    **BUTTON_STYLE
)
btn7.grid(row=3, column=0, padx=10, pady=10)

btn8 = tk.Button(
    buttons_frame,
    text="Github",
    command=bilal.Github,
    **BUTTON_STYLE
)
btn8.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
