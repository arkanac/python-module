from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict, available_mana: int) -> dict:
        if self.is_playable(available_mana):
            game_state = {'card_played': self.name, 'mana_used':
                          self.cost, 'effect': 'Creature '
                          'summoned to battlefield'}
            print(f"Playing {self.name} with {available_mana} available")
            print("Playable: True")
            return f"Play result: {game_state}"
        else:
            return "Playable: False"

    def get_card_info(self) -> dict:
        return {'name': self.name, 'cost': self.cost, 'rarity': self.rarity,
                'attack': self.attack, 'health': self.health}

    def is_playable(self, available_mana: int) -> bool:
        if self.cost > available_mana:
            return False
        return True

    def attack_target(self, target: str) -> dict:
        attack_result = {'attacker': self.name, 'target': target,
                         'damage dealt': self.attack, 'combat_resolved':
                         'True'}
        return attack_result
