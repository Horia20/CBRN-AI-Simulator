from dataclasses import dataclass, field

@dataclass
class WorldState:

    turn: int = 1

    mission_time: int = 0

    scenario_name: str = ""

    scenario_type: str = ""

    difficulty: str = "MEDIUM"

    casualties: int = 0

    population: int = 0

    contamination: int = 50

    morale: int = 100

    communications: int = 100

    mission_progress: int = 0

    resources: dict = field(default_factory=lambda: {
        "cbrn_teams": 2,
        "medical_teams": 2,
        "ambulances": 3,
        "decon_units": 2,
        "vehicles": 5
    })

    def next_turn(self):

        self.turn += 1

        self.mission_time += 15

    def print_state(self):

        print("\n========== WORLD STATE ==========")

        print("Scenario:", self.scenario_name)

        print("Type:", self.scenario_type)

        print("Difficulty:", self.difficulty)

        print("Turn:", self.turn)

        print("Time:", self.mission_time)

        print("Population:", self.population)

        print("Casualties:", self.casualties)

        print("Contamination:", self.contamination)

        print("Morale:", self.morale)

        print("Communications:", self.communications)

        print("Mission Progress:", self.mission_progress)

        print("Resources:", self.resources)

        print("=================================")