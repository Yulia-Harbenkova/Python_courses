#1. написать программу которая: запрашивает у пользователя логин
#2. Есть **функция** котороя выводит сумму на счете
#3. Декорируем эту функцию декоратором который проверяет если пользователь - админ (получили на первом этапе,
#то выводит сумму счета (выполняет функ из п 2)
#4. Если не админ - Сумму не выводить (функцию даже не выполнять) а выводить - доступ запрещен 

import functools
permission_user = {'Вася': 'admin'}
login = input('Введите логин: ')
def check_summ(func):
     @functools.wraps(func)
     def wrapper_decorator():
        if login in permission_user:
            print(login, 'Ваша сумма на счете - 10')
        # Do something before
        value = func()
        # Do something after
        return value
     return wrapper_decorator 
@check_summ
def not_summ():
    return 'Доступ запрещен'


