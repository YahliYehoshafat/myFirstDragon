from TypesOfPets import TypesOfPets
from typing import List


class Pet(object):
    def __init__(self, name: str, pet_type: TypesOfPets):
        self._name: str = name
        self._pet_type: str = pet_type
        self._hunger: int = 50
        self._happiness: int = 50
        self._energy: int = 50
        self._points: int = 0
        self._history: List[str] = []

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def pet_type(self) -> str:
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type: TypesOfPets) -> None:
        self._pet_type = pet_type

    @property
    def hunger(self) -> int:
        return self._hunger
    
    def change_hunger(self, hunger: int) -> None:
        """
        
        Changes hunger score
        :param hunger: How much do you want to reduce/add to your hunger param
        """
        self._hunger = self._hunger + hunger
        if self._hunger > 100:
            self._hunger = 100
        elif self._hunger <= 0:
            self.change_points(-30)
            self._hunger = 0
    
    @property
    def happiness(self) -> int:
        return self._happiness
    
    def change_happiness(self, happiness: int) -> None:
        """
        
        Changes happiness score
        :param happiness: How much do you want to reduce/add to your happiness param
        """
        self._happiness = self._happiness + happiness
        if self._happiness > 100:
            self._happiness = 100
        elif self._happiness <= 0:
            self.change_points(-30)
            self._happiness = 0

    
    @property
    def energy(self) -> int:
        return self._energy
    
    def change_energy(self, energy: int) -> None:
        """
        
        Changes energy score
        :param energy: How much do you want to reduce/add to your energy param
        """
        self._energy = self._energy + energy
        if self._energy > 100:
            self._energy = 100
        elif self._energy <= 0:
            self.change_points(-30)
            self._energy = 0
    
    @property
    def points(self) -> int:
        return self._points
    
    def change_points(self, points: int) -> None:
        """
        
        Changes points param
        :param points: How much do you want to reduce/add to your points param
        """
        self._points = self._points + points
        if self._points < 0:
            self._points = 0

    @property
    def history(self) -> List[str]:
        return self._history 
    
    def add_history_action(self, new_item: str) -> None:
        """
        
        Adding a new element to the list of actions performed in the game
        :param new_item: New element to the list
        """
        self._history.append(new_item)
    
    def eat(self) -> None:
        """
        
        Update pet parameters according to the eating actions
        """
        self.change_hunger(10)
        self.change_energy(5)
        self.change_happiness(5)
        self.change_points(10)
        self.add_history_action("eat")
        print("Your animal ate food!")


    def sleep(self) -> None:
        """
        
        Update pet parameters according to the sleeping actions
        """
        self.change_energy(10)
        self.change_happiness(5)
        self.change_points(10)
        self.add_history_action("sleep")
        print("Your animal went to sleep!")


    def play(self) -> None:
        """
        
        Update pet parameters according to the playing actions
        """
        self.change_happiness(10)
        self.change_energy(-7)
        self.change_hunger(-3)
        self.change_points(10)
        self.add_history_action("play")
        print("Your animal played!")
