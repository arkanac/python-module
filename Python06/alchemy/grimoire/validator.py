from .spellbook import record_spell


def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]

    for element in valid:
        if element in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
