

class Dinosaur():
    def __init__(self, name, attack_power):
        self.name = name                    #string
        self.attack_power = attack_power    #int
        self.health = 100
        

    def attack(self, robot):
        remaining_health = robot.health - self.attack_power                 #what code goes here
        print(f'{self.name} attacked {robot.name} for {self.attack_power} damage \n {robot.name} now has {remaining_health} remaining!\n')