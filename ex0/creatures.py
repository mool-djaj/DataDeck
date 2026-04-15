from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, typ: str) -> None:
        self.name = name
        self.typ = typ

    @abstractmethod
    def attack(self) -> str:
        """Abstract method to be implemented by concrete creatures."""
        pass

    def describe(self) -> str:
        """Concrete generic method returning a standard message."""
        return f"{self.name} is a {self.typ} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", typ="Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", typ="Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", typ="Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", typ="Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
