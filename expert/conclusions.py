from base_vertexes import Vertex
from logic import REPORT
from tkinter import messagebox
from sys import exit

# Базовый класс ВЕРШИНЫ РЕЗУЛЬТАТОВ-ВЫВОДОВ - ПРЯМОУГОЛЬНИК НА СХЕМЕ
# Используются только его классы-потомки
class Conclusion(Vertex):
    decision: str = None # ОКОНЧАТЕЛЬНОЕ РЕШЕНИЕ (два варианта) - "ОТКАЗ", "ПРЕДЛОЖЕНИЕ"
    result: str = None # РЕЗУЛЬТАТ: Роль при решении "ПРЕДЛОЖЕНИЕ" / Причина отказа при решении "ОТКАЗ"

    # Конструктор класса
    def __init__(self, vertex_num, decision, result):
        super().__init__(vertex_num)
        self.decision = decision
        self.result = result

    # Основной метод загружает объект и выполняет всю работу по логическому выводу и завершению
    def load(self):
        self.add_vertex_to_path() # Добавили номер вершины в переменную пути PATH
        self.show_result()        # Выводим результаты в окошко
        self.save_report()        # Сохраняем отчет
        exit()

    # Выводит результаты с заключением работы ЭС в окно-уведомление
    def show_result(self):
        messagebox.showinfo(self.decision, self.result)

    # Сохраняет отчет в текстовый файл report.txt и выводит окно-уведомление о сохранении отчета
    def save_report(self):
        # Добавляет в конец глобальной переменной правила ROOL переменные DECISION и RESULT
        REPORT.rool_finalize(self.decision, self.result)
        # Выгрузили текстовый файл с отчетом
        REPORT.save_report()

# Класс ВЕРШИНЫ РЕЗУЛЬТАТА - ПРЕДЛОЖЕНИЕ РОЛИ
class Conclusion_Role(Conclusion):
    # Конструктор класса принимает только результат
    def __init__(self, vertex_num, result):
        super().__init__(vertex_num, "ПРЕДЛОЖЕНИЕ", result)

# Класс ВЕРШИНЫ РЕЗУЛЬТАТА - ОТКАЗ
class Conclusion_Deny(Conclusion):
    # Конструктор класса принимает только результат
    def __init__(self, vertex_num, result):
        super().__init__(vertex_num, "ОТКАЗ", result)