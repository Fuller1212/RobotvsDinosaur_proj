from dinosaur import Dinosaur
from robot import Robot

class Battlefield():
    def __init__(self):
        self.robot = Robot('Screwie')
        self.dinosaur = Dinosaur('Rex', 25)
        

    def run_game(self):
        self.display_welcome()
        self.battle_phase() 
        self.display_winner   
        

    def display_welcome(self):
        print('\nWelcome to the fight of the century! \n Only one will prevail victorious!\n')


    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            if self.robot.health > 0:
                self.dinosaur.attack(self.robot)
                robot_remaining_health = self.robot.health - self.dinosaur.attack_power  
                if robot_remaining_health <=0:
                    break

            
            if self.dinosaur.health > 0:
                self.robot.attack(self.dinosaur)
                dinosaur_remaining_health = self.dinosaur.health - self.robot.active_weapon.attack_power
                if dinosaur_remaining_health <= 0:
                    break
        


    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} has defeated the mighty {self.robot.name}!')
        elif self.dinosaur.health <= 0:
            print(f'{self.robot.name} has defeated the mighty {self.dinosaur.name}')
        
