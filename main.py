import random
from Person import Person
from Action import Action

class PersonsAreDied(Exception):
    def __init__(self, message='Persons are died, depressed or went bankrupt'):
        Exception.__init__(self, message)
human = Person(name='Тарас', money = 0, mood = 100, hp = 100)
human2 = Person(name='Василий', money = 0, mood = 100, hp = 100)
human3 = Person(name='Данил', money = 0, mood = 100, hp = 100)

print(human)
print(human2)
print(human3)



people1 = 0
people2 = 0
people3 = 0

allpeoples = 0

if people1 == 1 and people2 == 1 and people3 == 1:
    allpeoples = 1

while allpeoples == 0:
    whattodo = random.randint(1, 2)

    if whattodo == 1:
        human.do(ahp=-5, amoney=100, amood=-20)
        print(human)
        if human.money <= 0 or human.mood <= 0 or human.hp <= 0:
            people1 = 1
            if people1 == 1 and people2 == 1 and people3 == 1:
                allpeoples = 1
    else:
        human.do(ahp=3, amoney=0, amood=15)
        print(human)
        if human.money <= 0 or human.mood <= 0 or human.hp <= 0:
            people1 = 1
            if people1 == 1 and people2 == 1 and people3 == 1:
                allpeoples = 1

    whattodo = random.randint(1, 2)

    if whattodo == 1:
        human2.do(ahp=-5, amoney=100, amood=-20)
        print(human2)
        if human2.money <= 0 or human2.mood <= 0 or human2.hp <= 0:
            people2 = 1
            if people1 == 1 and people2 == 1 and people3 == 1:
                allpeoples = 1
    else:
        human2.do(ahp=3, amoney=0, amood=15)
        print(human2)
        if human2.money <= 0 or human2.mood <= 0 or human2.hp <= 0:
            people2 = 1
            if people1 == 1 and people2 == 1 and people3 == 1:
                allpeoples = 1

    whattodo = random.randint(1, 2)

    if whattodo == 1:
        human3.do(ahp=-5, amoney=100, amood=-20)
        print(human3)
        if human3.money <= 0 or human3.mood <= 0 or human3.hp <= 0:
            people3 = 1
            if people1 == 1 and people2 == 1 and people3 == 1:
                allpeoples = 1
    else:
        human3.do(ahp=3, amoney=0, amood=15)
        print(human3)
        if human3.money <= 0 or human3.mood <= 0 or human3.hp <= 0:
            people3 = 1
            if people1 == 1 and people2 == 1 and people3 == 1:
                allpeoples = 1

if allpeoples == 1:
    raise PersonsAreDied



