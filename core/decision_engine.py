class DecisionEngine:

    def evaluate(
        self,
        world,
        decision
    ):

        text = decision.lower()

        score = 0

        feedback = []

        if "evacu" in text:

            world.mission_progress += 15

            score += 15

            feedback.append(
                "Evacuation initiated."
            )

        if "izol" in text:

            world.mission_progress += 10

            score += 10

            feedback.append(
                "Area isolated."
            )

        if "raport" in text:

            world.communications = min(
                100,
                world.communications + 5
            )

            score += 10

            feedback.append(
                "Command informed."
            )

        if "decont" in text:

            world.contamination = max(
                0,
                world.contamination - 10
            )

            score += 15

            feedback.append(
                "Decontamination started."
            )

        if (
            "cercet" in text
            or
            "recon" in text
        ):

            world.mission_progress += 10

            score += 15

            feedback.append(
                "Reconnaissance initiated."
            )

        if (
            "masca" in text
            or
            "protect" in text
        ):

            world.morale += 5

            score += 10

            feedback.append(
                "Protection measures implemented."
            )

        return {
            "score": score,
            "feedback": feedback
        }