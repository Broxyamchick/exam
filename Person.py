import random
from Action import Action

class PersonDied(Exception):
    def __init__(self, message='Person has 0 hp'):
        Exception.__init__(self, message)
class PersonInDepression(Exception):
    def __init__(self, message='Person has 0 mood'):
        Exception.__init__(self, message)
class PersonWentBankrupt(Exception):
    def __init__(self, message='Person has 0 money'):
        Exception.__init__(self, message)

class Person:
    name = ""
    hp = 100
    mood = 100
    money = 0

    def __init__(self, name, hp, mood, money):
        self.name = name
        self.hp = hp
        self.mood = mood
        self.money = money


    def __str__(self):
        return f'{self.name} (hp:{self.hp},' \
               f' mood:{self.mood},' \
               f' money: {self.money})'

    def change_state(self, hp, mood, money):
        self.hp = self.hp + hp
        self.mood = self.mood + mood
        self.money = self.money + money

    def do(self, ahp, amood, amoney, ):
        self.hp += ahp
        self.mood += amood
        self.money += amoney

  #      if self.hp <= 0:
 #           raise PersonDied
 #       if self.mood <= 0:
 #           raise PersonInDepression
 #       if self.money <= 0:
#            raise PersonWentBankrupt






