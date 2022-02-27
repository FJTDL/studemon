from random import randint as rd

# Define functions

def create_student():
  

def start():
  valid = False
  while not valid:
      global size
      global experience
      global special
      size = int(input("How large is your team?"))
      experience = int(input("How long have you held your position?"))
      special = input("Are you a dean, HOD or deputy principle? yes/no. ").lower()
      if special == "yes":
        special = True
      elif special == "no":
        special = False
      if type(size) == int and type(experience) == int and type(special) == bool:
        valid = True
      else:
        start()


# Declare student class
class Student:

  # Initial method
  def __init__(self, year, academics, involvement, special = False):
    self.year = year
    self.smarts = academics
    self.pillar = involvement
    self.status = special
  
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
  def __init__(self, experience, special, size):
    self.experience = experience
    self.special = special
    self.size = size
    self.team = []

  # Add students to team
  def add(self, student):
    self.team.append(student)




# Code to start the game
start()

# initialise the opponents
player1 = Teacher(experience, special, size)
if player1.special == True:
  pos = "HEIGHTENED"
else:
  pos = "STANDARD"
print(f"PLAYER ONE CREATED, WITH {player1.experience} YEARS OF EXPERIENCE, A {pos} POSITION, AND A TEAM OF {player1.size}.\n")
start()
player2 = Teacher(experience, special, size)
print(f"PLAYER TWO CREATED, WITH {player2.experience} YEARS OF EXPERIENCE, A {pos} POSITION, AND A TEAM OF {player2.size}.\n")

# add students

print("PLAYER ONE, ADD YOUR STUDENTS")
