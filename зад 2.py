#


place = int(input('Введите номер места'))
if(place<=0 or place>55): print('Место введено неверно')
else:
    if(place>36 and place<55):
        if(place%2== 0): print('< Боковое верхнее')
        else:print('Боковое верхнее')
    else:
        if(place % 2 == 0 ): print('Верхнее')
        else:print('Нижнее')