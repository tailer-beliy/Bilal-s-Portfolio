import re
import tkinter as tk
from tkinter import messagebox
import os
import webbrowser
try:
    with open("README.txt", "w", encoding="utf-8") as file:
        file.write(
            "Привет! Это инструкция пользования программой.\n"
            "Для начала работы закройте этот файл.\n"
            "Для получения информации обо мне, нажмите на кликабельный блок с названием.\n"
            "Весь репозиторий записан на моём Github.\n"
            "После закрытия нажмите Enter в консоли."
        )

    os.startfile("README.txt")  # Открывает файл в Блокноте

    input("После закрытия README.txt нажмите Enter...")
except FileNotFoundError:
    print("Файл не найден")
finally:
    file.close()
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
            command=self.best_work1
        ).pack()

        tk.Button(
            works_frame,
            text="Лучшая работа №2",
            command=self.best_work2
        ).pack()

        works_frame.pack()

    def Github(self):
        webbrowser.open("https://github.com/tailer-beliy/Bilal-s-Portfolio/tree/main")


bilal = Bilal()

root = tk.Tk()
root.title("Портфолио Билала")
root.state("zoomed")

root.bind("<Escape>", lambda event: root.destroy())

label = tk.Label(root, text="")
label.pack()

works_frame = tk.Frame(root)
works_frame.pack()

btn1 = tk.Button(root, text="Биография", command=bilal.bio)
btn1.pack()

btn2 = tk.Button(root, text="Цель", command=bilal.objective)
btn2.pack()

btn3 = tk.Button(root, text="История", command=bilal.history)
btn3.pack()

btn4 = tk.Button(root, text="Ментор", command=bilal.mentor)
btn4.pack()

btn5 = tk.Button(root, text="Точка А в точку Б", command=bilal.A_to_B)
btn5.pack()

btn6 = tk.Button(root, text="Хобби и увлечённости", command=bilal.Hobby_and_passion)
btn6.pack()

btn7 = tk.Button(root, text="Лучшие работы на GetCourse", command=bilal.best_works)
btn7.pack()

btn8 = tk.Button(root, text="Переход на Github", command=bilal.Github)
btn8.pack()

root.mainloop()
