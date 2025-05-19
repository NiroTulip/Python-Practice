# Импорты
from abc import ABC, abstractmethod
from logic import REPORT, LOGIC_VARS
import re
from sys import exit
from tkinter import messagebox

# Базовый абстрактный класс, общий для всех типов вершин (вопросов, результатов(выводов), условных ветвлений, установщиков значений логических переменных)
class Vertex(ABC):
    # Номер вершины на схеме-графе
    vertex_num: int = None

    # Конструктор класса принимает номер вершины
    def __init__(self, vertex_num):
        self.vertex_num = vertex_num

    # Метод добавляет в глобальную переменную пути REPORT.PATH номер текущей вершины
    def add_vertex_to_path(self):
        REPORT.add_vertex_to_path(self.vertex_num)

    # Метод заменяет имя логической переменной в строке на её эквивалент в словаре LOGIC_VARS.VARS
    def replace_logic_var_name_for_eval(self, input_str):
        words = input_str.split()
        result_str = input_str
        for word in words:
            if LOGIC_VARS.has_var_key(word):
                new_var_name = "LOGIC_VARS.VARS['" + word + "']"
                result_str = result_str.replace(word, new_var_name)
        if result_str == input_str:
            print('В вершину ' + str(self.vertex_num) + ' передано некорректное условие - оно не содержит ни одной логической переменной из словаря LOGIC_VARS.VARS')
            exit()
        else:
            return result_str

    # Метод заменяет логические операторы сравнения в строке с математического формата на формат Python для последующего вычисления условия
    def replace_operators_for_eval(self, input_str):
        # Заменили одиночные вхождения знака '=' на '==', при этом операторы '<=', '>=', '==', '!=' не тронуты
        pattern = r'(?<![<>=!]{1})(={1})(?!={1})'
        result_str = re.sub(pattern, '==', input_str)
        # Заменяем остальные операторы
        result_str = result_str.replace('≥', '>=')
        result_str = result_str.replace('≤', '<=')
        result_str = result_str.replace('≠', '!=')
        result_str = result_str.replace(' || ', ' or ')
        result_str = result_str.replace(' & ', ' and ')
        result_str = result_str.replace(' OR ', ' or ')
        result_str = result_str.replace(' AND ', ' and ')
        return result_str

# Общий базовый класс для ВЕРШИН ВЫБОРА:
# 1) ВЕРШИН ВОПРОСОВ (КРУГ НА СХЕМЕ)
# 2) ВЕРШИН УСЛОВНЫХ ВЕТВЛЕНИЙ (РОМБ НА СХЕМЕ)
# То есть вершин в которых определяются значения переменных (вопросы) / вычисляется значение условий (условные ветвления)
# и по результатам условий проводится ветвеление - переход к новой вершине
# Эти 2 типа вершин определяют основную логику работы, ветвления и конечный результат
class Choice(Vertex):
    # Объект вершины, который будет загружен следующим, если реализуется условие перехода к левой ветке на графе
    # или если есть только единственный вариант следующей вершины
    load_next_vertex_left_or_only: Vertex = None
    # Объект вершины, который будет загружен следующим, если реализуется условие перехода к правой ветке на графе
    load_next_vertex_right: Vertex = None
    # Текст значения реализованного условия вершины после выбора пользователя (добавляется в Правило)
    condition_result_str: str = None
    # Направление для загрузки следующего объекта (левая ветка / правая ветка на графе). Принимает значения 'LEFT' или 'RIGHT'
    next_load_direction: str = None

    # Конструктор класса дополнительно принимает два объекта следующих вершин загрузки
    def __init__(self, vertex_num, next_vertex_left_or_only: Vertex = None, next_vertex_right: Vertex = None):
        super().__init__(vertex_num)
        self.load_next_vertex_left_or_only = next_vertex_left_or_only
        self.load_next_vertex_right = next_vertex_right

    # Метод добавляет в глобальную переменную отчета значение реализованного условия текущей вершины
    def add_condition_result_to_rool(self):
        REPORT.add_condition_to_rool(self.condition_result_str)

    # Метод определения загрузки следующей вершины
    def load_next_vertex(self):
        # Если вторая следующая вершина не указана, то загружаем первую, т.е. единственную вершину (если она указана)
        if self.load_next_vertex_right is None:
            if self.load_next_vertex_left_or_only is not None:
                self.load_next_vertex_left_or_only.load()
        # Если вторая вершина указана, надо определять, какое условие реализовалось
        # проводим выбор вершины в соответствии со свойством next_load_direction
        else:
            if self.next_load_direction is not None:
                match self.next_load_direction:
                    case 'LEFT':
                        self.load_next_vertex_left_or_only.load()
                    case 'RIGHT':
                        self.load_next_vertex_right.load()

    # Абстрактный метод для загрузки самого объекта-потомка (вопроса / условного ветвления)
    @abstractmethod
    def load(self):
        pass

    # Абстрактный метод для вычисления значения строки self.condition_result_str
    @abstractmethod
    def get_condition_result_str(self):
        pass

class Stub(Vertex):
    def load(self):
        messagebox.showinfo("ПРОГРАММНАЯ ЗАГЛУШКА", "Эта ветка алгоритма пока не реализована программно. Выберете пожалуйста другой ответ. В будущем проект будет доделан. Спасибо за понимание. Счастья Вам, здоровья.")