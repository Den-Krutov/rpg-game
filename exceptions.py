class ValueNotNumber(ValueError):
    def __init__(self, value: int, range_value: tuple) -> None:
        self.message = f'{value} должен быть числом в {range_value}'

    def __str__(self) -> str:
        return self.message
