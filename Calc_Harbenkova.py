weight = float(input())
height = float(input())
i = round(weight/(height**2))
print('Ваш индекс массы тела:', i)

scale_start = 10
scale_end = 50
l1 = i - scale_start
l2 = scale_end - i
print(scale_start, '='*l1, '|', '='*l2, scale_end, sep='')