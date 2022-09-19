#  1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
# 30/2=15  15/3=5  5/5=1   [2,3,5]


# n = int(input("Введите число: "))
# '''пользователь вводит число N'''
# factors = []
# '''Создали пустой список, куда в дальнейшем будут записываться простые множители N'''
# d = 2
# m = n 
# while d * d <= n:
#         '''Находим в цикле while простые множители числа N'''
#         if n % d == 0:
#             factors.append(d)
#             n//=d
#         else:
#             d =d+1
# factors.append(n)
# '''Присоединяем n к m и все в список на выход'''
# print('{} = {}' .format(m, factors)) 

# ---------------------------------------------------------------------------------------------------------------------------



# 2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.


# numbers=list(map(int,input("Введите значения через пробел: ").split()))
# """Загоняем данные от пользователя в лист , через пробел"""

# def get_unique_numbers(numbers):
#     '''Создали функцию по нахождению уникальный значений в нашем списке '''
#     unik_list = []

#     for number in numbers:
#         if number in unik_list:
#             continue
#             '''пока числа от пользователя есть в unik_list , мы продолжаем цикл'''
#         else:
#             unik_list.append(number)
#             '''Как только число уникальное, мы записываем его в unik_list'''
#     return unik_list

# print(get_unique_numbers(numbers))

# # ---------------------------------------------------------------------------------------------------------------------------------------------------

# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3

# def turn_to_int(element):
#     if element.isdigit():
#         return int(element)
#     return element


# def read_file(filename):
#     with open(filename,  encoding='utf-8') as file:
#         names=file.read().split('\n')
#     return names
# def highlight_names(names):
#     for i, record in enumerate(names):
#         record=record.rsplit(' ',maxsplit=1)
#         names[i]=list(map(turn_to_int, record))

#         if names[i][-1]==5:
#             names[i][0]=record[0].upper()

#     return names

# names= read_file('text.txt')
# names=highlight_names(names)

# print(names)
# flat_1=[x for l in names for x in l]
# print(flat_1)

# with open("text.txt","w", encoding='utf-8') as file:
#     print(*flat_1, file=file, sep="\n")
 
# ---------------------------------------------------------------------------
    



# 4,5 задача не выполнена 

