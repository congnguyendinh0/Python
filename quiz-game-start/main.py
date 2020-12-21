from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    answer = question["answer"]
    text = question["text"]
    new_question = Question(text,answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You have completed the quiz')
print(f'your final score was: {quiz.score}/ {len(question_bank)}')
