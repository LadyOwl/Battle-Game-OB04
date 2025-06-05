from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    name = "Меч"
    def attack(self):
        print("Боец наносит удар мечом")

class Bow(Weapon):
    name = "Лук"
    def attack(self):
        print("Боец наносит удар луком")

class Fighter:
    def __init__(self, name):
        self.name = "Боец"
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.name}")

    def attack(self):
        if self.weapon:
            (self.weapon.attack())
        else:
            print("Оружия нет")

class Monster:
    def __init__(self, name):
        self.name = "Монстр"
        self.health = 100

    def take_damage(self):
        self.health = 0
        print(f"{self.name} побежден!")

def battle(fighter: Fighter, monster: Monster):
        fighter.attack()
        monster.take_damage()

def weapon_name(weapon: Weapon):
    names = {
        'Sword': "меч",
        'Bow': "лук"
    }
    return names.get(weapon.__class__.__name__, weapon.__class__.__name__)


if __name__ == "__main__":
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    sword = Sword()


    fighter.change_weapon(sword)

    battle(fighter, monster)
    print()

monster2 = Monster("Монстр 2")
bow = Bow()
fighter.change_weapon(bow)
battle(fighter, monster2)
