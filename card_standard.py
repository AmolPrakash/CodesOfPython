from card import Card
import random

class Card_group:
    def __init__(self, cards=[]):
        self.cards = cards
        
    def nextCard(self):
        return self.cards.pop(0)
    
    def hasCard(self):
        return len(self.cards)>0
    
    def size(self):
        return len(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)

class Standard_deck(Card_group):
    def __init__(self):
        self.cards = []
        for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for v in range(2,15):
                self.cards.append(Card(v, s))



deck = Standard_deck()
deck.shuffle()
first_card = deck.nextCard()
print(first_card)
choice = input("Higher (h) or lower (l): ")
second_card = deck.nextCard()
print(second_card)

if (choice == 'h' and second_card.value > first_card.value) or (choice == 'l' and second_card.value < first_card.value):    
    print ('Right guess')
else:
    print ('Wrong guess')
