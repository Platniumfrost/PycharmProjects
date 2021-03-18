import random
class Critter(object):
    """this is the class that defines what a critter is"""
    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = random.randint(2,7)
        self.name = ""
        self.happy = 50
        self.isAlive = True

    def getHunger(self):
        return self.hunger

    def getHealth(self):
        return self.health

    def getHeight(self):
        return self.height

    def getweight(self):
        return self.weight

    def gethappy(self):
        return self.happy

    def getname(self):
        return self.name

    def setname(self,name):
        if len(name) > 4:
            if (name.contains("uck")) == False:
                self.name = name

    def getHeight(self,height):
        if height < 5 and height > 1:
            self.height = height

    def getHealth(self,health):
        if self.health > 100:
            self.health = health

    def intro(self):
        print("hello my name is "+self.getname())

    def hud(self):
        health = self.health()
        if health > 80:
            print("Health: Great")
        elif health > 60:
            print("Health: Good")
        elif health > 50:
            print("Health: Fair")
        elif health == 0:
            self.die()
        else:
            print("Health: Poor")

            happy = self.gethappy()
            if happy > 50:
                print("Happiness: Happy")
            elif happy > 35:
                print("Happiness: Grumpy")
            else:
                print("Happiness: Pissed off")

        def die(self):
            print("your pet has died. You are a horable person for letting this digital creature die.")
            self.health = 0
            self.isAlive = False

        hunger = self.getHunger()
        if hunger > 40:
            print("Hunger: Starving")
        elif hunger > 20:
            print("Hunger: Really Hungry")
        elif hunger < 10:
            print("Hunger: Full")
        else:
            print("Hunger: Hungry")
        if hunger == 100:
            self.die()
        if hunger == -100:
            self.die()



    def feed(self,food):
        if food == "pizza":
            self.hunger -= 7
        elif food == "cheese burger":
            self.hunger -= 13
        elif food == "steaj":
            self.hunger -= 23
        elif food == "corn":
            self.hunger -= 3
        elif food == "cheesecake":
            self.hunger -= 100
        else:
            self.hunger -= 5

    def pass_time(self,hours):
        for i in range(hours):
            self.hunger += 2
            if self.hunger < 0:
                self.weight += 1
                self.happy += 10
                self.health -= 5
            if self.hunger > 50:
                self.weight -= 1
                self.happy -= 10
                self.health -= 5
            self.happy -= 5

    def play(self,time):
        self.pass_time(self,time)
        self.happy += 10 *time
        if self.happy > 100:
            self.happy = 100
        self.happy += 10 *time
        if self.health > 100:
            self.health = 100


def main():
    pet = Critter()
    name = input("what would you like to name your pet")
    pet.setname(name)
    height = int(input("how tall is your pet between 2 and 5"))
    pet.getHeight(height)
    pet.intro()
    pet.hud()
    while pet.isAlive:
        pet.pass_time(1)
        print("what would you like to know")
        print("feed")
        print("play")
        print("nothing")
        response = input()
        if response == "feed":
            food = input("what do you want to feed your pet")
            pet.feed(food)
        if response == "play":
            time = int(input("how long will you play with your pet"))
            pet.play(time)
    pet.hud()


main()
