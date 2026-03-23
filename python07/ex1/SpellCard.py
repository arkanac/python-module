from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.effect = effect_type
        
    def play(self, game_state: dict) -> dict:
        self.resolve_effect(targets)
        game_state = {'card_played': self.name, 'mana_used': self.cost,
                      'effect': self.effect}
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        results = []
        for target in targets:
            if self.effect == 'damage':
                target['health'] -= 3
                results.append({'target': target['name'], 'effect': 'dealt 3 damage'})
            elif self.effect == 'heal':
                target['health'] += 3
                results.append({'target': target['name'], 'effect': 'restored 3 health'})
            elif self.effect == 'buff':
                target['attack'] += 1
                results.append({'target': target['name'], 'effect': '+1 attack'})
            elif self.effect == 'debuff':
                target['attack'] -= 1
                results.append({'target': target['name'], 'effect': '-1 attack'})
        return {'results': results}
    