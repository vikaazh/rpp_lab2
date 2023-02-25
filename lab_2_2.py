#Задание 2.3 п.1 Считать с клавиатуры произвольную строку
my_string = input("Вы. ввели. число. и. текст.: ")
print("Введите произвольную строку : ", my_string)

#Задание 2.3 п.2 Удалить из строки все символы точки
my_string="Вы. ввели. число. и. текст."
string_cp = my_string.replace('.', '')
print(string_cp)

#Задание 2.3 п.3 Вывести в консоль количество удаленных символов
my_string="Вы. ввели. число. и. текст."
count = len(my_string) - len(my_string.replace('.', ''))
print(my_string)
print(str(count))
#Задание 2.3 п.4 Вывести в консоль полученную строку
my_string = input()
print(my_string.replace('.', ''))

