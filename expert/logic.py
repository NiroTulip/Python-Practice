# МОДУЛЬ СОДЕРЖИТ ОПИСАНИЕ КЛАССА И ОБЪЕКТА С ЛОГИЧЕСКИМИ ПЕРЕМЕННЫМИ (В ВИДЕ СЛОВАРЯ)
# И ОПИСАНИЕ КЛАССА И ОБЪЕКТА ОТЧЕТА, КОТОРЫЙ ВЫГРУЖАЕТСЯ В ФАЙЛ report.txt

from tkinter import messagebox
from typing import List

# КЛАСС ОСНОВНОЙ ЛОГИКИ СО СЛОВАРЕМ С ЛОГИЧЕСКИМИ ПЕРЕМЕННЫМИ-----------------------------------------------------------
class Logic:
    VARS = {
        # Начальная стадия опроса
        'IS_RECOMMENDED': None, # Рекомендация
        'AGE': None, # Возраст

       # Блок образования
        'IS_EDUCATED': None, # Образование
        'DEGREE_TYPE': None, # Степень
        'IS_ACTOR_COURSE': None, # Актерские курсы
        'DEGREE': None,  # ВЫЧИСЛЯЕМАЯ ПЕРЕМЕННАЯ, значения 0-3

        # БЛОК ОЦЕНКИ ЭКЗАМЕНАЦИОННЫХ ИСПЫТАНИЙ
        'ART_READING': None,
        'ACTOR_ETUDE': None,
        'CHOREOGRAPHY': None,
        'VOCAL': None,
        'SUMM_EXAM': None,  # вычисляемая

        # БЛОК ОЦЕНКИ ОСНОВНЫХ ПРОФЕССИОНАЛЬНЫХ КАЧЕСТВ
        'GESTURE_SKILL': None,
        'EMOTION_SKILL': None,
        'TEXT_SKILL': None,
        'IMPROV_SKILL': None,
        'SUMM_SKILL': None,  # вычисляемая

        # БЛОК ОЦЕНКИ ДОПОЛНИТЕЛЬНЫХ ПРОФЕССИОНАЛЬНЫХ НАВЫКОВ
        'IS_GOOD_KISS': None,
        'IS_GOOD_DRUNK': None,
        'IS_GOOD_FAINT': None,
        'IS_GOOD_SLAP': None,
        'SUMM_DOP_SKILL': None, # вычисляемая

        # БЛОК ОЦЕНКИ ФИЗИЧЕСКОЙ ПРИВЛЕКАТЕЛЬНОСТИ
        'IS_BEAUTY_SHAPE': None,
        'IS_BEAUTY_SMILE': None,
        'HEIGHT': None,
        'IS_TALL': None,  # вычисляемая
        'BEAUTY_SCALE': None,
        'SUMM_BEAUTY': None,  # вычисляемая

        # БЛОК ОЦЕНКИ ФИЗИЧЕСКОЙ ПОДГОТОВКИ
        'IS_PRACTICE_SPORT': None,
        'IS_SHAPED_MUSCLES': None,
        'IS_MARTIAL_ARTS': None,
        'IS_PERFORM_STUNTS': None,
        'SUMM_PHYSICAL': None, # вычисляемая

        # БЛОК ОЦЕНКИ ИНТЕЛЛЕКТУАЛЬНЫХ СПОСОБНОСТЕЙ
        'KNOW_FOREIGN_LANG': None,
        'IQ_LEVEL': None,
        'IS_SMART': None,
        'GOOD_MEMORY': None,
        'HIGH_EMOTIONAL_INTELLIGENCE': None,
        'SUMM_INTELLECT': None, # вычисляемая

        # БЛОК ОЦЕНКИ ТЕХНИЧЕСКИХ НАВЫКОВ
        'HANDLE_AUTO': None,
        'HANDLE_MOTO': None,
        'HANDLE_HYDRO': None,
        'HANDLE_BIKE': None,
        'SUMM_TECH': None, # вычисляемая

        # БЛОК ОЦЕНКИ ПСИХОЛОГИЧЕСКОЙ УСТОЙЧИВОСТИ
        'NOT_SCARY_BLOOD': None,
        'NOT_SCARY_CORPSES': None,
        'NOT_SCARY_REMAINS': None,
        'NOT_SCARY_INSECTS': None,
        'SUMM_MENTAL_STRENGTH': None, # вычисляемая

        # БЛОК ОЦЕНКИ ВЛАДЕНИЯ ОРУЖИЕМ
        'HANDLE_GUN': None,
        'HANDLE_MACHINEGUN': None,
        'HANDLE_GRENADER': None,
        'HANDLE_FLAMER': None,
        'SUMM_GUNS': None, # вычисляемая

        # Стадия ветвления возможных вариантов
        'IS_MOVIE_EXP': None,
        'IS_MOVIE_PROF': None,
        'IS_FULL_MOVIE': None,
        'EXPERIENCE': None,
        'IS_COMMERCIAL_MOVIE': None,
        'IS_COMMERCIAL_SUCCESS': None,
        'SUCCESS': None,
        'IMDB_RATING': None,
        'SUPER_STAR_PART': None,
        'FOREIGN_LANG': None,  # Иностранный язык
        'IS_AWARDS': None,
        'IS_OSCAR': None,
        'IS_GOOD_LOOK_ANTIQUE_DRESS': None,
        'FOOTAGE_TIMING_MIN': None, #Хронометраж эпизодов
        'IS_GOOD_LOOK_MILITARY_UNIFORM': None,
        'SECOND_STAR_PART': None,
        'THIRD_STAR_PART': None
    }

    # Метод возвращает тип bool, есть ли в словаре VARS ключ var или нет
    def has_var_key(self, var):
        get_value = self.VARS.get(var, 'KEY_NOT_FOUND')
        if get_value != 'KEY_NOT_FOUND':
            return True
        else:
            return False

    # Метод устанавливает значение логической переменной в словаре VARS
    def set_var(self, var_name, value):
        if self.VARS.get(var_name, 'KEY_NOT_FOUND') != 'KEY_NOT_FOUND':
            self.VARS[var_name] = value
            return value
        else:
            return None

    # Метод возвращает значение переменной
    def get_var(self, var):
        get_value = self.VARS.get(var, 'KEY_NOT_FOUND')
        if get_value != 'KEY_NOT_FOUND':
            return get_value
        else:
            return None

    # Метод возвращает значение суммы переменных, указанных в списке vars
    def get_vars_summ(self, vars: List[str], factor = 1):
        result: int = 0
        for var in vars:
            get_value = self.VARS.get(var, 'KEY_NOT_FOUND')
            if get_value != 'KEY_NOT_FOUND':
                if get_value is None:
                    print('Ошибка функции get_vars_summ: значение переменной-ключа в словаре LOGIC_VARS.VARS еще не определено: ' + var)
                    exit()
                else:
                    result += get_value * factor
            else:
                print('Ошибка функции get_vars_summ: словарь LOGIC_VARS.VARS не содержит переменной-ключа ' + var)
                exit()
        return result

    # Метод возвращает строку с именем переменной и ее значением из словаря VARS
    def get_var_value_str(self, var):
        get_value = self.VARS.get(var, 'KEY_NOT_FOUND')
        if get_value != 'KEY_NOT_FOUND':
            return var + ' = ' + str(get_value)
        else:
            return None

# КЛАСС ОТЧЕТА, КОТОРЫЙ ВЫГРУЖАЕТСЯ В ФАЙЛ report.txt  -----------------------------------------------------------------
class Report:
    # Содержимое этих 3 переменных последовательно выгружается в текстовый файл отчет report.txt
    PATH: str = ""      # Хранит последовательность пройденных вершин - ПУТЬ.
    ROOL: str = "ЕСЛИ " # Хранит последовательность реализованных условий вершин выбора, которые формируют ПРАВИЛО ВЫВОДА.
    VAR_VALUES_FOR_REPORT = [] # Список значений логических переменных для отчета.

    # Метод добавляет в переменную пути вершин PATH значение текущей вершины
    def add_vertex_to_path(self, vertex_num):
        if self.PATH == "":
            self.PATH = str(vertex_num)
        else:
            self.PATH = self.PATH + ', ' + str(vertex_num)

    # Метод добавляет переменную правила ROOL значение реализованного условия текущей вершины
    def add_condition_to_rool(self, condition_result_str, calculated = False):
        if self.ROOL == "ЕСЛИ " or calculated:
            self.ROOL = self.ROOL + str(condition_result_str)
        else:
            self.ROOL = self.ROOL + ' И ' + str(condition_result_str)

    # Метод добавляет в список логических переменных строку со значением переменной
    def add_var_value(self, var_value_str):
        self.VAR_VALUES_FOR_REPORT.append(var_value_str)

    # Добавляет в конец глобальной переменной правила ROOL результат логического вывода - DECISION и RESULT
    def rool_finalize(self, decision, result):
        self.ROOL = self.ROOL + ", ТО DECISION = " + decision + "; RESULT = " + result

    # Выгружает файл отчета
    def save_report(self):
        try:
            with open("report.txt", "w", encoding="utf-8") as file:
                file.write("ПУТЬ:\n")
                file.write(self.PATH)
                file.write("\n\n")
                file.write("ПРАВИЛО:\n")
                file.write(self.ROOL)
                file.write("\n\n")
                file.write("ЗНАЧЕНИЯ ПЕРЕМЕННЫХ:\n")
                file.write('\n'.join(self.VAR_VALUES_FOR_REPORT))
            # Окно с оповещением о выгрузке отчета
            messagebox.showinfo("ОТЧЕТ ВЫГРУЖЕН", "Отчет выгружен в файл report.txt")
        except Exception as err:
            print('ОШИБКА ПРИ ВЫГРУЗКЕ ОТЧЕТА report.txt: ' + err)

# Объекты КЛАССА ЛОГИКИ и КЛАССА ОТЧЕТА. Номер в названии соответствует номеру вершины в графе.-------------------------

# Объект LOGIC_VARS класса Logic содержит св-во словарь с логическими переменными
LOGIC_VARS = Logic()

# Объект отчета класса Report (содержит св-ва для Пути, Правила вывода, Список значений переменных)
REPORT = Report()
