num1 = int(input())
num2 = int(input())
num3 = int(input())

#Если нет ни одого нуля - вывести: "Нет нулевых значений!!!"(Без if - использовать лень)
num1 > 0 and num2 > 0 and num3 > 0 and print('Нет нулевых значений!!!')

#Вывести первое ненулевое значение. Если введены все нули - вывести "Введены все нули!" (цикл не использовать) без if - использовать лень
num1 > 0 and (num2 == 0 or num2 > 0) and (num3 == 0 or num2 > 0) and print('Первое не нулевое значение', num1) \
or num1 == 0 and num2 > 0 and (num3 == 0 or num3 > 0) and print('Первое не нулевое значение', num2) \
or num1 == 0 and num2 == 0 and num3 > 0 and print('Первое не нулевое значение', num3) \
or num1 == 0 and num2 == 0 and num3 == 0 and print('Введены все нули!')

#Если первое значение больше чем сумма второго и третьего вывести a - b - c
if num1 > num2 + num3:
    print('a - b - c =', num1 - num2 - num3)

#Если первое значение меньше чем сумма второго и третьего вывести b + c - a
if num1 < num2 + num3:
    print('b + c + a =', num2 + num3 - num1)

#Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася"
if num1 > 50 and num2 > num1 or num3 > num1:
    print('Вася')

#Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"
if num1 > 5 or num2 == num3 == 7:
    print('Петя')