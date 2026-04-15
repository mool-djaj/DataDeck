from ex0 import (
    AquaFactory,
    CreatureFactory,
    FlameFactory,
)


def test_factory(factory: CreatureFactory) -> None:
    """Verifies base and evolved creatures from a factory."""
    print("Testing factory")

    try:
        base_creature = factory.create_base()
        print(base_creature.describe())
        print(base_creature.attack())
        evolved_creature = factory.create_evolved()
        print(evolved_creature.describe())
        print(evolved_creature.attack())
    except Exception as e:
        print(e)


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    """Makes the base creatures from two different factories fight."""
    print("Testing battle")
    try:
        fighter1 = factory1.create_base()
        fighter2 = factory2.create_base()

        print(fighter1.describe())
        print("vs.")
        print(fighter2.describe())
        print("fight!")

        print(fighter1.attack())
        print(fighter2.attack())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)
