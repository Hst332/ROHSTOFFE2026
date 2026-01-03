def metals_macro_signal(metals):
    signals = {
        "Gold": metals[0]["bull"],
        "Silver": metals[1]["bull"],
        "Copper": metals[2]["bull"]
    }

    if signals["Copper"] > 40 and signals["Gold"] > 40:
        return "Global reflation / structural demand"
    elif signals["Copper"] < 30 and signals["Gold"] > 40:
        return "Late cycle / risk-off"
    else:
        return "Transition phase"
