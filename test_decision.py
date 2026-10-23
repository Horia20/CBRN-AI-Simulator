from core.scenario_engine import ScenarioEngine
from core.decision_engine import DecisionEngine

engine = ScenarioEngine()

world = engine.generate()

decision_engine = DecisionEngine()

result = decision_engine.evaluate(
    world,
    """
    Izolez zona.
    Evacuez populatia.
    Raportez superiorului.
    Initiez cercetare CBRN.
    """
)

world.print_state()

print()

print("Score:", result["score"])

print()

for item in result["feedback"]:

    print("-", item)