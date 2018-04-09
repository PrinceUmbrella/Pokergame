# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 23:37:19 2018

@author: eleou
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
    '''
    It takes the Values and return the names of the function
    '''
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
    
    def __str__(self):
        return ("{} of {}".format(self.ranks,self.suits))

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        newList = ', '.join(str(i) for i in self.deck)
        return(newList)
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop(0)

   
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def __str__(self):
        cardList = ', '.join(str(i) for i in self.cards)
        return(cardList)
    def add_card(self,card):
        self.cards.append(card) #adds the card that it got from the deal(self)
        self.value += values[card.ranks] #gets the value from the rank and adds it self.value
        
        if card.ranks == "Ace":
            self.ace += 1
        
    def adjust_for_ace(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.aces -= 1
            
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        #takes the bet adds it the win
        self.total += self.bet
        return self.bet
    def lose_bet(self):
        #takes the bet substract it the win
        self.total -= self.bet
        return self.bet

def take_bet():
    
    try:
        user_Bet = input("How Much do you want to bet: ")
        Chips.total -= user_Bet
        Chips.bet = user_Bet
        return Chips.bet and Chips.total
    except ValueError:
        print("Your Bet has exceded the total amount")
    except:
        print("You have entered an error value")
    
#test_deck = Deck()
#test_deck.shuffle()
#print(test_deck)
#test_player = Hand()
#card_g = test_deck.deal()
#test_player.add_card(card_g)
#print(str(test_player.cards))
#print(test_player.value)
        
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()         
        
    
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    Ask_Hit = input("Do you want to Hit or Stand: ")
    while playing:
        if Ask_Hit in ["Hit", "hit"]:
            hit(deck,hand)
        elif Ask_Hit in ["Stand", "stand"]:
            playing = False
        else:
            print("You have Entered a wrong value")


def show_some(player,dealer):
    player = Hand()
    print(player.cards)
    dealer = Hand()
    newCards = ''
    for i in range(1,len(dealer.cards)):
        newCards += dealer.cards[i]
        newCards += ' '
    print("x*x " + newCards)
        
    
    
def show_all(player,dealer):
    player = Hand()
    print(player.cards)
    dealer = Hand()
    print(dealer.cards)
    
def player_busts():
    print("Player Bust")
    Chips.lose_bet()
    
def player_wins():
    print("Player Wins")
    Chips.win_bet()
    
def dealer_busts():
    print("Dealer Bust")
    Chips.lose_bet()
    
def dealer_wins():
    print("Dealer Wins")
    Chips.win_bet()
    
def push():
    
    pass
   
