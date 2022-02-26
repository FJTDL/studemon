class Student:

  def __init__(self, year, academics, involvement, special = False):
    self.year = year
    self.smarts = academics
    self.pillar = involvement
    self.status = special
  

  def evade():
    # evade system
    pass

  
  def attack():
    # attack
    pass


  def defend():
    # defense
    pass


class Teacher:

  def __init__(self, experience, special, size):
    self.exp = experience
    self.special = special
    self.team = size


def start():
  valid = False
  while not valid:
      size = int(input("How large is your team?"))
      xp = int(input("How long have you held your position?"))
      status = input("Are you a dean, HOD or deputy principle?").lower()
      if status == "yes":
        status = True
      if type(size) == int and type(xp) == int and type(status) == str:
        valid = True
      else:
        start()
    
start()
#if 4 > size > 0:
 #     player1 = Teacher(xp, status, size)