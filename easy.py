# __author__ = 'Екомасова Ксения Алексеевна'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

print("Выводим поочередно цифры")

answer = ""
while answer != "q":
	answer = input("Введите число  или 'q' для выхода: ")
	for i in answer:
		print(i)
		if answer == "q":
			print("До скорой встречи :)")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


oneAnswer = input("Введите первое слово: ")
twoAnswer = input("Введите второе слово: ")

print("Ты написал: ", oneAnswer, twoAnswer)
answer = (twoAnswer,) + (oneAnswer,)
print("Смотри что получилось", answer)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print("Проверка твоего возраста!")
answer = int(input("И сколько тебе лет? "))
if answer >= 18:
	print("Доступ разрешен")
else:
	print("Маловато будет!")