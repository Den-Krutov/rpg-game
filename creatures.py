from random import randint


class Creature:
    # Написать для hp геттер и сеттер, добавить состояние alive
    DEFAULT_ATTACK: tuple = (1, 30)
    DEFAULT_DEFENCE: tuple = (1, 30)
    DEFAULT_HP: tuple = (1, 100)

    def __init__(
            self,
            name: str = 'unknown',
            attack: int = None,
            defence: int = None,
            hp: int = None) -> None:
        self.name: str = str(name)
        if not isinstance(attack, (int, float)):
            attack = randint(*self.DEFAULT_ATTACK)
        if not isinstance(defence, (int, float)):
            defence = randint(*self.DEFAULT_DEFENCE)
        if not isinstance(hp, (int, float)):
            hp = randint(*self.DEFAULT_HP)
        if hp < 0:
            hp = 0
        if not (self.DEFAULT_ATTACK[0] <= attack <= self.DEFAULT_ATTACK[1]):
            raise ValueError(
                f'attack должна быть в отрезке {self.DEFAULT_ATTACK}')
        if not (self.DEFAULT_DEFENCE[0] <= defence <= self.DEFAULT_DEFENCE[1]):
            raise ValueError(
                f'defence должна быть в отрезке {self.DEFAULT_DEFENCE}')
        self.attack: int = int(attack)
        self.defence: int = int(defence)
        self.hp: int = int(hp)

    def __str__(self) -> str:
        return (
            f'{self.name}: '
            f'attack-{self.attack}, defence-{self.defence}, hp-{self.hp}')
