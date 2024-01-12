from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for each in question_data:
    text = each['text']
    ans = each['answer']
    question = Question(text, ans)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz and your final score is {quiz.score}/{quiz.question_number}. ")
