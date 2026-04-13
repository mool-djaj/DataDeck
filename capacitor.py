from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_family() -> None:
    """Tests the describe, attack, and heal sequence for the healing family."""
    factory = HealingCreatureFactory()
    
    print("Testing Creature with healing capability")
    print("base:")
    base_creature = factory.create_base()
    if not isinstance(base_creature, HealCapability):
        raise TypeError("Healing factory returned creature without HealCapability")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal())

    print("evolved:")
    evolved_creature = factory.create_evolved()
    if not isinstance(evolved_creature, HealCapability):
        raise TypeError("Healing factory returned creature without HealCapability")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal())

def test_transforming_family() -> None:
    """Tests the describe, attack, transform, attack, revert sequence for the transforming family."""
    factory = TransformCreatureFactory()
    
    print("Testing Creature with transform capability")
    print("base:")
    base_creature = factory.create_base()
    if not isinstance(base_creature, TransformCapability):
        raise TypeError("Transform factory returned creature without TransformCapability")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())

    print("evolved:")
    evolved_creature = factory.create_evolved()
    if not isinstance(evolved_creature, TransformCapability):
        raise TypeError("Transform factory returned creature without TransformCapability")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())

if __name__ == "__main__":
    test_healing_family()
    test_transforming_family()
