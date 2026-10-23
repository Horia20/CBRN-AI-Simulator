from core.scenario_engine import ScenarioEngine
from core.decision_engine import DecisionEngine
from core.scoring_engine import ScoringEngine
from core.aar_engine import AAREngine

engine = ScenarioEngine()

world = engine.generate()

decision_engine = DecisionEngine()

decision_engine.evaluate(
    world,
    """
    Izolez zona.
    Evacuez populatia.
    Raportez superiorului.
    Initiez cercetare.
    """
)

scoring = ScoringEngine()

score = scoring.calculate(world)

readiness = scoring.readiness_level(score)

aar = AAREngine()

report = aar.generate(
    world,
    score,
    readiness
)

print(report)