

from weapon import Weapon
laser_eyes = Weapon('Laser eyes',45)
dino_blaster = Weapon('Dino blaster', 35)
flame_thrower = Weapon('Flame thrower', 40)



class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon

    def choose_weapon(self):
        print(f'{self.name}, you have 3 different weapon choices')
        print('Enter 1 for the deadly Laser eyes, Enter 2 for the destructive Dino blaster, or enter 3 for the scorching Flame thrower')
        user_input = int(input('Which weapon would you like to take into battle?'))
        if user_input == 1:
            self.active_weapon = laser_eyes
            return self.active_weapon
        elif user_input == 2:
            self.active_weapon = dino_blaster
            return self.active_weapon
        elif user_input == 3:
            self.active_weapon = flame_thrower
            return self.active_weapon
        else: 
            print('Not a valid option')
            
        

    def attack(self, dinosaur):  
        print(f'Robo {self.name} attacked {dinosaur.name} with a {self.active_weapon.name} for {self.active_weapon.attack_power} damage')
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{dinosaur.name} now has {dinosaur.health} health remaining!\n')
        
        
