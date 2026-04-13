from ex0.factories import CreatureFactory
from ex0.creatures import Creature
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        """Returns the base creature for the healing family."""
        return Sproutling()

    def create_evolved(self) -> Creature:
        """Returns the evolved creature for the healing family."""
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        """Returns the base creature for the transforming family."""
        return Shiftling()

    def create_evolved(self) -> Creature:
        """Returns the evolved creature for the transforming family."""
        return Morphagon()
