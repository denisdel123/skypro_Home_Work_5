import random

"""записываем имя в переменную"""


def to_meet():
    print("Ведите ваше имя: ")
    user_name = input()
    return user_name


user_name = to_meet()

"""функция выбирающее слово и перемешивающая его в этой функции процесс игры"""


def word_get():
    ex_count = 0
    for i in range(10):
        words_list = []
        with open('data/words.txt', 'r') as file:
            correct_word = random.choice(file.read().strip().split())

            for a in correct_word:
                words_list.append(a)
                random.shuffle(words_list)

            guess_word = "".join(words_list)

            print(f"Угадайте слово: {guess_word}")
            answer = input().strip().lower()
            if answer == correct_word:
                ex_count += 10
                print("Верно! Вы получаете 10 очков.")
            else:
                print(f"Неверно! Верный ответ – {correct_word}.")
    return ex_count


ex_count = word_get()

"""записываем результаты игры и имя в файл"""


def add_file_txt(name="user", ex_count=0):
    with open("data/history.txt", "a") as file:
        file.write(f"\n{name}: {ex_count}")


"""выводим результаты игры пользователю"""


def statistics_print():
    games = 0
    max_record = 0
    with open('data/history.txt', 'r', encoding='utf-8') as file:
        items = file.readlines()

        for line in items:
            games += 1
            score = int(line.split(':')[1])
            if max_record < score:
                max_record = score
    print(f"""Всего игр сыграно: {games}
Максимальный рекорд: {max_record}""")


add_file_txt(user_name, ex_count)

statistics_print()
