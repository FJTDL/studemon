import random as rd

# Define functions

def start():
  valid = False
  while not valid:
      global size
      global experience
      global status
      try:
        size = int(input("How large is your team?\n"))
        experience = int(input("How long have you held your position?\n"))
        status = input("Are you a dean, HOD or deputy principle? yes/no.\n").lower()
      except ValueError:
        start()
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
    self.academics = academics
    self.involvement = involvement
    self.status = status
    self.health = (self.year * 10 + self.involvement * 10) if (not self.status) else (self.year * 10 + self.involvement * 10 + 7)
    self.damage = (self.academics * 10 + self.involvement * 10) if (not self.status) else (self.academics * 10 + self.involvement * 10 + 2.5)
    self.evade=  (self.year + self.involvement) if (not status) else (self.year + self.involvement + 10)
    if self.involvement == 0:
      self.evade = 9

  
  def __repr__(self):
    represent = f"This student is year {self.year}, academics of {self.academics} with an involvement score of {self.involvement} and a leadership status of {self.status}.\nHealth: {self.health}\nDamage: {self.damage}\nEvade: {self.evade}"
    return represent
  
  # Actions
  def dodge(self):
    max = (self.evade * 100 ) ** -1
    success_score = rd.randint(0, max)
    if success_score < 2:
      return False
    return True

  
  def attack(self):
    # attack
    max = self.damage
    return round(rd.randint(0, max))


  def defend(self):
    # defense
    max = self.health + self.academics + self.involvement
    success_score = round(rd.randint(0, max))
    if success_score == max:
      return 0
    elif success_score > 0.9 * max:
      return 0.1
    elif success_score > 0.8 * max:
      return 0.2
    elif success_score > 0.7 * max:
      return 0.3
    elif success_score > 0.6 * max:
      return 0.4
    elif success_score > 0.5 * max:
      return 0.5
    elif success_score > 0.4 * max:
      return 0.6
    elif success_score > 0.3 * max:
      return 0.7
    elif success_score > 0.2 * max:
      return 0.8
    elif success_score > 0.1 * max:
      return 0.9
    else:
      return 1


# Declare Teacher class

class Teacher:

  # initialise method
  def __init__(self, experience, status, size):
    self.experience = experience
    self.status = status
    self.size = size
    self.team = []
    self.bonus = 0.25 * (self.experience * 5) if (not self.status) else 0.25 * (self.experience * 7)

  # Add students to team
  def add(self, student):
    self.team.append(student)
  
  def create_student(self):
    done = False
    while not done:
      try:
        while len(self.team) < self.size:
          year = int(input("Student year:\n"))
          smarts = int(input("Academic ability:\n"))
          involvement = int(input("Involvement:\n"))
          status = input("Leadership position? yes/no:\n").lower()
          if status == "yes":
            status = True
          else:
            status = False
          if len(self.team) == 0:
            self.student1 = Student(year, smarts, involvement, status)
            self.team.append(self.student1)
          elif len(self.team) == 1:
            self.student2 = Student(year, smarts, involvement, status)
            self.team.append(self.student2)
          else:
            self.student3 = Student(year, smarts, involvement, status)
            self.team.append(self.student3)
          done = True
      except ValueError:
        self.create_student()


print("WELCOME TO STUDEMON (pending legal approval)")
print("For most of the setup, you will enter numbers 0-10 inclusive unless otherwise stated")

# Code to start the game
start()

# initialise the opponents
player1 = Teacher(experience, status, size)
if player1.status == True:
  pos = "HEIGHTENED"
else:
  pos = "STANDARD"
print(f"PLAYER ONE CREATED, WITH {player1.experience} YEARS OF EXPERIENCE, A {pos} POSITION, AND A TEAM OF {player1.size}.\nPlayer Bonus: {player1.bonus}\n")
start()
player2 = Teacher(experience, status, size)
if player2.status == True:
  pos = "HEIGHTENED"
else:
  pos = "STANDARD"
print(f"PLAYER TWO CREATED, WITH {player2.experience} YEARS OF EXPERIENCE, A {pos} POSITION, AND A TEAM OF {player2.size}.\nPlayer Bonus: {player2.bonus}\n")

# add students

print("PLAYER ONE, ADD YOUR STUDENTS!")

for i in range(0, player1.size):
  player1.create_student()

for i in player1.team:
  print(i)

print("PLAYER TWO, ADD YOUR STUDENTS!")

for i in range(0, player2.size):
  player2.create_student()

for i in player2.team:
  print(i)

print("COMBAT LASTS 10 ROUNDS, FIGHT!")