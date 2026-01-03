def interpret_regime(regime):
    interpretations = {
        "Reflation": (
            "Gleichzeitiger Inflations- und Wachstumsdruck. "
            "Zyklische Rohstoffe profitieren, Absicherungsassets bleiben stabil."
        ),
        "Stagflation": (
            "Hohe Kosten treffen auf schwaches Wachstum. "
            "Energie und Gold werden bevorzugt, Industrie-Metalle unter Druck."
        ),
        "Recession": (
            "Nachfragerückgang dominiert. "
            "Industriemetalle schwach, Gold stabilisierend."
        ),
        "Transition": (
            "Uneinheitliche Signale. "
            "Märkte ohne klaren Trend, erhöhte Unsicherheit."
        )
    }
    return interpretations.get(regime, "")
    
def regime_confidence(gas, metals):
    copper = next(m for m in metals if m["commodity"] == "Copper")
    gold = next(m for m in metals if m["commodity"] == "Gold")

    spread = abs(gas["bull"] - copper["bull"])

    if spread > 20:
        return "hoch"
    if spread > 10:
        return "mittel"
    return "niedrig"

