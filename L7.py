# Задача 1: Создайте файл с именем "fruits.txt" и запишите в него названия фруктов:"яблоко", "банан", "апельсин" (каждое с новой строки).Затем откройте этот файл, прочитайте все строки и выведите на экран только те строки, которые начинаются с буквы "а".

# Решение:
file = open("fruits.txt", "r", encoding='utf-8')
for line in file.readlines():
 if line.startswith("а"):
    print(line)
file.close()


# Задача 2: Создай новый текстовый файл 'test.txt' и запиши в него строку "Hello, World!"
# Прочитай и выведи в консоль содержимое файла 'test.txt'
# Добавь в конец файла 'test.txt' строку "This is appended text"
# Прочитай и выведи только первые 5 символов из файла 'test.txt'

# Решение:
file = open("test.txt", "r+", encoding='utf-8')
file.write(" This is appended text")
file.seek(0)
print(file.read(5))
file.close()


# Задача 3: Используя конструкцию with, создай файл 'test.txt' и запиши в него "Using with statement"
#Используя with, прочитай и выведи содержимое файла 'test.txt'
#Используя with, добавь в файл 'with_example.txt' строку "Appended with with"

#Решение:
with open("test.txt", "w") as file:
    content = file.write("fdsfsdfsf")
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
with open("test.txt", "a") as file:
    file.write(" \nAppended with with")
with open("test.txt", "r") as file:
    content = file.read()
    print(content)




