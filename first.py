"""
Представленная функция isEven читаема для пользователя, незнакомого с языком python,
т.к. '%' - довольно частое обозначение операции взятия остатка.
Функции isEven_2 и isEven_3 не настолько интуитивно понятны, но работают быстрее.
"""
def isEven(value):
    return value%2==0

def isEven_2(value):
    return value&1 == 0

def isEven_3(value):
    return value|1 != value
