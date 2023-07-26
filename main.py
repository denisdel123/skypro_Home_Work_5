from unit import words_list, change_word, write_to_history, print_history

word_txt = 'data/words.txt'
history_txt = 'data/history.txt'

if __name__ == '__main__':

    print("Введите ваше имя!")
    user_name = input()
    words = words_list(word_txt)
    score = 0

    for word in words:

        word_change = change_word(word)
        print(f"Угадайте слово: {word_change}")
        user_answer = input().strip(" ").lower()

        if user_answer == word:
            print("Верно! Вы получаете 10 очков.")
            score += 10
        else:
            print(f"Неверно! Верный ответ – {word}")

    write_to_history(history_txt, user_name, score)
    print(print_history(history_txt))