
import random


class CardManager:
    def __init__(self):
        self.cards = set()

    def generate_card(self):
        suit = random.choice(['C', 'D', 'H', 'S'])
        number = random.randint(1,13)
        card = (suit, number)

        if card not in self.cards:
            return card
        elif len(self.cards) == 52:
            raise Exception("all cards drawn")
        else:
            return self.generate_card()
 
    def draw_card(self, player):
        new_card = self.generate_card()
        self.cards.add(new_card)
        player.cards.append(new_card)

class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []

    def first_card(self):
        if len(self.cards) > 0:
            return self.cards[0] 
        else:
            return None
            # raise Exception("No cards found")
    
    def calculate_hand_total(self, cards):
        count = 0
        for card in cards:
            pass



card_manager = CardManager()
Bob = Player("Bob")
for i in range(2):
    card_manager.draw_card(Bob)
    print(card_manager.cards)
    print(Bob.cards)

print(Bob.first_card())