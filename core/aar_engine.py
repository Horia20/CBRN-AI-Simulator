class AAREngine:

    def generate(
        self,
        world,
        score,
        readiness
    ):

        report = []

        report.append(
            "AFTER ACTION REVIEW"
        )

        report.append("=" * 40)

        report.append(
            f"Scenario: {world.scenario_name}"
        )

        report.append(
            f"Type: {world.scenario_type}"
        )

        report.append(
            f"Difficulty: {world.difficulty}"
        )

        report.append(
            f"Score: {score}"
        )

        report.append(
            f"Readiness: {readiness}"
        )

        report.append("")

        report.append("STRENGTHS")

        if world.mission_progress >= 30:
            report.append(
                "- Good mission execution"
            )

        if world.communications >= 80:
            report.append(
                "- Communications maintained"
            )

        if world.morale >= 80:
            report.append(
                "- High morale"
            )

        report.append("")

        report.append("WEAKNESSES")

        if world.contamination > 50:
            report.append(
                "- Contamination remains high"
            )

        if world.casualties > 100:
            report.append(
                "- High casualty count"
            )

        report.append("")

        report.append("RECOMMENDATIONS")

        report.append(
            "- Improve reconnaissance"
        )

        report.append(
            "- Expand decontamination capability"
        )

        report.append(
            "- Improve evacuation planning"
        )

        return "\n".join(report)