def adjust_metals_for_regime(metals, regime):
    for metal in metals:
        if regime == "Recession":
            if metal["commodity"] in ["Silver", "Copper"]:
                metal["bear"] += 5
                metal["bull"] -= 5

        if regime == "Stagflation":
            if metal["commodity"] == "Gold":
                metal["bull"] += 5
                metal["bear"] -= 5

        if regime == "Reflation":
            if metal["commodity"] in ["Copper", "Silver"]:
                metal["bull"] += 5
                metal["bear"] -= 5

    return metals
