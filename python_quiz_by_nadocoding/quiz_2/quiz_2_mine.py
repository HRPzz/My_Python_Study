import random
import re


def yield_index_ch(answer, user_ch):
    for i, ch in enumerate(answer):
        if ch == user_ch:
            yield i, ch


def make_user_answer(answer):
    user_answer = re.sub('\w', '_', answer)
    return user_answer


def check_ch(answer, user_answer, user_ch):
    if user_ch in answer:
        for i, ch in yield_index_ch(answer, user_ch):
            user_answer = user_answer[:i] + user_ch + user_answer[i+1:]
        print('--- Correct ---')
        print(user_answer)
    else:
        print('--- Wrong ---')
    return user_answer


def is_answer(answer, user_answer):
    if user_answer == answer:
        print('--- Success ---')
        return True
    return False


def is_over(chance):
    if chance <= 0:
        print('--- Game Over ---')
        return True
    return False


def play_hangman(answer):
    print('--- Start ---')
    chance = 10
    user_answer = make_user_answer(answer)

    while True:
        user_ch = input(f"남은 도전 횟수 {chance}. 알파벳 1개 입력: ")
        if len(user_ch) != 1 or not user_ch.isalpha():
            print("다시 입력하세요. 알파벳 1개만 입력 가능합니다.")
            continue
        if user_ch in user_answer:
            print("다시 입력하세요. 앞서 정답을 맞춘 알파벳입니다.")
            continue
        
        user_answer = check_ch(answer, user_answer, user_ch)
        if is_answer(answer, user_answer):
            break
        else:
            chance -= 1

        if is_over(chance):
            break


answers = ["apple", "banana", "orange"]
answer = random.choice(answers)

play_hangman(answer)
