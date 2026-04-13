from abc import ABC, abstractmethod
from typing import cast

from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Custom exception raised when a creature is incompatible with a strategy."""
    pass


class BattleStrategy(ABC):
    
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Returns True if the creature has the required capabilities for this strategy."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Executes the sequence of actions for the given creature."""
        pass


class NormalStrategy(BattleStrategy):
    
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Battle error, aborting tournament: Invalid Creature '{creature.name}' for this normal strategy"
            )
        
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Battle error, aborting tournament: Invalid Creature '{creature.name}' for this aggressive strategy"
            )

        transformer = cast(TransformCapability, creature)
        # Sequence: transform -> attack -> revert
        print(transformer.transform())
        print(creature.attack())
        print(transformer.revert())


class DefensiveStrategy(BattleStrategy):
    
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Battle error, aborting tournament: Invalid Creature '{creature.name}' for this defensive strategy"
            )

        healer = cast(HealCapability, creature)
        # Sequence: attack -> heal
        print(creature.attack())
        print(healer.heal())
