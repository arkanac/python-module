#!/usr/bin/env python3
from ex0.CreatureCard import CreatureCard

print("=== DataDeck Card Foundation ===")
print()
print("Testing Abstract Base Class Design:")
available_mana = 10
game_state = {}
card = CreatureCard('Fire Dragon', 5, 'legendary', 7, 5)
print(card.get_card_info())
print(card.play(game_state, available_mana))
print("Fire Dragon attacks Goblin Warrior:")
print(card.attack_target("Goblin Warrior"))
print()
available_mana = 3
print("Testing insufficient mana (3 available):")
print(card.play(game_state, available_mana))
print()
print("Abstract pattern successfully demonstrated!")
