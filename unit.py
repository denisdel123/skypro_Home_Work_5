import random


def words_list(words_file):
    new_list = []

    with open(words_file, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            new_list.append(line.strip('\n'))
        return new_list


def change_word(word):
    word = list(word)
    random.shuffle(word)
    return "".join(word)


def write_to_history(file_name, user_name, score):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"{user_name} {score}\n")


def print_history(history_txt):
    max_score = 0
    count = 0
    with open(history_txt, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            count += 1
            score = int(line.split(' ')[1])
            if score > max_score:
                max_score = score
    result = f"Всего игр сыграно: {count}\nМаксимальный рекорд: {max_score}"
    return result
