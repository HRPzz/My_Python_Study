from random import *


words = ["apple", "banana", "orange"]
word = choice(words)
letters = ""  # 사용자로부터 지금까지 입력받은 모든 알파벳

while True:
    succed = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succed = False
    print()

    if succed:
        print("Success")
        break

    letter = input("Input letter > ")  # 사용자 입력 받기
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("Correct")
    else:
        print("Wrong")