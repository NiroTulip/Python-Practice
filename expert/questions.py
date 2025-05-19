# Импорты, касающиеся графического интерфейса
from gui import ask_lb, img_lb, answ_btn, answ_radio_btn_1, answ_radio_btn_2, answ_reader, update_answ_reader, r_var
from tkinter import messagebox, END
from PIL import Image as I # Должен быть установлен пакет Pillow
from PIL import ImageTk as ITk
# Другие импорты
from abc import abstractmethod
from re import fullmatch
from logic import REPORT, LOGIC_VARS
from base_vertexes import Choice, Vertex, Stub

__all__ = ['Question_Number', 'Question_Number_Dihotomy', 'Question_Number_Many_Options', 'Question_Radio', 'Y_N_Question', 'Question_Str']

# Базовый абстрактный класс ВОПРОСА (КРУГ НА СХЕМЕ)
# В вопросах происходит заполнение логических переменных из словаря LOGIC_VARS.VARS по результатам ответов на вопросы
# за исключением вычисляемых логических переменных
class Question(Choice):
    # Текст вопроса
    text: str = None
    # Картинка вопроса
    image_path: str = None
    # Название глобальной логической переменной (ключа из словаря LOGIC_VARS.VARS), в которую надо поместить результат
    logic_var_name: str = None
    # Ответ может быть разных типов (строка или число)
    answer = None
    # Режим добавления скобки в Правило  - используется, чтобы поместить набор условий в скобки перед расчетной переменной
    # с целью подчеркнуть тот факт, что неколько условий эквивалентны этой расчетной переменной
    # Пример: (IS_EDUCATED = True И DEGREE_TYPE = Магистр) ≡ DEGREE = 3
    bracket_mode: str = None

    # Конструктор класса
    def __init__(self, vertex_num, text, image_path, var_name, next_vertex_left_or_only: Vertex = None, next_vertex_right: Vertex = None, bracket_mode: str = None):
        super().__init__(vertex_num, next_vertex_left_or_only, next_vertex_right)
        self.text = text
        self.image_path = image_path
        self.logic_var_name = var_name
        self.bracket_mode = bracket_mode

    # Метод загружает вопрос (текст вопроса и его картинку) из объекта в элементы-виджеты формы фрейма окна
    # Метод добавляет номер вершины в переменную пути REPORT.PATH
    def load(self):
        # Добавили номер вершины в переменную пути REPORT.PATH
        self.add_vertex_to_path()

        # Текст вопроса помещается в виджет label для текста вопроса
        ask_lb['text'] = self.text

        # Картинка вопроса помещается  в виджет label для картинки вопроса
        im = I.open(self.image_path)
        ph = ITk.PhotoImage(im)  # Создали объект с изображением
        img_lb.configure(image = ph)
        img_lb.image = ph

        # Указали в кнопке ответа обработчик ее нажатия - метод process_answer
        answ_btn['command'] = self.process_answer

    # Метод устанавливает значение глобальной логической переменной из словаря LOGIC_VARS.VARS по ее названию (ключ) и ответу (значение)
    def set_logic_variable(self):
        if LOGIC_VARS.set_var(self.logic_var_name, self.answer) is None:
            print('ОШИБКА! Словарь объекта LOGIC_VARS не содержит ключа ' + self.logic_var_name)
            exit()

    # Метод добавляет имя переменной текущего вопроса и её значение в список значений переменных REPORT.VAR_VALUES_FOR_REPORT (для отчета)
    def add_var_value_to_report(self):
        var_value_str = LOGIC_VARS.get_var_value_str(self.logic_var_name)
        if var_value_str is None:
            print('ОШИБКА! Словарь объекта LOGIC_VARS не содержит ключа ' + self.logic_var_name)
            exit()
        else:
            # Метод добавляет имя переменной и её значение в список значений переменных REPORT.VAR_VALUES_FOR_REPORT (для отчета)
            REPORT.add_var_value(var_value_str)

    # Метод вычисляет строку self.condition_result_str
    def get_condition_result_str(self):
        var_value_str = LOGIC_VARS.get_var_value_str(self.logic_var_name)
        if var_value_str is None:
            print('ОШИБКА! Словарь объекта LOGIC_VARS не содержит ключа ' + self.logic_var_name)
            exit()
        else:
            if self.bracket_mode is not None:
                match self.bracket_mode:
                    case '(':
                        var_value_str = '(' + var_value_str
                    case ')':
                        var_value_str = var_value_str + ')'
                    case '()':
                        var_value_str = '(' + var_value_str + ')'

            # Метод добавляет в глобальную переменную с текстом правила ROOL (для отчета) значение реализованного условия текущей вершины
            self.condition_result_str = var_value_str

    # Метод добавляет в переменную с текстом правила REPORT.ROOL значение реализованного условия текущего вопроса (для отчета)
    def add_var_condition_to_rool(self):
        self.get_condition_result_str()
        self.add_condition_result_to_rool()

    # Метод добавляет имя переменной и её значение в список значений переменных REPORT.VAR_VALUES_FOR_REPORT (для отчета)
    # Метод добавляет в глобальную переменную с текстом правила REPORT.ROOL (для отчета) значение реализованного условия текущей вершины
    def add_var_value_and_condition_to_report(self):
        var_value_str = LOGIC_VARS.get_var_value_str(self.logic_var_name)
        if var_value_str is None:
            print('ОШИБКА! Словарь объекта LOGIC_VARS не содержит ключа ' + self.logic_var_name)
            exit()
        else:
            self.add_var_value_to_report()
            self.add_var_condition_to_rool()

    # Получение ответа, установка значения логической переменной, обработка ответа, загрузка следующей вершины.
    def process_answer(self):
        self.get_answer()               # Получили ответ
        # Дальнейшая обработка только, если ответ получен
        if self.answer is not None:
            # Если переход НЕ на заглушку, то установили значение логической переменной и добавили условие и значение переменной в отчет
            if not (self.next_load_direction == 'RIGHT' and isinstance(self.load_next_vertex_right, Stub)):
                self.set_logic_variable()       # Установили значение логической переменной
                self.add_var_value_and_condition_to_report()  # Добавили значение переменной в список значений переменных и условие в список условий в объекте REPORT
            self.load_next_vertex()         # Загрузили следующую вершину

    # Абстрактный метод получения значения ответа из элементов ввода формы
    @abstractmethod
    def get_answer(self):
        pass

# Базовый класс вопроса, в котором ответ вводится в строку ввода Entry в виде строки
# Реализует метод get_answer
# Класс не используется в вопросах - используются его классы-потомки
# Унаследованное св-во answer (ответ) получает строковое значение, однако в классе-потомке Question_Number - числовое значение
class Question_Entry(Question):
    # Свойство - строка ответа, полученная из поле ввода Entry
    str_input: str = None
    # Стандартная ширина поля ввода
    answ_reader_width = 4

    # В метод загрузки добавлена деактивация радиокнопок и активации строки ввода Entry
    def load(self):
        global answ_reader
        super().load()

        # Деактивировали элементы ввода радиокнопки
        answ_radio_btn_1.grid_remove()
        answ_radio_btn_2.grid_remove()

        # Задали стандартную узкую ширину поля ввода (поле ввода пересоздается)
        answ_reader = update_answ_reader(self.answ_reader_width)

    # Метод получает ответ в виде строки из поля ввода Entry и помещает его в свойство str_answer
    def get_answer(self):
        str_from_entry = answ_reader.get()
        if len(str_from_entry) > 0:
            self.str_input = str_from_entry
            self.answer = self.str_input
        else:
            messagebox.showinfo('Введите значение', 'Введите значение в поле ввода')
            self.str_input = None
            self.answer = None

# Класс вопроса, где ответ это строка, которая вводится в поле ввода Entry,
# а для вычисления условий переходов используется словарь ответов answer_dict
# ключи (ответы) в этом словаре должны быть в формате с большой буквы: 'Ключ'
# Унаследованное св-во answer (ответ) получает строковое значение
class Question_Str(Question_Entry):
    answer_dict = dict()

    # В Конструктор класса добавлен словарь с ответами
    def __init__(self, vertex_num, text, image_path, answer_dict, var_name, bracket_mode: str = None):
        super().__init__(vertex_num, text, image_path, var_name, None, None, bracket_mode)
        self.answ_reader_width = 13
        self.set_answer_dict(answer_dict)

    # Метод заполнения свойства - словаря answer_dict. Нужен для того, чтобы привести ключи в формат с большой буквы: 'Ключ'
    def set_answer_dict(self, input_answer_dict: dict):
        for key, value in input_answer_dict.items():
            self.answer_dict[key.title()] = value

    # Метод получает ответ в виде строки из поля ввода Entry
    def get_answer(self):
        # Получили строку, введенную в поле ввода Entry
        super().get_answer()
        # Если строка была введена, помещаем ее в ответ в формате с большой буквы
        if self.str_input is not None:
            self.answer = self.str_input.title()

    # Метод загружает следующую вершину, используя для ее определения словарь ответов answer_dict
    def load_next_vertex(self):
        next_vertex = self.answer_dict.get(self.answer)
        if next_vertex is None:
            next_vertex = self.answer_dict.get('Else')
            if next_vertex is None:
                print('ОШИБКА. В словаре ответов вопроса ' + str(self.vertex_num) + ' отсутствует обязательный ключ Else.')
                exit()
            else:
                next_vertex.load()
        else:
            next_vertex.load()

# Класс - где ответ это целое число, которое вводится в поле ввода Entry
class Question_Number(Question_Entry):
    min = 0
    max = 1000000

    # В Конструктор класса добавлено минимальное и максимальное допустимые значения ответа целого числа
    def __init__(self, vertex_num, text, image_path, min_val, max_val, var_name, next_vertex_left_or_only: Vertex = None, next_vertex_right: Vertex = None, bracket_mode: str = None):
        super().__init__(vertex_num, text, image_path, var_name, next_vertex_left_or_only, next_vertex_right, bracket_mode)
        self.min = min_val
        self.max = max_val

    # Метод получает ответ в виде целого числа из поля ввода Entry
    def get_answer(self):
        # Получили строку, введенную в поле ввода Entry
        super().get_answer()
        # Если строка НЕ была введена, проставляем значение свойства экземпляра self.answer в None
        if self.str_input == None:
            self.answer = None
        # Если строка была введена, проверяем содержит ли она корректное значение целого числа
        else:
            match = fullmatch(r'0|[1-9]{1}\d*', self.str_input)
            # Если строка содержит НЕкорректное выражение для целого числа
            if not match:
                messagebox.showinfo('Некорректное значение', 'Введите целое число')
                self.answer = None
            # Если строка содержит корректное выражение для целого числа
            else:
                int_answer = int(self.str_input)
                # Если значение принадлежит допустимому диапазону - помещаем его в свойство экземпляра self.int_answer
                if int_answer >= self.min and int_answer <= self.max:
                    self.answer = int_answer
                else:
                    messagebox.showinfo('Значение вне допустимого диапазона', 'Значение должно быть в диапазоне от ' + str(self.min) + ' до ' + str(self.max))
                    self.answer = None

# Класс вопроса, где ответ это целое число, причем ответ сравнивается с числом-порогом и получается 2 результата сравнения (выполнения условия)
# от которых зависит выбор следующей вершины для загрузки (ветвление из 2 вариантов)
class Question_Number_Dihotomy(Question_Number):
    # Логический оператор сравнения, выполнение которого в выражении рассматривается как Истина в условии
    true_operator: str = None
    # Порог, с которым сравнивается ответ в условии
    threshold: int = None

    # В Конструктор класса добавлено значение логического оператора сравнения (для истинного условия) и порога
    def __init__(self, vertex_num, text, image_path, min_val, max_val, true_operator, threshold,  var_name, next_vertex_left_or_only: Vertex = None, next_vertex_right: Vertex = None, bracket_mode: str = None):
        super().__init__(vertex_num, text, image_path, min_val, max_val, var_name, next_vertex_left_or_only, next_vertex_right, bracket_mode)
        self.true_operator = true_operator
        self.threshold = threshold

    # Метод переопределяет родительский. Для получения ответа
    def get_answer(self):
        super().get_answer()
        if self.answer is not None:
            # Получаем рабочий оператор сравнения на языке Python
            true_operator_for_eval = self.replace_operators_for_eval(self.true_operator)
            # Получаем текст условия проверки на языке Python
            condition_for_eval = str(self.answer) + true_operator_for_eval + str(self.threshold)
            # Получаем результат проверки условия на языке Python (тип bool)
            eval_result = eval(condition_for_eval)
            # Если результат Истина - выбираем левое направление на диаграмме, иначе - правое
            if eval_result:
                self.next_load_direction = 'LEFT'
            else:
                self.next_load_direction = 'RIGHT'

    # Метод переопределяет родительский - в строку результата условия записывается результат оценки условия
    def get_condition_result_str(self):
        if self.answer is not None:
            condition_result_str = self.logic_var_name + ' ' + self.true_operator + ' ' + str(self.threshold)
            if self.next_load_direction == 'LEFT':
                self.condition_result_str = condition_result_str
            else:
                self.condition_result_str = '(' + condition_result_str + ') = False'

# Класс вопроса с номером, в котором больше 2 результатов сравнения (выполнения условия, т.е. ветвления).
# Условия и соответствующие им следующие вершины в словаре conditions_dict
class Question_Number_Many_Options(Question_Number):
    # Условия и соответствующие им следующие вершины.
    # В тексте условия переменная обозначается символом '*'
    conditions_dict: dict = None

    # В Конструктор класса добавлено значение словаря с ответами
    def __init__(self, vertex_num, text, image_path, min_val, max_val, conditions_dict,  var_name, bracket_mode: str = None):
        super().__init__(vertex_num, text, image_path, min_val, max_val, var_name, None, None, bracket_mode)
        self.conditions_dict = conditions_dict
        self.next_load_direction = 'LEFT' # Т.к. следующая вершина будет загружаться через св-во self.load_next_vertex_left_or_only (будет определено в get_condition_result_str(self))

    # Метод переопределяет родительский (по определению строки self.condition_result_str) и дополнительно определяет следующую вершину для загрузки
    def get_condition_result_str(self):
        if self.answer is not None:
            next_vertex = None
            # Цикл прохода по возможным ожидаемым условиям из словаря условий conditions_dict
            for expected_condition in self.conditions_dict:
                # В тексте условия сделали подстановку - строка с ответом вместо звездочки
                expected_condition_for_eval = expected_condition.replace('*', 'self.answer')
                # В тексте условия проверки заменили логические операторы на операторы языка Python
                expected_condition_for_eval = self.replace_operators_for_eval(expected_condition_for_eval)
                # Получаем результат проверки условия на языке Python (тип bool)
                eval_result = eval(expected_condition_for_eval)
                if eval_result == True:
                    # Определили следующую вершину для загрузки
                    next_vertex = self.conditions_dict[expected_condition]
                    self.load_next_vertex_left_or_only = next_vertex
                    # Получили строку с условием self.condition_result_str
                    self.condition_result_str = expected_condition.replace('*', self.logic_var_name)
            if next_vertex is None:
                print('В словаре условий вопроса ' + str(self.vertex_num) + ' отсутствует условие, соответствующее ответу ' + str(self.answer))
                exit()

# Класс вопроса, в котором ответ вводится выбором из 2 вариантов радиокнопки
class Question_Radio(Question):
    # Выбранная опция
    option_answer = None

    # Свойства для хранения текста надписей опций флажков радиокнопок
    option_text_1 = ""
    option_text_2 = ""

    # В Конструктор класса добавлено обновление текста радиокнопок
    def __init__(self, vertex_num, text, image_path, option_text_1, option_text_2, var_name, next_vertex_left_or_only: Vertex = None, next_vertex_right: Vertex = None, bracket_mode: str = None):
        super().__init__(vertex_num, text, image_path, var_name, next_vertex_left_or_only, next_vertex_right, bracket_mode)

        # Заполняются свойства для хранения текста надписей опций флажков радиокнопок
        self.option_text_1 = option_text_1
        self.option_text_2 = option_text_2

    # В метод загрузки добавлена деактивация строки ввода Entry и активация радиокнопок
    def load(self):
        super().load()

        # Деактивировали элемент ввода Entry
        answ_reader.grid_remove()

        # Активировали элементы ввода радиокнопки
        answ_radio_btn_1.grid()
        answ_radio_btn_2.grid()

        # Текст опций помещается в надписи радиокнопок
        answ_radio_btn_1['text'] = self.option_text_1
        answ_radio_btn_2['text'] = self.option_text_2

        # Установили переменную опций в 0 - то есть сняли выделение с обоих флажков
        r_var.set(0)

    # Метод получает ответ из радиокнопки (опция 1 или 2) и помещает его в свойство экземпляра self.option_answer
    # Метод определяет следующее направление загрузки вершин self.next_load_direction
    def get_answer(self):
        option_answer = r_var.get()
        if option_answer == 0:
            messagebox.showinfo('Надо выбрать вариант ответа', 'Выберите один из переключателей с ответом')
            self.option_answer = None
        else:
            self.option_answer = option_answer
            match self.option_answer:
                case 1:
                    self.answer = self.option_text_1
                    self.next_load_direction = 'LEFT'
                case 2:
                    self.answer = self.option_text_2
                    self.next_load_direction = 'RIGHT'

# Класс вопроса, в котором ответ вводится выбором из 2 вариантов радиокнопки, но есть только 2 варианта: ДА и НЕТ
class Y_N_Question(Question_Radio):
    # Текст радиокнопок "ДА", "НЕТ"; ответ ДА будет иметь код 1, ответ НЕТ будет иметь код 2
    def __init__(self, vertex_num, text, image_path, var_name, next_vertex_left_or_only: Vertex = None, next_vertex_right: Vertex = None, bracket_mode: str = None):
        super().__init__(vertex_num, text,  image_path, "ДА", "НЕТ", var_name, next_vertex_left_or_only, next_vertex_right, bracket_mode)

    # Метод переопределяет родительский
    def get_answer(self):
        super().get_answer()
        match self.answer:
            case 'ДА':
                self.answer = True
                self.next_load_direction = 'LEFT'
            case 'НЕТ':
                self.answer = False
                self.next_load_direction = 'RIGHT'