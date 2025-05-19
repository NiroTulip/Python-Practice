from base_vertexes import Choice, Vertex
from sys import exit
from logic import LOGIC_VARS

# Базовый класс УСЛОВНОГО ВЫБОРА (РОМБ НА СХЕМЕ)
class Condition_Choice(Choice):
    # condition_str - логическое условие выбора, которое необходимо проверить в этой вершине УСЛОВНОГО ВЫБОРА
    condition_str: str = None           # Входная строка с условием, записана на математическом языке, задается при создании через конструктор
    condition_str_for_eval: str = None  # Строка с условием, записанном на языке Питона для непосредственного вычисления условия, вычисляется методом condition_str_for_eval
    condition_result_str: str = None    # Строка с условием и его результатом, будет добавлена в правило, вычисляется в методе get_condition_result_str
    result: bool = None                 # Результат вычисления условия, вычисляется в методе get_result

    # Конструктор
    def __init__(self, vertex_num, condition_str, next_vertex_left_or_only: Vertex, next_vertex_right: Vertex):
        super().__init__(vertex_num, next_vertex_left_or_only, next_vertex_right)
        self.condition_str = condition_str
        self.set_condition_str_for_eval()

    # Метод вычисляет и устанавливает значение строки condition_str_for_eval
    def set_condition_str_for_eval(self):
        condition_str_for_eval = self.condition_str
        # Метод заменяет имя логической переменной в строке на её эквивалент в словаре LOGIC_VARS.VARS
        condition_str_for_eval = self.replace_logic_var_name_for_eval(condition_str_for_eval)
        # Метод заменяет логические операторы сравнения в строке с математического формата на формат Python для последующего вычисления условия
        condition_str_for_eval = self.replace_operators_for_eval(condition_str_for_eval)
        self.condition_str_for_eval = condition_str_for_eval

    # Метод вычисляет результат по строке condition_str_for_eval и задает направление следующей загрузки
    def get_result(self):
        print(self.condition_str_for_eval)
        self.result = eval(self.condition_str_for_eval)
        print(self.result)
        match self.result:
            case None:
                print('ОШИБКА В ВЕРШИНЕ УСЛОВНОГО ВЕТВЛЕНИЯ ' + str(self.vertex_num) + '. Выражение условия ' + self.condition_str_for_eval + ' ошибочно или одна из его переменных еще не определена (имеет тип None).')
                exit()
            case True:
                self.next_load_direction = 'LEFT'
            case False:
                self.next_load_direction = 'RIGHT'

    # Метод заменяет логические операторы конъюнкции/дизъюнкции в строке из формата Python на математический формат для выгрузки в отчет
    def replace_operators_for_report(self, input_str):
        result_str = input_str.replace(' and ', ' & ')
        result_str = result_str.replace(' AND ', ' & ')
        result_str = result_str.replace(' or ', ' || ')
        result_str = result_str.replace(' OR ', ' || ')
        return result_str

    # Метод вычисляет строку self.condition_result_str по модифицированной входной строке condition_str и результату result
    def get_condition_result_str(self):
        condition_result_str = self.condition_str
        # Замена логических операторов конъюнкции/дизъюнкции в строке из формата Python на математический формат для выгрузки в отчет
        condition_result_str = self.replace_operators_for_report(condition_result_str)
        condition_result_str = '[' + condition_result_str + ']' + ' = ' + str(self.result)
        self.condition_result_str = condition_result_str

    # Основной метод выполняет всю работу
    def load(self):
        self.get_result()
        self.get_condition_result_str()
        self.add_condition_result_to_rool()
        self.add_vertex_to_path()
        self.load_next_vertex()