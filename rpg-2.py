from random import randint

class Character:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        print('The %s did %s damage to %s' % (self.name, self.power, enemy.name))

    def print_status(self):
        print('%s has %d health and %d power' % (self.name, self.health, self.power))

class Hero(Character):
    def double_attack(self, enemy):
        dice = randint(0,10)
        double = self.power
        if dice == 0 or dice == 1:
            double = (self.power * 2)
            enemy.health -= double
        else:
            enemy.health -= self.power
        print('The %s did %s damage to %s' % (self.name, double, enemy.name))

class Goblin(Character):
    pass

class Zombie(Character):
    pass
    

hero = Hero('Hero', 10, 5)
goblin = Goblin('Goblin', 500, 2)
zombie = Zombie('Zombie', 10, 1)

###### for goblin vs hero
def main():
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.double_attack(goblin)
            if goblin.alive() == False:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive() == True:
            goblin.attack(hero)
            if hero.alive() == False:
                print("You are dead.")
main()


##### for goblin vs immortal zombie
# def main():
#     while hero.alive():
#         hero.print_status()
#         zombie.print_status()
#         print()
#         print("What do you want to do?")
#         print("1. fight zombie")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ",)
#         user_input = input()
#         if user_input == "1":
#             hero.attack(zombie)
#         elif user_input == "2":
#             pass
#         elif user_input == "3":
#             print("You used smokescreen and escaped")
#             break
#         else:
#             print("Invalid input %r" % user_input)

#         zombie.attack(hero)
#         if hero.alive() == False:
#             print("You are dead.")
# main()