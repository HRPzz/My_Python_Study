import random


number_input = Element("number_input")  # input 태그의 id
add_todo = Element("add_todo")  # button 태그의 id
result = Element("result")  # h1 태그의 id


def play_game(*args):
    user_guess = number_input.value
    if not user_guess:
        result.element.innerText = "Enter your number"
        return
    machine_guess = random.randint(1, 50)
    if int(user_guess) == machine_guess:
        result.element.innerText = "You win!"
    else:
        result.element.innerText = f"You lost! The machine chose {machine_guess}!"
    number_input.clear()


# 클릭 이벤트
add_todo.element.onclick = play_game
