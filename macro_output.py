def macro_regime_output(regime, gas, metals):
    return {
        "macro_regime": regime,
        "horizon": "2026",
        "drivers": {
            "gas_bull": gas["bull"],
            "copper_bull": next(
                m for m in metals if m["commodity"] == "Copper"
            )["bull"],
            "gold_bull": next(
                m for m in metals if m["commodity"] == "Gold"
            )["bull"],
        },
        "interpretation": interpret_regime(regime),
        "confidence": regime_confidence(gas, metals)
    }
