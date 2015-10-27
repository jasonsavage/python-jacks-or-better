
'''
Created on Jul 24, 2013

@author: JSavage
'''

from games.jacks_or_better.card_deck import CardDeck
from games.jacks_or_better.poker_hands import PokerHands

"""
Main game class
"""
class JacksOrBetter(object) :
    
    @staticmethod
    def get_version() :
        return 1.0
    
    payout = [
        [0, 0, 0, 0, 0],            # no hand
        [1, 2, 3, 4, 5],            # Jacks or Better
        [2, 4, 6, 8, 10],           # Two Pair
        [3, 6, 9, 12, 15],          # Three of a Kind
        [4, 8, 12, 16, 20],         # Straight
        [6, 12, 18, 24, 30],        # Flush
        [9, 18, 27, 36, 45],        # Full House
        [25, 50, 75, 100, 125],     # Four of a Kind
        [50, 100, 150, 200, 250],   # Straight Flush
        [250, 500, 750, 1000, 4000] # Royal Flush
    ]
    
    payout_names = [
        "no hand",
        "Jacks or Better",
        "Two Pair",
        "Three of a Kind",
        "Straight",
        "Flush",
        "Full House",
        "Four of a Kind",
        "Straight Flush",
        "Royal Flush"
    ]
    
    
    def __init__(self):
        # init views
        self.views = JacksOrBetterViews()
        self.views.show_title_screen()
        
        # set game variables
        self.credits = 1000
        self.bet = 0
        self.bet_by = 25
        
    def play(self):
        
        if self.credits < self.bet_by :
            print("out of credits")
            self.end(False)
            return
        
        # create a new deck of cards
        deck = CardDeck()
        
        # show score board
        self.views.show_score_board()
        self.views.show_credits(self.credits, self.bet_by)
        
        # ask for bet
        raw = raw_input("Enter your bet (1, 2, 3, 4, 5): ")

        # validate bet
        while not self.bet_valid(raw) :
            raw = raw_input("invalid bet, please enter (1, 2, 3, 4, 5): ")
        
        self.bet = int(raw)
        
        self.views.show_bet(self.bet * self.bet_by)
        
        # deal 5 cards to player 1
        cards = deck.deal_hand()
        
        #show hand
        self.views.show_cards(cards)
        
        hold = []
        c = 0 
        print("Which card would you like to hold? (1, 2, 3, 4, 5) (enter to continue)")
        while c != -1 and len(hold) < 5 : 
            raw = raw_input(">>> ").strip()
            c = int(raw) if raw and raw.isdigit() else -1
            if c != -1 and c not in range(1, 6) :
                print("you have entered an invalid card")
            elif c in hold :
                print("you've already selected " + str(c))
            elif c != -1 :
                hold.append(c)
            # else :  c == -1 
        
        # replace cards in hand
        cards = deck.deal_second_hand(cards, hold)
        
        #show hand
        self.views.show_cards(cards)
        
        # compare hand 
        hand_id = self.calculate_hand(cards)
        
        if hand_id == 0 :
            # player didn't win
            self.credits -= self.bet * self.bet_by
            self.views.show_lost(self.credits)
        else :
            # player won, add winnings to credits
            self.credits += self.payout[hand_id][(self.bet-1)] # self.bet = 1 - 5 but payout is 0 - 4
            self.views.show_won(self.credits, self.payout_names[hand_id])
        
        # ask to play again
        self.end(True)
        
    # end play()
    
    def end(self, allow_replay):
        if allow_replay and self.credits >= self.bet_by :
            replay = raw_input("Would you like to play again? (y/n): ")
            if replay.lower() == 'y' :
                return self.play()

        self.views.show_gameover()
            
    # end end()
    
    def bet_valid(self, bet=''):
        
        print("bet: ", bet)
        
        if len(bet) == 0 or not bet.isdigit() :
            return False
        
        valid_bets = [1,2,3,4,5]
        int_bet = int(bet)
        ret = (int_bet in valid_bets)
        
        if ret :
            # need to check if player has enough credits
            bet_credits = int_bet * self.bet_by
            ret = bet_credits <= self.credits
        
        return ret
    
    # end bet_valid()
    
    def calculate_hand(self, hand):
        poker_hand = PokerHands(hand)
        
        if poker_hand.is_royal_flush() :
            return 9
        elif poker_hand.is_straight_flush() :
            return 8
        elif poker_hand.is_four_of_a_kind() :
            return 7
        elif poker_hand.is_full_house() :
            return 6
        elif poker_hand.is_flush() :
            return 5
        elif poker_hand.is_straight() :
            return 4
        elif poker_hand.is_three_of_a_kind() :
            return 3
        elif poker_hand.is_two_pair() :
            return 2
        elif poker_hand.is_jacks_or_better() :
            return 1
        else :
            return 0
    # end calculate_hand()
    
# end class JacksOrBetter()    
        

class JacksOrBetterViews(object):
    
    def show_title_screen(self):
        print("+-------------------------------------------------+")
        print(" Welcome to Python Jacks or Better")
        print("  > author: Jason Savage")
        print("  > version: " + str( JacksOrBetter.get_version() ))
        print("+-------------------------------------------------+")
    
    def show_score_board(self):
        print("+-------------------------------------------------+")
        print("| Hand            |  1  |  2  |  3  |  4   |  5   |")
        print("+-------------------------------------------------+")
        print("| Royal Flush     | 250 | 500 | 750 | 1000 | 4000 |")
        print("| Straight Flush  | 50  | 100 | 150 | 200  | 250  |")
        print("| Four of a Kind  | 25  | 50  | 75  | 100  | 125  |")
        print("| Full House      | 9   | 18  | 27  | 36   | 45   |")
        print("| Flush           | 6   | 12  | 18  | 24   | 30   |")
        print("| Straight        | 4   | 8   | 12  | 16   | 20   |")
        print("| Three of a Kind | 3   | 6   | 9   | 12   | 15   |")
        print("| Two Pair        | 2   | 4   | 6   | 8    | 10   |")
        print("| Jacks or Better | 1   | 2   | 3   | 4    | 5    |")
        print("+-------------------------------------------------+")
        
    def show_credits(self, creds, bet_cost=0):
        if bet_cost != 0 :
            print("Credits : " + str(creds) + " (" + str(bet_cost) + " credits each)")
        else :
            print("Credits : " + str(creds))
        print("+-------------------------------------------------+")
    
    def show_bet(self, bet):
        print("Bet : " + str(bet))
        
    def show_cards(self, hand):
        print("+---+ +---+ +---+ +---+ +---+")
        print("| " + self.fix_card_name(hand[0]) + "| | " + self.fix_card_name(hand[1]) + "| | " + self.fix_card_name(hand[2]) + "| | " + self.fix_card_name(hand[3]) + "| | " + self.fix_card_name(hand[4]) + "| ")
        print("| " + hand[0].suit + " | | " + hand[1].suit + " | | " + hand[2].suit + " | | " + hand[3].suit + " | | " + hand[4].suit + " | ")
        print("+---+ +---+ +---+ +---+ +---+")
        print("  1     2     3     4     5  ")
    
    def fix_card_name(self, card):   
        if len(card.name) > 1 :
            return card.name
        return card.name + " "
    
    def show_won(self, creds, hand_name):
        print("You win! " + hand_name)
        self.show_credits(creds)
    
    def show_lost(self, creds):
        print("You lost.")
        self.show_credits(creds)
        
    def show_gameover(self):
        print("+-------------------------------------------------+")
        print("|                    Game Over                    |")
        print("+-------------------------------------------------+")
        
        
# end class JacksOrBetterViews()       

