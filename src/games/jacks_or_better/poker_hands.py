'''
Created on Jul 25, 2013

@author: JSavage
'''

class PokerHands(object):
    '''
    This class is used to compare poker hands of 5 cards
    '''
    royals = ["J","Q","K","A"]
    
    four_of_a_kind  = False
    three_of_a_kind = False
    two_of_a_kind   = False
    two_of_a_kind_royal = False
    two_pairs       = False
    
    def __init__(self, cards):
        self.cards = sorted(cards)
        self.grouped_cards = self.group_cards_by_name()
        # grouped_cards = ex. {"A" : [card(),card()], "5" : [card()] }
        
        #pre check for pairs
        for key in self.grouped_cards :
            length = len(self.grouped_cards[key])
            if length == 4 :
                self.four_of_a_kind = True
            elif length == 3 :
                self.three_of_a_kind = True
            elif length == 2 :
                # if we already have a pair then 2 pair
                if self.two_of_a_kind : 
                    self.two_pairs = True
                else :
                    # else 1 pair
                    self.two_of_a_kind = True 
                # check if its a pair of royal cards
                if key in self.royals :
                    self.two_of_a_kind_royal = True
              
    # end __init__()    

    def is_royal_flush(self):
        if self.is_straight_flush() and self.cards[0] == "10" :
            return True
        return False
    # end is_royal_flush()
    
    def is_straight_flush(self):
        if self.is_flush() and self.is_straight() :
            return True
        return False
    # end is_straight_flush()
    
    def is_four_of_a_kind(self):
        return self.four_of_a_kind
    # end is_four_of_a_kind()
    
    def is_full_house(self):
        return (self.three_of_a_kind and self.Two_of_a_kind)
    # end is_full_house()
    
    def is_flush(self):
        # all cards are the same sute
        # (if any of the cards suit not equal to first card's suite then False)
        for card in self.cards :
            if card.suit != self.cards[0].suit :
                return False
        return True
    # end is_flush()
    

    def is_straight(self):
        # all cards are in order
        # (if any of the cards are not right after the next card then False)
        length = len(self.cards)
        for index, card in enumerate(self.cards) :
            if index != length-1 : # if not at end of list 
                if not card.is_before(self.cards[index+1]) : # compare this card to next
                    return False
        return True
    # end is_straight()
    
    def is_three_of_a_kind(self):
        return self.three_of_a_kind
    # end is_three_of_a_kind()
    
    def is_two_pair(self):
        return self.two_pairs
    # end is_two_pair()
    
    def is_jacks_or_better(self):  
        return self.two_of_a_kind_royal and not self.two_pairs
    # end is_jacks_or_better()
    
    # helpers
    def group_cards_by_name(self):
        """ creates an object where the key is the card.name and the value is a list of the cards with that name """
        group = {}
        for card in self.cards :
            if not card.name in group :
                group[card.name] = []
            group[card.name].append(card)
        return group
    # end group_cards_by_name()
    
# end class PokerHands