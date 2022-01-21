import re

TestPositive = ['Мама', 'авТо', 'гриБ', 'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО']
TestNegative = ['агент007','стриж','ГТО','Три богатыря', 'КБавангард', '5g', 'b2b', 'B2b', 'B2B']

def check(word):
 match = re.fullmatch(r'[а-я]*[А-Я]{1}[а-я]*', word)

 print(word, 'YES' if match else 'NO')

for element in TestPositive:
 check(element)

for element in TestNegative:
 check(element)
