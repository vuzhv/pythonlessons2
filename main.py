# Переменні - ячейка в памято яку можна занести інформацію а потім з нею працювати
# назва може бути якою завгодно але не використовувати спеціальні символи ?*; (назву краще обирати по смислу)
number = 5 #int
print("Результат : ", number)

number = 7
print("Результат : ", number)
#в ході коду можна змінювати значення переменної
del number
#del видалення переменної

digit = 0.35325 #float
word = "Результат : " #string
print(word, digit)
#в переменних можна хранити строки(символ або багато символів), числа( с точкою, цілі відємні та додатні)

boolean = True #bool
#bool true or false, проверка
print(boolean)

# немає типізації при создаванні переменної не потрібно вказувати тип данних але він є
# bool string int float

print(word + str(boolean))
str_num = '5'
print(word + str(digit + float(str_num)))
# Привидение типів данних str int bool float
# str - приводить число до строки
# int - приводить строку до числа


num1 = int(input("Введіть перше число :"))
num2 = int(input("Введіть друге число :"))
#int(intput) сразу преображаєм в числа
num1 += 5
# += сразу добавляє якесь число так же *= /= -=

print("Result :", num1 + num2)
print("Result :", num1 - num2)
print("Result :", num1 * num2)
print("Result :", num1 / num2)
print("Result :", num1 ** num2)
print("Result :", num1 // num2)

word = "Hi" #string
print(word * 2)
#можна помножити строку вона буде виводитись два рази

word = 45
# одну й ту саму переменну можна використовувати багато разів та змінювати тип вона буде сама видалятися





