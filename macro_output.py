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
