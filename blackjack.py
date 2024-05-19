
import os
import random
from typing import Union

class CardManager:
    def __init__(self) -> None:
        self.drawn_cards = set()

    def generate_card(self) -> tuple[str, Union[int,str]]:
        suit: int = random.choice(['C', 'D', 'H', 'S'])
        NUMBERS = ['A'] + list(range(2,11)) + ['J', 'Q', 'K']
        number: Union[int, str] = random.choice(NUMBERS)
        card = (number, suit)

        if card not in self.drawn_cards:
            return card
        elif len(self.drawn_cards) == 52:
            raise Exception("all cards drawn")
        else:
            return self.generate_card()
 
    def draw_card(self) -> None:
        new_card: tuple[str, Union[int,str]] = self.generate_card()
        self.drawn_cards.add(new_card)
        return new_card


class Hand():
    def __init__(self, card_manager: 'CardManager', cards = []) -> None:
        self.cards = cards
        self.card_manager = card_manager
    
    def draw_card(self) -> None:
        new_card = self.card_manager.draw_card()
        self.cards.append(new_card)
    
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
    
    def calculate_hand_total(self, cards: list) -> list[int]:
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
    

class Player():
    def __init__(self, name, card_manager) -> None:
        self.name = name
        self.hands = [Hand(card_manager)]
        self.money = 500
    
    def show_hands(self) -> None:
        for i, hand in enumerate(self.hands, start = 1):
            print(f'{self.name} Hand No. {i}: {hand.cards}')

    def add_hand(self) -> None:
        self.hands.append(Hand(card_manager, cards = []))
    
    def draw_card(self, hand_number) -> None:
        self.hands[hand_number - 1].draw_card() #* hand_number starts from 1
    
    #! remember to sanitise input amount to int
    def transfer_money(self, receiver: 'Player', amount: int) -> None:
        '''
        Transfer money from player to receiver

        Args:
            receiver: Player that is receiving the money
            amount: amount to be transferred
        Returns:
            None

        '''
        self.money, receiver.money = self.money - amount, receiver.money + amount

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def exit_game() -> None:
    print("Exiting...")
    exit()


if __name__ == '__main__':
    card_manager = CardManager()
    Dealer = Player('Dealer', card_manager)
    Bob = Player("Bob", card_manager)
    print(Dealer.name, Dealer.hands[0].cards, Dealer.money)
    Dealer.draw_card(1)
    print(Dealer.hands[0].cards)
    Dealer.show_hands()
    Dealer.add_hand()

    print(Dealer.hands[0].cards, Dealer.hands[1].cards)
    Dealer.draw_card(2)
    Dealer.show_hands() 

    print(Dealer.money, Bob.money)
    Dealer.transfer_money(Bob, 69)
    print(Dealer.money, Bob.money)
    for i in range(2):
        Bob.draw_card(1)
        print(card_manager.drawn_cards)
        Bob.show_hands()

    # print(Bob.calculate_hand_total(Bob.cards))
    # exit_game()