def mage_counter() -> callable:
    mage_count = 0

    def count_mage() -> int:
        nonlocal mage_count
        mage_count += 1
        return mage_count
    return count_mage


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def accumulator_count(n) -> int:
        nonlocal power
        power += n
        return power
    return accumulator_count


def enchantment_factory(enchantment_type: str) -> callable:

    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply_enchantment


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main():
    print("Testing mage counter...")
    c = mage_counter()
    for _ in range(0, 5):
        print(c())
    print(c.__code__.co_freevars)

    print("\nTesting spell accumulator...")
    spell_power = spell_accumulator(100)
    print(spell_power(0))
    print(spell_power(20))
    print(spell_power(50))

    print("\nTesting enchantment factory...")
    flame_factory = enchantment_factory("Flame")
    ice_factory = enchantment_factory("Ice")
    print(flame_factory("sword"))
    print(ice_factory("shield"))

    print("\nTesting memory vault...")
    bank = memory_vault()
    bank["store"]("secret", 42)
    print(bank["recall"]("secret"))
    print(bank["recall"]("nothing"))






if __name__ == "__main__":
    main()