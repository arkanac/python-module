from functools import lru_cache, singledispatch
from collections.abc import Callable
from typing import Any


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Error: n must be a positive int!")
    if n == 0 or n == 1:
        return n
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def cast(spell):
        return "Unknown type"

    @cast.register
    def _(x: int):
        return f"Damage dealt: {x}"

    @cast.register
    def _(x: str):
        return f"Enchantment: {x}"

    @cast.register
    def _(x: list):
        return f"Multi-cast result: {[cast(z) for z in x]}"

    return cast


def main():
    print("Testing Fibonacci:")
    print(memoized_fibonacci(60))
    print(memoized_fibonacci.cache_info())
    print()
    print("Testing dispatcher")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("Fireball"))
    print(cast(["Fire", "Ice", 12]))
    print(cast(3.14))


if __name__ == "__main__":
    main()
