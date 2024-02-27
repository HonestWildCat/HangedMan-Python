import json
from random import choice, randint


def chose_word(difficulty):  # Рандомный выбор слова, считывание его темы и подсказки.
    if difficulty == 0:  # Выбор слова по сложности
        w = choice(words[randint(0, 4)])
    else:
        w = choice(words[difficulty - 1])
    return w, data[w], data[w]["definition"]


def read_json(lang):  # Открытие json и считывание с файла.
    path = f"words_{lang}.json"
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)

    # Создание списка со всеми словами, их темами и подсказками.
    words = [[], [], [], [], []]
    for i in data.keys():
        length = len(i)
        if length < 4:
            words[0].append(i)
        elif length < 7:
            words[1].append(i)
        elif length < 10:
            words[2].append(i)
        elif length < 14:
            words[3].append(i)
        else:
            words[4].append(i)
    return words, data


def validation():  # Обеспечевает правильность ввода
    while True:
        w = input(">>> ").lower()
        if len(w) != 1:
            print(message[lang]["TooManyLetters"])
        elif w == "?" or w == "!":
            return w
        elif not w.isalpha():
            print(message[lang]["Invalid input"])
        else:
            for j in alphabet[lang]:
                if w == j.lower():
                    return w


run = True
# Язык
lang = ""
print("Select language(ru|ua|en):")
while lang not in ["ru", "ua", "en"]:
    lang = input(">>> ")
words, data = read_json(lang)
msg = "None"

# Сообщения
message = {"ru": {"None": "",
                  "NotEnoughScore": "Недостаточно очков.",
                  "TooManyLetters": "Введите 1 букву.",
                  "Invalid input": "Введите букву, а не число или символ.",
                  "Mistakes": "Ошибки",
                  "Points": "Очки",
                  "Victory": "Вы победили!",
                  "Defeat": "Вы проиграли...",
                  "Word": "Слово:",
                  "Replay": "Сыграть ещё?",
                  "SelectDifficulty": "Выберите сложность:",
                  "InvalidNumber": "Неверный ввод.",
                  "Difficulty": "  0: случайная длинна слова."
                                "\n  1: 1-3 буквы."
                                "\n  2: 4-6 буквы."
                                "\n  3: 7-9 буквы."
                                "\n  4: 10-13 буквы."
                                "\n  5: больше 13 букв."},
           "ua": {"None": "",
                  "NotEnoughScore": "No",
                  "TooManyLetters": "Введіть 1 літеру.",
                  "Invalid input": "Введіть літеру, а не число або символ.",
                  "Mistakes": "Помилки",
                  "Points": "Очки",
                  "Victory": "Вы виграли!",
                  "Defeat": "Вы програли...",
                  "Word": "Слово:",
                  "Replay": "Грати ще?",
                  "SelectDifficulty": "Оберіть складність:",
                  "InvalidNumber": "Неправильне введення.",
                  "Difficulty": "  0: випадкова довжина слова."
                                "\n  1: 1-3 літери."
                                "\n  2: 4-6 літер."
                                "\n  3: 7-9 літер."
                                "\n  4: 10-13 літер."
                                "\n  5: більше 13 літер."
                  },
           "en": {"None": "",
                  "NotEnoughScore": "Not enough points.",
                  "TooManyLetters": "Input 1 letter.",
                  "Invalid input": "Enter a letter, not a number or symbol.",
                  "Mistakes": "Mistakes",
                  "Points": "Points",
                  "Victory": "You won!",
                  "Defeat": "You lost...",
                  "Word": "Word:",
                  "Replay": "Play again?",
                  "SelectDifficulty": "Select difficulty:",
                  "InvalidNumber": "Invalid input.",
                  "Difficulty": "  0: random word length."
                                "\n  1: 1-3 letters."
                                "\n  2: 4-6 letters."
                                "\n  3: 7-9 letters."
                                "\n  4: 10-13 letters."
                                "\n  5: more than 13 letters."
                  }}

# Текст в начале игры
intoduction = {"ru": """
Игра Виселица
=================================================
Вам необходимо отгадать загаданное слово,
вводя по букве с клавиатуры.
Не допускайте более 6 ошибок.
За каждую отгаданную букву начисляется 1 очко.
=================================================
! - показать подсказку
? - подсказать букву (цена подсказки 2 очка)
=================================================
""",
               "ua": """
Гра Шибениця
=================================================
Вам необхідно відгадати загадане слово,
вводячи по літері з клавіатури.
Не допускайте більше 6 помилок.
За кожну відгадану літеру нараховується 1 очко.
=================================================
! - показати підказку
? - підказати букву (ціна підказки 2 очки)
=================================================
""",
               "en": """
Hangman game
================================================
You need to guess the hidden word,
entering letter by letter from the keyboard.
Do not make more than 6 mistakes.
For each guessed letter, 1 point is awarded.
================================================
! - show hint
? - suggest a letter (suggestion price is 2 points)
================================================
                 """}
print(intoduction[lang])
# Основной цикл игры
while run:
    difficulty = -1  # Сложность
    print(message[lang]["SelectDifficulty"])
    print(message[lang]["Difficulty"])
    while not 0 < difficulty < 6:
        try:
            difficulty = int(input(">>> "))
        except:
            print(message[lang]["InvalidNumber"])

    word, topic, prompt = chose_word(difficulty)
    mistakes = 0  # Кол-во ошибок
    score = 0  # Кол-во очков
    secret = "_" * len(word)  # Слово из прочерков
    dash = word.find("-")
    if dash != -1:
        secret = secret[:dash] + "-" + secret[dash + 1:]  # Добавление дефиса

    alphabet = {"en": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                       "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                       "W", "X", "Y", "Z"],
                "ru": ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К",
                       "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х",
                       "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"],
                "ua": ["А", "Б", "В", "Г", "Ґ", "Д", "Е", "Є", "Ж", "З",
                       "И", "І", "Ї", "Й", "К", "Л", "М", "Н", "О", "П", "Р",
                       "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ь", "Ю", "Я"]}
    letters = []  # Введенные буквы

    print("#" * 15)
    print(word)
    print(prompt)
    print("#" * 15)
    print()

    game = True

    # Раунд игры
    while game:
        # Вывод информации
        for i in secret:
            print(" " + i, end="")
        print("\n")
        n = 0
        for i in alphabet[lang]:
            if n == 10:
                print("")
                n = 0
            print(i, end=" ")
            n += 1
        print("")
        print(f"{message[lang]['Mistakes']}: {mistakes}/7")
        print(f"{message[lang]['Points']}: {score}")
        print(message[lang][msg])
        msg = "None"

        # Пользовательский ввод и его обработка
        letters.append(validation())
        guessed = False
        # Помощь игроку
        if letters[-1] == "?":  # Помощь (открытие 1 буквы)
            if score > 1:
                print()
                score -= 3
                letters[-1] = word[secret.find("_")]
            else:
                msg = "NotEnoughScore"
                guessed = True
        if letters[-1] == "!":  # Подсказка
            print(prompt)
            letters.append(validation())

        for o in alphabet[lang]:  # Убирает букву из алфавита
            if o == letters[-1].upper():
                alphabet[lang][alphabet[lang].index(o)] = " "
        for i in range(len(word)):
            if word[i] == letters[-1]:
                guessed = True
                secret = secret[:i] + letters[-1] + secret[i + 1:]
        if not guessed:
            mistakes += 1
        else:
            score += 1

        # Победа.
        if secret.find("_") == -1:
            print(message[lang]["Victory"])
            print(message[lang]['Word'] + word)
            game = False

        # Поражение
        if mistakes == 7:
            print(message[lang]["Defeat"])
            print(message[lang]['Word'] + word)
            game = False

    # Начать цикл снова
    print(message[lang]["Replay"] + " +/-")
    replay = input(">>> ")
    if replay != "+":
        run = False
