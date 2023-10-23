class QuizBrain:

    def __init__(self , question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return len(self.question_list) > self.question_no

    def next_question(self):
        statement = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f'Q. no {self.question_no}: {statement.text}(True / False)?: ')
        self.check_answer(user_ans , statement.answer)

    def check_answer(self, user_ans , correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print('You got right!')
            self.score += 1
        else:
            print("That's wrong")
        print(f'The correct answer was {correct_answer}.')
        print(f'Your current score is {self.score}/{self.question_no}')
        print('\n')