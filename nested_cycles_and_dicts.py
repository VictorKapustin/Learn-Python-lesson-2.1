# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
names = {}
for dict in students:
    for key, value in dict.items():
        if value in names:
            names[value]+=1
        else:
            names[value]=1
for key, value in names.items():
    print('{}: {}'.format(key, value))
print()

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
  {'first_name': 'Оля'},
  {'first_name': 'Оля'},
]
names = {}
for dict in students:
    for key, value in dict.items():
        if value in names:
            names[value]+=1
        else:
            names[value]=1
most_common = [k for k in sorted(names.keys(), key=names.get, reverse=True)][0]
print('Самое частое имя среди учеников: {}'.format(most_common), '\n')
        

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
names = {}
klass_count = 1
for klass in school_students:
    for dict in klass:
        for key, value in dict.items():
            if value in names:
                names[value]+=1
            else:
                names[value]=1
    most_common = [k for k in sorted(names.keys(), key=names.get, reverse=True)][0]
    print('Самое частое имя в классе {}: {}'.format(klass_count, most_common))
    names = {}
    klass_count += 1
print()

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for klass in school:
    
    devochki = 0
    malchiki = 0
    for student in klass['students']:
        
        if is_male[student['first_name']]==True:
            malchiki += 1
        else:
            devochki += 1
    print('В классе {} {} девочки и {} мальчика.'.format(klass['class'], devochki, malchiki), )    
print()
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
  {'class': '4b', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}]}
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
dev = {}
mal = {}
for klass in school:
    devochki = 0
    malchiki = 0
    for student in klass['students']:
        
        if is_male[student['first_name']]==True:
            malchiki += 1
        else:
            devochki += 1
    dev[klass['class']] = devochki
    mal[klass['class']] = malchiki
print('Больше всего мальчиков в классе {}'.format([k for k in sorted(mal.keys(), key=mal.get, reverse=True)][0]))
print('Больше всего девочек в классе {}'.format([k for k in sorted(dev.keys(), key=dev.get, reverse=True)][0]))    

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a