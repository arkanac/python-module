from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.5)
    return "Fireball casted"


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = power = args[2] if len(args) > 2 else args[1]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


@power_validator(50)
def cast_spell(power: int, target: str) -> str:
    return f"Casting at {target} with power {power}"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying..."
                        f"(attempt {i+1}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(3)
def cast_fireball(power, target):
    import random
    if random.random() < 0.7:
        raise Exception("Spell fizzled!")
    return f"Fireball hits {target} with power {power}"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            c.isalpha() or c == " " for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("Testing timer")
    print(fireball())
    print()
    print("Testing validator")
    print(cast_spell("dragon", 60))
    print(cast_spell("dragon", 30))
    print()
    print("Testing retrying spell")
    print(cast_fireball(50, "dragon"))
    print()
    print("Testing MageGuild")
    guild = MageGuild()
    print(guild.validate_mage_name("Dumbledore"))
    print(guild.validate_mage_name("V0ldemort"))
    print(guild.cast_spell("Fireball", 30))
    print(guild.cast_spell("WaterJet", 5))


if __name__ == "__main__":
    main()
