"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.


   Abstraction: Hiding details we don't need
   Encapsulation: Keeping everything together. Organize our components
   Polymorphism: Things which serve the same function but have different genesis.

2. What is a class?
    Classes are a category of object-groupings. Their members (objects) carry attributes designated by their membership in a particular class. Attributes and methods can be attached to specific classes. All members of a class can be acted upon by methids attached to that class. All members of a class will have the same class-attributes. Instance attributes take precidence over class attributes.

3. What is an instance attribute?
    Attribute attached to a particular instance

4. What is a method?
  Actions attached to specific classes

5. What is an instance in object orientation?
    One member of a class or subclass

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Say we have a parent class Animal(object):

   Class attributes are attached to every member of the class to which they are assigned. Birds have wings, so each instance of a class Bird(Animal) will have the attribute winged = True. 

   Instance attributes are attached only to the instance to which they are assigned. Bats have wings. But they are the only instance of the class Mammal(Animal) (that I can think of at the moment) that does. The instance bat(Mammal) should have the instance attribute winged = True All other mammals (that I can think of) will have the attribute winged = False dog.winged() would be False. cat.winged(), kangaroo.winged(), echidna.winged() and so on would all be False.


"""

#Students have first name, last name and address
class Student(object):
    """Students, with names (first and last) and addresses"""

    def __init__(self, name_first, name_last, address_street):
        self.name_first = name_first
        self.name_last = name_last
        self.address_street = address_street
        self.score = 0

class Question(object):
    """Questions and correct answers"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        user_answer = raw_input(self.question + ">\n")
        if user_answer == self.correct_answer:
            return True

class Exam(object):
    """Exams have titles and contain a list of questions"""

    def __init__(self, title, questions):
      self.title = title
      self.questions = questions

    def administer(self, student, questions):
        for question in self.questions:
            if question.ask_and_evaluate():
                self.score = self.score + 1
            else:
                self.score = self.score
        return self.score

def example():
    """Administer a test to myself and alter my score"""
    question1 = Question("What is pi?", "delicious")
    question2 = Question("What's brown and sticky?","stick")
    question3 = Question("The more you take, the more you leave behind. What is it?", "footsteps")

    example_exam = Exam("example_exam", [question1, question2, question3])

    erin = Student("Erin", "Woodworth", "123 main st")

    example_exam.administer(erin, [question1, question2, question3])


example()

class Quiz(Exam):
"""Shorter pass/fail exams"""

    def administer(self, students, questions):
        super(Quiz, self).administer()
        if self.score / len(questions) >= 0.5:
            return True
        else:
            return False