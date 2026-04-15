from ex0.factories import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    """
    Takes a list of opponents and runs a round-robin tournament.
    """
    print("*** Tournament ***")
    try:
        print(f"{len(opponents)} opponents involved")

        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory1, strategy1 = opponents[i]
                factory2, strategy2 = opponents[j]

                print("* Battle *")
                fighter1 = factory1.create_base()
                fighter2 = factory2.create_base()

                print(fighter1.describe())
                print("vs.")
                print(fighter2.describe())
                print("now fight!")

                try:
                    strategy1.act(fighter1)
                    strategy2.act(fighter2)
                except InvalidStrategyError as e:
                    print(e)
                    return
    except Exception as e:
        print(e)


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    opponents_basic = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
    ]
    battle(opponents_basic)

    print("\nTournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_error = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
    ]
    battle(opponents_error)

    print("\nTournament 2 (multiple)")
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    opponents_multi = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy),
    ]
    battle(opponents_multi)
