

class Dinosaur():
    def __init__(self, name, attack_power):
        self.name = name                    
        self.attack_power = attack_power    
        self.health = 100
        

    def attack(self, robot):
        print(f'Dino {self.name} attacked {robot.name} for {self.attack_power} damage')
        robot.health -= self.attack_power
        print(f'{robot.name} now has {robot.health} health remaining!\n')
        