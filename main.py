def task1(num):
    num = int(num)
    x = [2, 3, 4, 5, 6]
    if num in x:
        print('Поздравляю, Вы угадали число!')
    else:
        print('Нет такого числа!')


def task2():
    ls = [7, 9, 3, 8, 3]
    duplicate = {str(x) for x in ls if ls.count(x) > 1}
    x = lambda: print('nothing')
    y = lambda: print(' '.join(duplicate))
    x() if len(duplicate) < 1 else y()


def task3():
    week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sun', 'Sut')
    weekends = int(input())
    print('Weekends:', week[:-weekends - 1:-1])
    print('Work days:', week[:-weekends])
    print()
 def task4():
     students = [ 'Грищенко', 'Козлов', 'Сидоров' ' Васюткин' ,' Бондаренко' ]
     students = [  ' Иванов ', 'Cтиценко' , 'Любимов' , 'Веркина']
     sport_team = tuple ( sample ( students1, 5)) + tuple( sample (students2, 5))
     print('Исходящий список первой группы :' ,*students1)
     print( ' Исходящий список второй групы :' , * students2)
     print( ' Список спортивный команды :', *sorted(sport_team))
     print( 'Колличество человек в спортивной команде : ,' len(sport_team))
     if 'Козлов' in sport_team
     print(f ' Козлов входит в список спортивной команды , его фамилия встречается {sport_team.count("Козлов")} раз ' )
     else:
         print(' Лозлов в списке спортивной команды не входит ')