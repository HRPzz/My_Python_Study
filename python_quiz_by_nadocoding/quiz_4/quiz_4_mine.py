class Word():

    def __init__(self, word, choice_1, choice_2, answer):
        self.word = word
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.answer = answer

    def show_question(self):
        question = (
            f'"{self.word}"의 뜻은?\n'
            f'1. {self.choice_1}\n'
            f'2. {self.choice_2}'
        )
        print(question)

    def check_answer(self, choice):
        is_answer = True if self.answer == choice else False
        
        if is_answer:
            print("정답입니다")
        else:
            print("틀렸습니다")


word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer(int(input("=> ")))