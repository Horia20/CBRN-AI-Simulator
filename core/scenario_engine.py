import json
import random

from core.world_state import WorldState


class ScenarioEngine:

    def __init__(self):

        with open(
            "data/scenarios.json",
            "r",
            encoding="utf-8"
        ) as f:

            self.scenarios = json.load(f)

    def generate(self):

        scenario = random.choice(
            self.scenarios
        )

        world = WorldState()

        world.scenario_name = scenario["name"]

        world.scenario_type = scenario["category"]

        world.difficulty = scenario["difficulty"]

        world.population = random.randint(
            500,
            10000
        )

        world.casualties = random.randint(
            5,
            250
        )

        world.contamination = random.randint(
            30,
            95
        )

        return world