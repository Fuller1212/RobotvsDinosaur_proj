

from weapon import Weapon




class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Dino blaster', 35)
        

    def attack(self, dinosaur):  
        dinosaur.health = dinosaur.health  - self.active_weapon.attack_power
        print(f'Robo {self.name} attacked {dinosaur.name} with a {self.active_weapon.name} for {self.active_weapon.attack_power} damage \n {dinosaur.name} now has {dinosaur.health} health remaining! \n')
        
