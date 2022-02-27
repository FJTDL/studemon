from random import randint as rd

# Define functions

def start():
  valid = False
  while not valid:
      global size
      global experience
      global status
      size = int(input("How large is your team?"))
      experience = int(input("How long have you held your position?"))
      status = input("Are you a dean, HOD or deputy principle? yes/no. ").lower()
      if status == "yes":
        status = True
      else:
        status = False
      if type(size) == int and type(experience) == int and type(status) == bool:
        valid = True
      else:
        start()


# Declare student class
class Student:

  # Initial method
  def __init__(self, year, academics, involvement, status = False):
    self.year = year
    self.smarts = academics
    self.pillar = involvement
    self.status = status

  
  def __repr__(self):
    represent = f"This student is year {self.year}, academics of {self.smarts} with an involvement score of {self.pillar} and a leadership status of {self.status}"
    return represent
  
  # Actions
  def evade():
    # evade system
    pass

  
  def attack():
    # attack
    pass


  def defend():
    # defense
    pass


# Declare Teacher class

class Teacher:

  # initialise method
  def __init__(self, experience, status, size):
    self.experience = experience
    self.status = status
    self.size = size
    self.team = []

  # Add students to team
  def add(self, student):
    self.team.append(student)
  
  def create_student(self):
    while len(self.team) < self.size:
      year = int(input("Student year:"))
      smarts = int(input("Academic ability:"))
      pillar = int(input("Involvement: "))
      status = input("Leadership position? yes/no.").lower()
      if status == "yes":
        status = True
      else:
        status = False
      if len(self.team) == 0:
        self.student1 = Student(year, smarts, pillar, status)
        self.team.append(self.student1)
      elif len(self.team) == 1:
        self.student2 = Student(year, smarts, pillar, status)
        self.team.append(self.student2)
      else:
        self.student3 = Student(year, smarts, pillar, status)
        self.team.append(self.student3)


print("WELCOME TO STUDEMON (pending legal approval)")
print("For most of the setup, you will enter numbers 0-10 inclusive unless otherwise stated 😁")

# Code to start the game
start()

# initialise the opponents
player1 = Teacher(experience, status, size)
if player1.status == True:
  pos = "HEIGHTENED"
else:
  pos = "STANDARD"
print(f"PLAYER ONE CREATED, WITH {player1.experience} YEARS OF EXPERIENCE, A {pos} POSITION, AND A TEAM OF {player1.size}.\n")
start()
player2 = Teacher(experience, status, size)
print(f"PLAYER TWO CREATED, WITH {player2.experience} YEARS OF EXPERIENCE, A {pos} POSITION, AND A TEAM OF {player2.size}.\n")

# add students

print("PLAYER ONE, ADD YOUR STUDENTS")

for i in range(0, player1.size):
  player1.create_student()

for i in player1.team:
  print(i)