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
        pass

    def display_welcome(self):
        print('\nWelcome to the fight of the century! \n Only one will prevail victorious!\n')


    def battle_phase(self):
        while self.robot.health != 0 and self.dinosaur.health != 0:
            self.dinosaur.attack(self.robot)
            self.robot.attack(self.dinosaur)
            if self.robot.health == 0 or self.dinosaur.health == 0:
                break
        


    def display_winner(self):
        if self.robot.remaining_health == 0:
            print(f'{self.dinosaur.name} has defeated the mighty {self.robot.name}!')
        elif self.dinosaur.remaining_health == 0:
            print(f'{self.robot.name} has defeated the mighty {self.dinosaur.name}')
        pass
