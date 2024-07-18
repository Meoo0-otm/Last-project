print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы:")
questions = [
    "1. Какой объем памяти имела автоматическая цифровая вычислительная машина М-1?",
    "2. Какого числа отмечается День программиста (256 день в году) в високосный год?",
    "3. Кто заложил идеи двоичного кодирования?",
    "4. Какова была тактовая частота у первой модели персонального компьютера фирмы IBM?",
    "5. Как называлась первая ЭВМ в СССР?",
    "6. Кто был первым изобретателем перфокарт?",
    "7. В каком году появился язык программирования Python?"]
answers = ["1. 256 слов",
           "2. 12 сентября",
           "3. Готфрид Вильгельм Лейбниц",
           "4. 4,77 МГц",
           "5. МЭСМ",
           "6. Жаккард",
           "7. В 1991 году",]
score = 0

print(questions[0])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[0].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[1])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[1].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[2])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[2].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[3])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[3].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[4])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[4].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[5])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[5].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[6])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[6].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(f'Вы ответили правильно на  {score} вопросы')