
import random
from typing import Union

class CardManager:
    def __init__(self) -> None:
        self.cards = set()

    def generate_card(self) -> tuple[str, Union[int,str]]:
        suit: int = random.choice(['C', 'D', 'H', 'S'])
        NUMBERS = ['A'] + list(range(2,11)) + ['J', 'Q', 'K']
        number: Union[int, str] = random.choice(NUMBERS)
        card = (number, suit)

        if card not in self.cards:
            return card
        elif len(self.cards) == 52:
            raise Exception("all cards drawn")
        else:
            return self.generate_card()
 
    def draw_card(self, player) -> None:
        new_card: tuple[str, Union[int,str]] = self.generate_card()
        self.cards.add(new_card)
        player.cards.append(new_card)

class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []

    def first_card(self) -> Union[tuple, None]:
        if len(self.cards) > 0:
            return self.cards[0]
        else:
            return None
            # raise Exception("No cards found")

    def get_card_value(self, card: tuple[str, Union[list, int]]) -> Union[list[int, int], int]:
        number: Union[int, str] = card[0]
        if number == 'A':
            return [1, 11]
        elif number in ['J', 'Q', 'K']:
            return 10
        else:
            return number
    
    def calculate_hand_total(self, cards: list):
        count = [0]
        for card in cards:
            value: Union[list[int, int], int] = self.get_card_value(card)
            if type(value) == int:
                count = list(map(lambda x: x + value, count))
            else: #* 'A' returns [1,11]
                new_count = []
                for item in count:
                    new_item = [item + 1, item + 11]
                    new_count.extend(new_item)
                new_count = list(dict.fromkeys(new_count)) #* remove duplicates from list
                count = new_count
        return count



card_manager = CardManager()
Bob = Player("Bob")
for i in range(5):
    card_manager.draw_card(Bob)
    print(card_manager.cards)
    print(Bob.cards)

print(Bob.calculate_hand_total(Bob.cards))