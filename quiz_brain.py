class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    def next_question(self):
        text = self.questions_list[self.question_number].text
        answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        user_input = input(f"Q{self.question_number}. {text}(True/False): ")
        self.check_answer(user_input, answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's not correct")
        print(f"your current score is {self.score}/{self.question_number}\n")