import random

class Question:
   def __init__(self, prompt, answer):
       self.prompt = prompt
       self.answer = answer

class Quiz:
   def __init__(self, questions):
       self.questions = questions
       self.score = 0

   def grade(self, answer):
       if answer == self.questions[-1].answer:
           self.score += 1

   def take(self):
       for question in self.questions:
           print(question.prompt)
           guess = input("Your Answer: ")
           self.grade(guess)
       print("Score: ", self.score)

class Student:
   def __init__(self, name):
       self.name = name
       self.quizzes = []

   def take_quiz(self, quiz):
       quiz.take()
       self.quizzes.append(quiz)

# Create some questions
q1 = Question("What is the capital of France?", "Paris")
q2 = Question("Who wrote Pride and Prejudice?", "Jane Austen")
q3 = Question("What is the square root of 144?", "12")

quiz = Quiz([q1, q2, q3])

student = Student("Alice")

student.take_quiz(quiz)
