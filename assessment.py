"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.


   Abstraction:
   Polymorphism: Things which serve the same function but have different genesis.

2. What is a class?
    Classes are a category of object-groupings. Their members (objects) carry attributes designated by their membership in a particular class. Attributes and methods can be attached to specific classes. All members of a class can be acted upon by methids attached to that class. All members of a class will have the same class-attributes. Instance attributes take precidence over class attributes.

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

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

# questions have answers

class Question(object):
    """Questions and answers, and belong to exams"""
2
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

#Exams have names, questions and answers
class Exam(object):
    """Exams have titles and contain questions"""

#Could treat a question as a very short exam, or could add a list of questions to a given exam