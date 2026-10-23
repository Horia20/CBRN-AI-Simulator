class ScoringEngine:

    def calculate(self, world):

        score = 0

        score += min(
            30,
            world.mission_progress
        )

        score += min(
            20,
            world.morale // 5
        )

        score += min(
            20,
            world.communications // 5
        )

        score += min(
            30,
            100 - world.contamination
        )

        return min(
            100,
            score
        )

    def readiness_level(
        self,
        score
    ):

        if score >= 85:
            return "EXCELLENT"

        if score >= 70:
            return "GOOD"

        if score >= 50:
            return "SATISFACTORY"

        return "NEEDS IMPROVEMENT"