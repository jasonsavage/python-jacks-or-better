
'''
Created on Jul 24, 2013

@author: JSavage
'''

import random

class CardDeck(object):
    suits = ["S","C","H","D"]
    names = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    
    def __init__(self):
        self.cards = []
        
        for n in self.names :
            for s in self.suits :
                self.cards.append( Card(n,s) )     
                  
    #end __init__()   
    
    def deal_hand(self):
        # shuffle
        random.shuffle(self.cards)
        
        #get first 5 cards
        ret = self.cards[:5]
        
        # remove cards from deck
        self.cards = self.cards[5:]
        
        # return hand
        return ret
        
    # end deal_hand()
    
    def deal_second_hand(self, hand, hold):
        # hold = 1,2,3,4,5
        # hand = [card(), card(), card(), card(), card()]
        
        # replace each card in hand with a new one from deck
        for i, card in enumerate(hand):
            if (i+1) not in hold :
                hand[i] = self.cards.pop()
        
        # return deck
        return hand
        
    # end deal_second_hand()

    def __repr__(self):
        return "(CardDeck object)"
    
#end class CardDeck()   


class Card(object):
    
    order = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    
    def __init__(self, name, suit):
        self.suit, self.name = suit, name
    
    def is_before(self, card):
        """ checks if this card is right before other card name """
        if self.name == "2" : 
            return False
        return card.name == self.order[self.order.index(self.name)-1]
    
    def __lt__(self, other) :
        return self.order.index(self.name) < self.order.index(other.name)
    
    def __repr__(self):
        return "(%s, %s)" % (self.name, self.suit)
    
#end class Card()   