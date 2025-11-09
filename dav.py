import random

class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_info(self):
        return f"{self.name} is {self.age} and studies: {','.join(self.subjects)}"
    
students = []    
alice =  Student('Alice', 15, ['Math', "Science"])
muhamed = Student('Muhamed', 17, ['Math', 'History'])
michael = Student('Michael', 14, ['Geography', 'Biology'])
chris  = Student('Chris', 16, ['Music', 'Art'])
students.append(alice)
students.append(muhamed)
students.append(michael)
students.append(chris)

#a)
print(len(students))

if michael in students:
    students.remove(michael)

#b)
grades = {}
for i in students:
    grades[i]= random.randint(1, 10)

grades['chris'] = 10

for i in grades:
    print(f"{i} got  {grades[i]}")

#g)

schedule = ("Math", 'Lunch', "Science", "Gym")

print(schedule[1])

#schedule[0] = "Geography"  -----> error-s miwers

#d)
classes = {"Robotics", "Debate", "Art"}
classes.add("Math")
classes.add("Art")
print(classes) # ----> orjer Art ar daaamata
if 'Art' in classes:
    print("Art in classes")
else:
    print("Art not in classes")