from core.scenario_engine import ScenarioEngine
from core.decision_engine import DecisionEngine
from core.scoring_engine import ScoringEngine

engine = ScenarioEngine()

world = engine.generate()

decision_engine = DecisionEngine()

decision_engine.evaluate(
    world,
    """
    Izolez zona.
    Evacuez populatia.
    Raportez superiorului.
    Initiez cercetare CBRN.
    """
)

scoring = ScoringEngine()

score = scoring.calculate(world)

level = scoring.readiness_level(score)

world.print_state()

print()

print("FINAL SCORE:", score)

print("READINESS:", level)