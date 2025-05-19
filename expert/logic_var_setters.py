from base_vertexes import Vertex
from logic import LOGIC_VARS, REPORT

# Базовый класс для ВЕРШИН УСТАНОВКИ ЗНАЧЕНИЙ ВЫЧИСЛЯЕМЫХ ПЕРЕМЕННЫХ, значения которых определяются не ответами на вопросы, а вычисляются на базе других переменных
# В УСТАНОВЩИКАХ ПЕРЕМЕННЫХ происходит заполнение ВЫЧИСЛЯЕМЫХ логических переменных из словаря LOGIC_VARS.VARS
# Соответствует ОВАЛУ (с номером вершины) на схеме графа
class Logic_Var_Setter(Vertex):
    # Объект вершины, который будет загружен следующим
    load_next_vertex_only: Vertex = None
    # Имя логической переменной из LOGIC_VARS.VARS
    logic_var_name: str = None
    # Значение для установки в "логическую" переменную ИЛИ список названий переменных для вычисления их суммы
    logic_var_value = None

    # Конструктор класса
    def __init__(self, vertex_num, logic_var_name, logic_var_value, load_next_vertex_only: Vertex):
        super().__init__(vertex_num)
        self.logic_var_name = logic_var_name
        self.logic_var_value = logic_var_value
        self.load_next_vertex_only = load_next_vertex_only

    # Метод устанавливает значение логической переменной из LOGIC_VARS.VARS
    def set_logic_variable(self):
        # Подфункция непосредственно устанавливает значение лог. переменной из self.logic_var_value
        def set_logic_variable_value():
            if LOGIC_VARS.set_var(self.logic_var_name, self.logic_var_value) is None:
                print('ОШИБКА! Словарь объекта LOGIC_VARS не содержит ключа ' + self.logic_var_name)
                exit()

        # Если значение self.logic_var_value имеет значение списка - значит был передан список с названиями "логических"
        # переменных - надо предварительно получить их сумму и потом устанавливать ее в "логическую" переменную
        if isinstance(self.logic_var_value, list):
            # Если в списке последний элемент - число, то передаем список без него, а его - как множитель
            if isinstance(self.logic_var_value[-1], int):
                factor = self.logic_var_value[-1]
                self.logic_var_value = LOGIC_VARS.get_vars_summ(self.logic_var_value[:-1], factor)

            # Если в списке последний элемент НЕ число, то просто передаем список
            else:
                self.logic_var_value = LOGIC_VARS.get_vars_summ(self.logic_var_value)

            # После установки значения self.logic_var_value вызвали подфункцию установки значения "логической" переменной
            set_logic_variable_value()

        # Если значение self.logic_var_value имеет значение типа str, то в него передана строка с логическим условием,
        # которе надо проверить и получить результат типа bool
        elif isinstance(self.logic_var_value, str):
            condition = self.logic_var_value
            condition = self.replace_logic_var_name_for_eval(condition)
            condition = self.replace_operators_for_eval(condition)
            self.logic_var_value = eval(condition)

            # После установки значения self.logic_var_value вызвали подфункцию установки значения "логической" переменной
            set_logic_variable_value()

        # Если значение self.logic_var_value имеет значение типа int или bool - устанавливаем это значение в "логическую" переменную
        else:
            set_logic_variable_value()

    # Метод добавляет в переменную отчета Правила REPORT.ROOL значение реализованного условия текущей вершины
    def add_condition_result_to_rool(self):
        condition_result_str = ' ≡ ' + self.logic_var_name + ' = ' + str(self.logic_var_value)
        REPORT.add_condition_to_rool(condition_result_str, True)

    # Метод добавляет имя переменной текущего вопроса и её значение в список значений переменных REPORT.VAR_VALUES_FOR_REPORT (для отчета)
    def add_var_value_to_report(self):
        var_value_str = LOGIC_VARS.get_var_value_str(self.logic_var_name)
        if var_value_str is None:
            print('ОШИБКА! Словарь объекта LOGIC_VARS не содержит ключа ' + self.var_name)
            exit()
        else:
            # Метод добавляет имя переменной и её значение в список значений переменных REPORT.VAR_VALUES_FOR_REPORT (для отчета)
            var_value_str = var_value_str + ' (вычисляемая переменная)'
            REPORT.add_var_value(var_value_str)

    # Метод загрузки следующей вершины
    def load_next_vertex(self):
        if self.load_next_vertex is not None:
            self.load_next_vertex_only.load()

    # Метод загрузки самого объекта и выполнение всей работы
    def load(self):
        self.set_logic_variable()
        self.add_vertex_to_path()
        self.add_condition_result_to_rool()
        self.add_var_value_to_report()
        self.load_next_vertex()