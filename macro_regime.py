def detect_macro_regime(gas, copper, gold):
    """
    gas, copper, gold = forecast dicts
    """

    gas_bull = gas["bull"]
    copper_bull = copper["bull"]
    gold_bull = gold["bull"]

    if gas_bull > 40 and copper_bull > 40:
        return "Reflation"

    if gas_bull > 40 and copper_bull < 30:
        return "Stagflation"

    if gas_bull < 30 and copper_bull < 30:
        return "Recession"

    if gold_bull > 40 and copper_bull < 35:
        return "Risk-Off"

    return "Transition"
