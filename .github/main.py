from forecast_gas import forecast_gas_2026
from metals_bundle import forecast_metals_2026
from macro_regime import detect_macro_regime
from regime_adjustment import adjust_metals_for_regime
from macro_output import macro_regime_output

gas = forecast_gas_2026()
metals = forecast_metals_2026()["metals"]

regime = detect_macro_regime(
    gas=gas,
    copper=next(m for m in metals if m["commodity"] == "Copper"),
    gold=next(m for m in metals if m["commodity"] == "Gold")
)

metals = adjust_metals_for_regime(metals, regime)
macro = macro_regime_output(regime, gas, metals)

print(macro)
