from questions import *
from base_vertexes import Stub
from conclusions import Conclusion_Role, Conclusion_Deny
from condition_choices import Condition_Choice
from logic_var_setters import Logic_Var_Setter

# Объекты. Номер вопроса в названии соответствует номеру вершины в графе.-----------------------------
# Заглушка для тех вариантов, которые еще не реализованы программно
STUB = Stub(999)

# Стадия ветвления возможных вариантов
Conclusion_151 = Conclusion_Role(151, "Эпизодическая роль в топовом фильме")
Conclusion_150 = Conclusion_Role(150, "Роль 3 плана в топовом фильме")
CC_149 = Condition_Choice(149, 'DEGREE >= 2 and SUMM_EXAM >= 10 and SUMM_SKILL >= 10', Conclusion_150, Conclusion_151)
Conclusion_148 = Conclusion_Role(148, "Роль 2 плана в топовом триллере")
Conclusion_147 = Conclusion_Role(147, "Роль 2 плана в топовом историческом фильме")
CC_146 = Condition_Choice(146, 'SUMM_INTELLECT >= 15 and SUMM_BEAUTY >= 17', Conclusion_147, Conclusion_148)
Conclusion_145 = Conclusion_Role(145, "Роль 1 плана в топовом триллере")
Conclusion_144 = Conclusion_Role(144, "Роль 1 плана в топовом историческом фильме")
CC_143 = Condition_Choice(143, 'SUMM_DOP_SKILL >= 15 and SUMM_BEAUTY >= 17', Conclusion_144, Conclusion_145)
CC_142 = Condition_Choice(142, 'DEGREE >= 2 and SUMM_EXAM >= 15 and SUMM_SKILL >= 15', CC_143, CC_146)
Q_141 = Y_N_Question(141, "Участие в фильмах со звездами третьей величины?", "img/141.jpg", 'THIRD_STAR_PART', CC_142, CC_149)
Conclusion_140 = Conclusion_Role(140, "Роль 2 плана в топовом политическом фильме")
Conclusion_139 = Conclusion_Role(139, "Роль 1 плана в топовом фантастическом фильме")
CC_138 = Condition_Choice(138, 'SUMM_INTELLECT >= 10 and IS_RECOMMENDED = True', Conclusion_139, Conclusion_140)
Conclusion_137 = Conclusion_Role(137, "Роль 1 плана в топовом фильме про спорт")
CC_136 = Condition_Choice(136, 'SUMM_PHYSICAL >= 20', Conclusion_137, CC_138)
Conclusion_135 = Conclusion_Role(135, "Роль симпатяжки 2 плана в топовом фильме")
CC_134 = Condition_Choice(134, 'SUMM_BEAUTY >= 22', Conclusion_135, CC_136)
Conclusion_133 = Conclusion_Role(133, "Роль 3 плана в топовом фильме")
Conclusion_132 = Conclusion_Role(132, "Роль 2 плана в топовом ужастике")
CC_131 = Condition_Choice(131, 'SUMM_MENTAL_STRENGTH >= 15', Conclusion_132, Conclusion_133)
Conclusion_130 = Conclusion_Role(130, "Роль 2 плана в топовом боевике")
CC_129 = Condition_Choice(129, 'SUMM_PHYSICAL >= 15 and SUM_GUNS >= 10', Conclusion_130, CC_131)
Conclusion_128 = Conclusion_Role(128, "Комедийная роль 2 плана в топовом фильме")
CC_127 = Condition_Choice(127, 'SUMM_DOP_SKILL >= 15 and IS_RECOMMENDED = True', Conclusion_128, CC_129)
Conclusion_126 = Conclusion_Role(126, "Роль симпатяжки 2 плана в топовом фильме")
CC_125 = Condition_Choice(125, 'SUMM_BEAUTY >= 22', Conclusion_126, CC_127)
Conclusion_124 = Conclusion_Role(124, "Роль 2 плана в топовом детективе")
Conclusion_123 = Conclusion_Role(123, "Роль 2 плана в топовом приключенческом фильме")
CC_122 = Condition_Choice(122, 'SUMM_BEAUTY >= 18', Conclusion_123, Conclusion_124)
Conclusion_121 = Conclusion_Role(121, "Роль 1 плана в топовом боевике")
CC_120 = Condition_Choice(120, 'SUMM_PHYSICAL >= 15 and SUM_GUNS >= 10', Conclusion_121, CC_122)
Conclusion_119 = Conclusion_Role(119, "Комедийная роль 1 плана в топовом фильме")
CC_118 = Condition_Choice(118, 'SUMM_DOP_SKILL >= 15', Conclusion_119, CC_120)
Conclusion_117 = Conclusion_Role(117, "Драматическая роль 1 плана в топовом фильме")
CC_116 = Condition_Choice(116, 'SUMM_INTELLECT >= 15 and IS_RECOMMENDED = True', Conclusion_117, CC_118)
CC_115 = Condition_Choice(115, 'DEGREE = 3 and SUMM_EXAM >= 15 and SUMM_SKILL >= 15', CC_116, CC_125)
Q_114 = Y_N_Question(114, "Участие в фильмах со звездами второй величины?", "img/114.jpg", 'SECOND_STAR_PART', CC_115, CC_134)
Conclusion_113 = Conclusion_Role(113, "Роль 2 плана в топовом фильме")
Conclusion_112 = Conclusion_Role(112, "Роль 1 плана в топовом ужастике")
CC_111 = Condition_Choice(111, 'SUMM_MENTAL_STRENGTH >= 15',  Conclusion_112, Conclusion_113)
Conclusion_110 = Conclusion_Role(110, "Роль 1 плана в топовом военном фильме")
Q_109 = Y_N_Question(109, "Хорошо смотрится в военной форме?", "img/109.jpg", 'IS_GOOD_LOOK_MILITARY_UNIFORM', Conclusion_110, CC_111)
Conclusion_108 = Conclusion_Role(108, "Роль 1 плана в топовом фильме")
Q_107 = Question_Number_Dihotomy(107, "Общий хронометраж эпизодов, мин?", "img/107.jpg", 0, 100000, '≥', 60, 'FOOTAGE_TIMING_MIN', Conclusion_108, Q_109)
Conclusion_106 = Conclusion_Role(106, "Роль 1 плана в топовом политическом фильме")
Conclusion_105 = Conclusion_Role(105, "Роль 1 плана в топовом историческом фильме")
Q_104 = Y_N_Question(104, "Хорошо смотрится в платье 19 века?", "img/104.jpg", 'IS_GOOD_LOOK_ANTIQUE_DRESS', Conclusion_105, Conclusion_106)
Conclusion_103 = Conclusion_Role(103, "Роль 1 плана в топовом приключенческом фильме")
CC_102 = Condition_Choice(102, 'AGE <= 45 and SUMM_BEAUTY >= 16 and SUMM_DOP_SKILL >= 15',  Conclusion_103, Q_104)
Conclusion_101 = Conclusion_Role(101, "Роль 1 плана в топовом фильме")
Q_100 = Y_N_Question(100, "Были номинации на Оскар?", "img/100.jpg", 'IS_OSCAR', Conclusion_101, CC_102)
Q_99 = Y_N_Question(99, "Наличие наград?", "img/99.jpg", 'IS_AWARDS', Q_100, Q_107)
Conclusion_328 = Conclusion_Role(97, "Роль 2 плана в топовом фильме")
Conclusion_327 = Conclusion_Role(327, "Роль учительницы в топовом фильме")
Conclusion_326 = Conclusion_Role(326, "Роль китайской шпионки в топовом фильме")
Conclusion_325 = Conclusion_Role(325, "Роль немецкой шпионки в топовом фильме")
Conclusion_324 = Conclusion_Role(324, "Роль американской шпионки в топовом фильме")
Q_323_answer_dict = {
    'английский': Conclusion_324,
    'немецкий': Conclusion_325,
    'китайский': Conclusion_326,
    'ELSE': Conclusion_327
    }
Q_323 = Question_Str(107, "Какой язык знает?", "img/38.jpg", Q_323_answer_dict, 'FOREIGN_LANG')
CC_98 = Condition_Choice(98, 'FOREIGN_LANG = True', Q_323, Conclusion_328)
Conclusion_97 = Conclusion_Role(97, "Роль 1 плана в топовом приключенческом фильме")
CC_96 = Condition_Choice(96, '( SUMM_DOP_SKILL >= 15 OR SUMM_PHYSICAL >= 15 ) AND IS_RECOMMENDED = True', Conclusion_97, CC_98)
Conclusion_95 = Conclusion_Role(95, "Роль 1 плана в топовом фильме церебрал муви")
CC_94 = Condition_Choice(94, 'SUMM_INTELLECT >= 20', Conclusion_95, CC_96)
Conclusion_93 = Conclusion_Role(93, "Роль Тринити в Матрице")
CC_92 = Condition_Choice(92, 'AGE >= 33 and HANDLE_AUTO = True and HANDLE_MOTO = True and HANDLE_GUN = True and HANDLE_MACHINEGUN = True and IS_MARTIAL_ARTS = True', Conclusion_93, CC_94)
Conclusion_91 = Conclusion_Role(91, "Роль английской королевы")
Conclusion_90 = Conclusion_Role(90, "Роль Маргаретт Тэтчер")
CC_89 = Condition_Choice(89, 'AGE <= 60', Conclusion_90, Conclusion_91)
Conclusion_88 = Conclusion_Role(88, "Роль училки в топовом фильме")
Conclusion_87 = Conclusion_Role(87, "Роль Сарры Коннор")
CC_86 = Condition_Choice(86, 'SUMM_PHYSICAL >= 10 and SUMM_GUNS >= 10 and SUMM_TECH >= 10', Conclusion_87, Conclusion_88)
CC_85 = Condition_Choice(85, 'AGE <= 45', CC_86, CC_89)
Conclusion_84 = Conclusion_Role(84, "Роль бизнесвумен 1 плана в топовом фильме")
Conclusion_83 = Conclusion_Role(83, "Роль симпатяжки 1 плана в топовом фильме")
CC_82 = Condition_Choice(82, 'SUMM_BEAUTY >= 24', Conclusion_83, Conclusion_84)
Conclusion_81 = Conclusion_Role(81, "Роль девушки Бена Аффлека")
Conclusion_80 = Conclusion_Role(80, "Роль девушки Эштона Катчера")
CC_79 = Condition_Choice(79, 'IS_TALL = TRUE', Conclusion_80, Conclusion_81)
Conclusion_78 = Conclusion_Role(78, "Роль девушки Леонардо ди Каприо")
CC_77 = Condition_Choice(77, 'ACTOR_ETUDE >= 4 and EMOTION_SKILL >= 4 and BEAUTY_SMILE = TRUE', Conclusion_78, CC_79)
Conclusion_76 = Conclusion_Role(76, "Роль девушки Брэда Питта")
CC_75 = Condition_Choice(75, 'GOOD_KISS = TRUE and BEAUTY_SCALE ≥ 8', Conclusion_76, CC_77)
Conclusion_74 = Conclusion_Role(74, "Роль девушки Тома Круза")
Conclusion_73 = Conclusion_Role(73, "Роль девушки Джеймса Бонда")
CC_72 = Condition_Choice(72, 'IS_TALL = TRUE', Conclusion_73, Conclusion_74)
CC_71 = Condition_Choice(71, 'HANDLE_AUTO = TRUE and SUMM_PHYSICAL >=5', CC_72, CC_75)
CC_70 = Condition_Choice(70, 'SUMM_BEAUTY >= 15 and SUMM_DOP_SKILL >= 10 and SUMM_INTELLECT >= 10', CC_71, CC_82)
CC_69 = Condition_Choice(69, 'AGE <= 35', CC_70, CC_85)
CC_68 = Condition_Choice(68, 'DEGREE = 3 and SUMM_EXAM >= 15 and SUMM_SKILL >= 15', CC_69, CC_92)
Q_67 = Y_N_Question(67,"Участие в фильмах со звездами первой величины?", "img/67.jpg", 'SUPER_STAR_PART', CC_68, Q_99)
Q_66_condition_dict = {
    '*<4': Q_141,
    '4≤*≤7': Q_114,
    '*>7': Q_67,
    }
Q_66 = Question_Number_Many_Options(66,"IMDb рейтинг самого удачного фильма (0-10)?", "img/66.jpg", 0, 10, Q_66_condition_dict, 'IMDB_RATING')
LVS_65 = Logic_Var_Setter(65, 'SUCCESS', 10, Q_66)
Q_64 = Y_N_Question(64,"Коммерческий успех в прокате?", "img/64.jpg", 'IS_COMMERCIAL_SUCCESS', LVS_65, STUB, ')')
Q_63 = Question_Radio(63,"Фильм коммерческий/артхаусный?", "img/63.jpg", "Коммерческий", "Артхаусный", 'IS_COMMERCIAL_MOVIE', Q_64, STUB, '(')
LVS_62 = Logic_Var_Setter(62, 'EXPERIENCE', 7, Q_63)
Q_61 = Question_Radio(61,"Фильм полнометражный/короткометражный?", "img/61.jpg", "Полнометражный", "Короткометражный", 'IS_FULL_MOVIE', LVS_62, STUB, ')')
Q_60 = Question_Radio(60,"Фильм профессиональный/любительский?", "img/60.jpg", "Профессиональный", "Любительский", 'IS_MOVIE_PROF', Q_61, STUB)
Q_59 = Y_N_Question(59,"Есть ли опыт в съёмках?", "img/59.jpg", 'IS_MOVIE_EXP', Q_60, STUB, '(')
# Стадия ветвления возможных вариантов закончена

# БЛОК ОЦЕНКИ ВЛАДЕНИЯ ОРУЖИЕМ
LVS_58 = Logic_Var_Setter(58, 'SUMM_GUNS', ['HANDLE_GUN', 'HANDLE_MACHINEGUN', 'HANDLE_GRENADER', 'HANDLE_FLAMER', 5], Q_59)
Q_57 = Y_N_Question(57,"Умеет стрелять из огнемета?", "img/57.jpg", 'HANDLE_FLAMER', LVS_58, None, ')')
Q_56 = Y_N_Question(56,"Умеет стрелять из гранатомета?", "img/56.jpg", 'HANDLE_GRENADER', Q_57)
Q_55 = Y_N_Question(55,"Умеет стрелять из автомата?", "img/55.jpg", 'HANDLE_MACHINEGUN', Q_56)
Q_54 = Y_N_Question(54,"Умеет стрелять из пистолета?", "img/54.jpg", 'HANDLE_GUN', Q_55, None, '(')

# БЛОК ОЦЕНКИ ПСИХОЛОГИЧЕСКОЙ УСТОЙЧИВОСТИ
LVS_53 = Logic_Var_Setter(53, 'SUMM_MENTAL_STRENGTH', ['NOT_SCARY_BLOOD', 'NOT_SCARY_CORPSES', 'NOT_SCARY_REMAINS', 'NOT_SCARY_INSECTS', 5], Q_54)
Q_52 = Y_N_Question(52,"Отсутствует боязнь насекомых?", "img/52.jpg", 'NOT_SCARY_INSECTS', LVS_53, None, ')')
Q_51 = Y_N_Question(51,"Отсутствует боязнь останков (муляжи)?", "img/51.jpg", 'NOT_SCARY_REMAINS', Q_52)
Q_50 = Y_N_Question(50,"Отсутствует боязнь трупов (муляжи)?", "img/50.jpg", 'NOT_SCARY_CORPSES', Q_51)
Q_49 = Y_N_Question(49,"Отсутствует боязнь крови (искусств.)?", "img/49.jpg", 'NOT_SCARY_BLOOD', Q_50, None, '(')

# БЛОК ОЦЕНКИ ТЕХНИЧЕСКИХ НАВЫКОВ
LVS_48 = Logic_Var_Setter(48, 'SUMM_TECH', ['HANDLE_AUTO', 'HANDLE_MOTO', 'HANDLE_HYDRO', 'HANDLE_BIKE', 5], Q_49)
Q_47 = Y_N_Question(47,"Умение кататься на велосипеде?", "img/47.jpg", 'HANDLE_BIKE', LVS_48, None, ')')
Q_46 = Y_N_Question(46,"Умение водить гидроцикл?", "img/46.jpg", 'HANDLE_HYDRO', Q_47)
Q_45 = Y_N_Question(45,"Умение водить мотоцикл?", "img/45.jpg", 'HANDLE_MOTO', Q_46)
Q_44 = Y_N_Question(44,"Умение водить автомобиль?", "img/44.jpg", 'HANDLE_AUTO', Q_45, None, '(')

# БЛОК ОЦЕНКИ ИНТЕЛЛЕКТУАЛЬНЫХ СПОСОБНОСТЕЙ
LVS_43 = Logic_Var_Setter(43, 'SUMM_INTELLECT', ['KNOW_FOREIGN_LANG', 'IS_SMART', 'GOOD_MEMORY', 'HIGH_EMOTIONAL_INTELLIGENCE', 5], Q_44)
Q_42 = Y_N_Question(42,"Способность убедительно врать?", "img/42.jpg", 'HIGH_EMOTIONAL_INTELLIGENCE', LVS_43, None, ')')
Q_41 = Y_N_Question(41,"Быстро запоминает большие тексты?", "img/41.jpg", 'GOOD_MEMORY', Q_42)
LVS_40 = Logic_Var_Setter(40, 'IS_SMART', 'IQ_LEVEL > 110', Q_41)
Q_39 = Question_Number(39,"Уровень IQ (0-160)?", "img/39.jpg", 0, 160, 'IQ_LEVEL', LVS_40)
Q_38 = Y_N_Question(38,"Знание иностранных языков?", "img/38.jpg", 'KNOW_FOREIGN_LANG', Q_39, None, '(')

# БЛОК ОЦЕНКИ ФИЗИЧЕСКОЙ ПОДГОТОВКИ
LVS_37 = Logic_Var_Setter(37, 'SUMM_PHYSICAL', ['IS_PRACTICE_SPORT', 'IS_SHAPED_MUSCLES', 'IS_MARTIAL_ARTS', 'IS_PERFORM_STUNTS',  5], Q_38)
Q_36 = Y_N_Question(36,"Делает трюки сама?", "img/36.jpg", 'IS_PERFORM_STUNTS', LVS_37, None, ')')
Q_35 = Y_N_Question(35,"Владение боевыми искусствами?", "img/35.jpg", 'IS_MARTIAL_ARTS', Q_36)
Q_34 = Y_N_Question(34,"Мышцы подкачены?", "img/34.jpg", 'IS_SHAPED_MUSCLES', Q_35)
Q_33 = Y_N_Question(33,"Занимается спортом или гимнастикой?", "img/33.jpg", 'IS_PRACTICE_SPORT', Q_34, None, '(')

# БЛОК ОЦЕНКИ ФИЗИЧЕСКОЙ ПРИВЛЕКАТЕЛЬНОСТИ
LVS_32 = Logic_Var_Setter(32, 'SUMM_BEAUTY', ['IS_BEAUTY_SHAPE','IS_BEAUTY_SMILE','IS_TALL','BEAUTY_SCALE', 3], Q_33)
Q_31 = Question_Number(31,"Красота по 7 балльной шкале?", "img/31.jpg", 1, 7, 'BEAUTY_SCALE', LVS_32, None, ')')
LVS_30 = Logic_Var_Setter(30, 'IS_TALL', 'HEIGHT ≥ 172', Q_31)
Q_29 = Question_Number(29,"Рост, см?", "img/29.jpg", 100, 250, 'HEIGHT', LVS_30, None, '()')
Q_28 = Y_N_Question(28,"Красивая улыбка?", "img/28.jpg", 'IS_BEAUTY_SMILE', Q_29)
Q_27 = Y_N_Question(27,"Красивая фигура?", "img/27.jpg", 'IS_BEAUTY_SHAPE', Q_28, None, '(')

# БЛОК ОЦЕНКИ ДОПОЛНИТЕЛЬНЫХ ПРОФЕССИОНАЛЬНЫХ НАВЫКОВ
LVS_26 = Logic_Var_Setter(26, 'SUMM_DOP_SKILL', ['IS_GOOD_KISS', 'IS_GOOD_DRUNK', 'IS_GOOD_FAINT', 'IS_GOOD_SLAP', 5], Q_27)
Q_25 = Y_N_Question(25,"Умеет красиво давать пощёчины?", "img/25.jpg", 'IS_GOOD_SLAP', LVS_26, None, ')')
Q_24 = Y_N_Question(24,"Умеет красиво падать в обморок?", "img/24.jpg", 'IS_GOOD_FAINT', Q_25)
Q_23 = Y_N_Question(23,"Умеет изображать пьяную?", "img/23.jpg", 'IS_GOOD_DRUNK', Q_24)
Q_22 = Y_N_Question(22,"Умеет красиво целоваться?", "img/22.jpg", 'IS_GOOD_KISS', Q_23, None, '(')

# БЛОК ОЦЕНКИ ОСНОВНЫХ ПРОФЕССИОНАЛЬНЫХ КАЧЕСТВ
LVS_21 = Logic_Var_Setter(21, 'SUMM_SKILL', ['IMPROV_SKILL', 'TEXT_SKILL', 'EMOTION_SKILL', 'GESTURE_SKILL'], Q_22)
Q_20 = Question_Number(20,"Способность к импровизации(1-5 баллов)?", "img/20.jpg", 1, 5, 'IMPROV_SKILL', LVS_21, None, ')')
Q_19 = Question_Number(19,"Уровень работы с текстом (1-5 баллов)?", "img/19.jpg", 1, 5, 'TEXT_SKILL', Q_20)
Q_18 = Question_Number(18,"Уровень владения эмоциями (1-5 баллов)?", "img/18.jpg", 1, 5, 'EMOTION_SKILL', Q_19)
Q_17 = Question_Number(17,"Уровень владения жестами (1-5 баллов)?", "img/17.jpg", 1, 5, 'GESTURE_SKILL', Q_18, None, '(')

# БЛОК ОЦЕНКИ ЭКЗАМЕНАЦИОННЫХ ИСПЫТАНИЙ
LVS_16 = Logic_Var_Setter(11, 'SUMM_EXAM', ['ART_READING', 'ACTOR_ETUDE', 'CHOREOGRAPHY', 'VOCAL'], Q_17)
Q_15 = Question_Number(15,"Оценка по вокалу (1-5 баллов)?", "img/15.jpg", 1, 5, 'VOCAL', LVS_16, None, ')')
Q_14 = Question_Number(14,"Оценка по хореографии (1-5 баллов)?", "img/14.jpg", 1, 5, 'CHOREOGRAPHY', Q_15)
Q_13 = Question_Number(13,"Оценка за актерский этюд (1-5 баллов)?", "img/13.jpg", 1, 5, 'ACTOR_ETUDE', Q_14)
Q_12 = Question_Number(12,"Оценка за художественное чтение (1-5 баллов)?", "img/12.jpg", 1, 5, 'ART_READING', Q_13, None, '(')

# БЛОК ОЦЕНКИ ОБРАЗОВАНИЯ
LVS_11 = Logic_Var_Setter(11, 'DEGREE', 0, Q_12)
LVS_10 = Logic_Var_Setter(10, 'DEGREE', 1, Q_12)
LVS_9 = Logic_Var_Setter(9, 'DEGREE', 2, Q_12)
LVS_8 = Logic_Var_Setter(8, 'DEGREE', 3, Q_12)
Q_7 = Y_N_Question(7,"Пройдены ли курсы актерского мастерства?", "img/7.jpg","IS_ACTOR_COURSE",LVS_10,LVS_11,')')        # Актерские курсы
Q_6 = Question_Radio(6,"Степень магистра или бакалавра?","img/6.jpg","Магистр","Бакалавр","DEGREE_TYPE",LVS_8,LVS_9,')') # Степень
Q_5 = Y_N_Question(5,"Есть ли высшее актерское образование?", "img/5.jpg", "IS_EDUCATED", Q_6, Q_7, '(')                 # ОБРАЗОВАНИЕ
Conclusion_4 = Conclusion_Deny(4,"Вам пора на заслуженный отдых.")
Conclusion_3 = Conclusion_Deny(3,"Вас ждут в ТЮЗе.")
# ПРЕДВАРИТЕЛЬНЫЙ ОПРОС
Q_2_condition_dict = {
    '*<18':Conclusion_3,
    '*>80': Conclusion_4,
    '18≤*≤80': Q_5
    }
Q_2 = Question_Number_Many_Options(2,"Введите свой возраст:", "img/2.jpg", 1, 150, Q_2_condition_dict, "AGE")  # ВОЗРАСТ
Q_1 = Y_N_Question(1,"Есть ли рекомендации?", "img/1.jpg", "IS_RECOMMENDED", Q_2)