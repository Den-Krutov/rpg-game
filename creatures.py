from random import randint

from exceptions import ValueNotNumber


class Creature:
    DEFAULT_NAME: str = 'Unknown'
    MIN_ATTACK: int = 1
    MAX_ATTACK: int = 30
    MIN_DEFENCE: int = 1
    MAX_DEFENCE: int = 30
    MIN_HP: int = 0
    DEFAULT_MIN_DAMAGE: int = 0
    RANGE_ATTACK: tuple = (MIN_ATTACK, MAX_ATTACK)
    RANGE_DEFENCE: tuple = (MIN_DEFENCE, MIN_DEFENCE)
    RANGE_HP: tuple = (MIN_HP, float('inf'))

    def __init__(
            self,
            name: str = DEFAULT_NAME,
            attack: int = MIN_ATTACK,
            defence: int = MIN_DEFENCE,
            hp: int = MIN_HP,
            min_damage: int = DEFAULT_MIN_DAMAGE) -> None:
        self.name: str = str(name)
        self.attack: int = attack
        self.defence: int = defence
        self.hp: int = hp
        self.min_damage: int = min_damage

    def _check_on_number(self, number: int, range_number: tuple) -> int:
        try:
            if isinstance(number, (float, str)):
                number = int(float(number))
        except ValueError:
            raise ValueNotNumber(number, range_number)
        if range_number[0] > number:
            number = range_number[0]
        else:
            if range_number[1] < number:
                number = range_number[1]
        return number

    @property
    def attack(self) -> int:
        return self.__attack

    @attack.setter
    def attack(self, attack: int) -> None:
        self.__attack = self._check_on_number(attack, self.RANGE_ATTACK)

    @property
    def defence(self) -> int:
        return self.__defence

    @defence.setter
    def defence(self, defence: int) -> None:
        self.__defence = self._check_on_number(defence, self.RANGE_DEFENCE)

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, hp: int) -> None:
        self.__hp = self._check_on_number(hp, self.RANGE_HP)

    def _range_damage_border(self):
        return (self.MIN_HP, self.hp)

    @property
    def min_damage(self) -> int:
        return self.__min_damage

    @min_damage.setter
    def min_damage(self, min_damage: int) -> None:
        self.__min_damage = self._check_on_number(
            min_damage, self._range_damage_border())

    def range_damage(self) -> tuple:
        return (self.min_damage, self.hp)

    def alive(self) -> bool:
        return bool(self.hp)

    def take_hit(self) -> int:
        return randint(self.range_damage())

    def __str__(self) -> str:
        return (
            f'{self.name}: '
            f'атака-{self.attack}, защита-{self.defence}, здоровье-{self.hp}. '
            f'Живой?-{self.alive()}, урон-{self.range_damage()}')
