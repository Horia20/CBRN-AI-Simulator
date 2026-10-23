import random
from dataclasses import dataclass, field
from typing import Dict, List


# ==========================================================
# WORLD STATE
# ==========================================================

@dataclass
class WorldState:

    mission_time: int = 0

    threat_type: str = "CHEMICAL"

    wind_direction: str = "N"
    wind_speed: int = 10

    contamination_level: int = 50
    contamination_radius: int = 500

    civilians: int = 500
    military_personnel: int = 30

    casualties: int = 5

    evacuated_people: int = 0

    morale: int = 100

    communications_status: int = 100

    mission_progress: int = 0

    events: List[str] = field(default_factory=list)

    decisions: List[str] = field(default_factory=list)

    resources: Dict = field(
        default_factory=lambda: {
            "cbrn_teams": 2,
            "ambulances": 3,
            "decon_units": 2,
            "vehicles": 5
        }
    )

    def apply_decision(self, decision):

        text = decision.lower()

        self.decisions.append(decision)

        if "evacu" in text:

            count = random.randint(50, 300)

            self.evacuated_people += count

            self.civilians = max(
                0,
                self.civilians - count
            )

            self.mission_progress += 15

        if "izol" in text:

            self.mission_progress += 10

        if "raport" in text:

            self.mission_progress += 5

        if "decont" in text:

            self.contamination_level = max(
                0,
                self.contamination_level - 10
            )

            self.mission_progress += 15

        if "protect" in text or "masc" in text:

            self.morale += 5

        if "cercet" in text or "recon" in text:

            self.mission_progress += 10

    def advance_time(self, minutes=15):

        self.mission_time += minutes

        self.contamination_radius += random.randint(
            20,
            100
        )

        self.contamination_level = min(
            100,
            self.contamination_level + random.randint(1, 4)
        )

    def print_dashboard(self):

        print("\n" + "=" * 60)
        print("WORLD STATE")
        print("=" * 60)

        print(f"Time: T+{self.mission_time} min")

        print(f"Threat: {self.threat_type}")

        print(
            f"Wind: {self.wind_direction} "
            f"{self.wind_speed} km/h"
        )

        print(
            f"Contamination: "
            f"{self.contamination_level}%"
        )

        print(
            f"Radius: "
            f"{self.contamination_radius} m"
        )

        print(
            f"Casualties: "
            f"{self.casualties}"
        )

        print(
            f"Civilians: "
            f"{self.civilians}"
        )

        print(
            f"Evacuated: "
            f"{self.evacuated_people}"
        )

        print(
            f"Morale: "
            f"{self.morale}"
        )

        print(
            f"Comms: "
            f"{self.communications_status}%"
        )

        print(
            f"Mission Progress: "
            f"{self.mission_progress}%"
        )

        print("=" * 60)


# ==========================================================
# SCENARIO ENGINE
# ==========================================================

class ScenarioEngine:

    def __init__(self):

        self.scenarios = [

            {
                "name": "Chlorine Release",
                "type": "CHEMICAL",
                "description":
                    "Nor toxic rezultat in urma unui accident industrial.",
                "contamination": 70,
                "radius": 700,
                "casualties": 8,
                "civilians": 1500
            },

            {
                "name": "Sarin Attack",
                "type": "CHEMICAL",
                "description":
                    "Atac cu agent neurotoxic intr-o zona urbana.",
                "contamination": 90,
                "radius": 500,
                "casualties": 15,
                "civilians": 2500
            },

            {
                "name": "Dirty Bomb",
                "type": "RADIOLOGICAL",
                "description":
                    "Explozie cu contaminare radioactiva.",
                "contamination": 80,
                "radius": 1200,
                "casualties": 20,
                "civilians": 3000
            },

            {
                "name": "Anthrax Outbreak",
                "type": "BIOLOGICAL",
                "description":
                    "Focar biologic intr-o zona militara.",
                "contamination": 45,
                "radius": 250,
                "casualties": 5,
                "civilians": 700
            },

            {
                "name": "Nuclear Fallout",
                "type": "NUCLEAR",
                "description":
                    "Contaminare radioactiva pe suprafata extinsa.",
                "contamination": 95,
                "radius": 3000,
                "casualties": 30,
                "civilians": 6000
            }
        ]

    def generate(self):

        scenario = random.choice(
            self.scenarios
        )

        world = WorldState()

        world.threat_type = scenario["type"]

        world.contamination_level = (
            scenario["contamination"]
        )

        world.contamination_radius = (
            scenario["radius"]
        )

        world.casualties = (
            scenario["casualties"]
        )

        world.civilians = (
            scenario["civilians"]
        )

        world.wind_direction = random.choice(
            [
                "N",
                "S",
                "E",
                "W",
                "NE",
                "NW",
                "SE",
                "SW"
            ]
        )

        world.wind_speed = random.randint(
            5,
            25
        )

        return scenario, world

    def inject_event(self, world):

        events = [

            "Vantul isi schimba directia.",

            "Apar noi victime.",

            "Comunicatiile sunt afectate.",

            "Panica in randul populatiei.",

            "Ruta de evacuare este blocata.",

            "Este descoperita o sursa secundara de contaminare."
        ]

        event = random.choice(events)

        if "victime" in event:

            world.casualties += random.randint(
                1,
                8
            )

        if "Comunicatiile" in event:

            world.communications_status -= 15

        if "Panica" in event:

            world.morale -= 10

        if "directia" in event:

            world.wind_direction = random.choice(
                [
                    "N",
                    "S",
                    "E",
                    "W",
                    "NE",
                    "NW",
                    "SE",
                    "SW"
                ]
            )

        world.events.append(event)

        return event


# ==========================================================
# SCORING
# ==========================================================

def calculate_score(world):

    score = 0

    score += min(
        40,
        world.mission_progress
    )

    score += min(
        25,
        world.evacuated_people // 20
    )

    score += min(
        20,
        world.morale // 5
    )

    score += min(
        15,
        world.communications_status // 10
    )

    return score


# ==========================================================
# MAIN SIMULATOR
# ==========================================================

if __name__ == "__main__":

    engine = ScenarioEngine()

    scenario, world = engine.generate()

    print("\n" + "=" * 60)
    print("CBRN TACTICAL TRAINER")
    print("=" * 60)

    print("\nSCENARIO")
    print("-" * 60)

    print("Name:", scenario["name"])
    print("Type:", scenario["type"])
    print("Description:", scenario["description"])

    print(
        "\nMisiunea ta este sa gestionezi situatia "
        "pe parcursul a 5 runde."
    )

    for turn in range(1, 6):

        print("\n")
        print("=" * 60)
        print(f"RUNDA {turn}")
        print("=" * 60)

        world.print_dashboard()

        decision = input(
            "\nDecizia comandantului:\n> "
        )

        world.apply_decision(
            decision
        )

        event = engine.inject_event(
            world
        )

        print("\nEVENT OPERATIONAL:")

        print(event)

        world.advance_time(15)

    print("\n")
    print("=" * 60)
    print("FINAL REPORT")
    print("=" * 60)

    world.print_dashboard()

    score = calculate_score(world)

    print("\nSCOR FINAL:", score)

    if score >= 80:
        print("Evaluare: EXCELENT")

    elif score >= 60:
        print("Evaluare: BUNA")

    elif score >= 40:
        print("Evaluare: SATISFACATOARE")

    else:
        print("Evaluare: NECESITA ANTRENAMENT")

    input("\nApasa ENTER pentru iesire...")