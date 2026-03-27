"""Module for handling localization (translation)."""

LANG = "sv"

TRANSLATIONS = {
    "en": {
        "temperature": "Temperature",
        "solar_intensity": "Solar intensitet",
        "planet_albedo": "Planetary albedo",
        "infrared_emissivity": "Infrared emissivity",
        "optical_absorptivity": "Optical absorptivity",
        "unit.C": "°C",
        "unit.percent_of_present_value": "% of the present value",
        "unit.fraction": "fraction",
    },
    "sv": {
        "temperature": "Temperatur",
        "solar_intensity": "Solens intensitet",
        "planet_albedo": "Planetens albedo",
        "infrared_emissivity": "Infraröd emissivitet",
        "optical_absorptivity": "Optisk absorptionsförmåga",
        "unit.C": "°C",
        "unit.percent_of_present_value": "% av dagens värde",
        "unit.fraction": "andel",
    },
}


def tr(key, **kwargs):
    """Translate a key to the current language."""
    lang_table = TRANSLATIONS.get(LANG, {})
    en_table = TRANSLATIONS.get("en", {})

    translation = lang_table.get(key) or en_table.get(key) or key

    if kwargs:
        return translation.format(**kwargs)

    return translation
