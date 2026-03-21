from alchemy.grimoire import validate_ingredients, record_spell

print("=== Circular Curse Breaking ===")
print()
print("Testing ingredient validation:")
print("validate_ingredients(fire air):", validate_ingredients("fire air"))
print("validate_ingredients(dragon scales):", validate_ingredients
      ("dragon scales"))
print()
print("record_spell(Fireball, fire air):", record_spell("Fireball", "fire air"))
print("record_spell(Dark Magic, shadow):", record_spell("Dark Magic", "shadow"))
