from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Атака мечом")

class Bow(Weapon):
    def attack(self):
        print("Атака луком")

class Fighter:
    def __init__(self, name):
        self.name = "Боец"
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} changed {weapon.__class__.__name__}")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print("Оружия нет")

class Monster:
    def __init__(self, name):
        self.name = "Монстр"
        self.health = 100

    def take_damage(self):
        self.health = 0
        print(f"{self.name} побежден!")

        