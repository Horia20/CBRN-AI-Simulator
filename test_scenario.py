from core.scenario_engine import ScenarioEngine

engine = ScenarioEngine()

world = engine.generate()

world.print_state()