# Задача 1: Создай словарь car, где ключи — это "brand", "model" и "year", а значения — "Toyota", "Corolla" и 2018 соответственно.
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year":  2018
}
print(car)


# Задача 2: Дан словарь person = {"name": "Alice", "age": 25}. Выведи значение, связанное с ключом "age".
person = {"name": "Alice", "age": 25}
age = person["age"]


# Задача 3: Дан словарь fruit = {"apple": 3, "banana": 5}.
# Добавь в него новый ключ "orange" со значением 2.
# Затем измени значение ключа "banana" на 7.
fruit = {
    "apple": 3,
    "banana": 5
}
fruit["orange"] = 2
fruit["banana"] = 7

print(fruit)


# Задача 4: Дан словарь colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}. Удали ключ "green" и его значение.
colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF"
}
del colors["green"]


# Задача 5: Дан словарь book = {"title": "1984", "author": "Orwell", "year": 1949}.
# Выведи:
# Список всех ключей словаря.
# Список всех значений словаря.
book = {
    "title": "1984",
    "author": "Orwell",
    "year": 1949
}
keys = list(book.keys())
values = list(book.values())


# Задача 6: Дан словарь grades = {"Math": 90, "Science": 85, "History": 78}.
# Проверь, есть ли в словаре ключ "Science"
# Проверь, есть ли среди значений число 78
grades = {
    "Math": 90,
    "Science": 85,
    "History": 78
}
if "Science" in grades:
    print("Science" in grades)
    print(78 in grades.values()


