'''
  @Author: Uthsavi KP
  @Date: 2021-01-02 3:24:47
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-02 3:24:47
  @Title: To shuffle the deck of cards and distribute 9 cards to 4 players.  
'''
import itertools
import random

suits = "Clubs", "Diamonds", "Hearts", "Spades" 
rank = "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"

class DeckOfCards:

    @staticmethod
    def deck_of_cards():
        cards = list(itertools.product([ "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"],
                              ['Clubs', 'Diamonds', 'Hearts', 'Spades']))

        random.shuffle(cards)  #shuffling cards

        print("***Player 1 Cards***")          
        array_one = []
        for index in range(9):
            array_one.append(cards[index][0])
            print([ array_one[index] + " of "+ cards[index][1] ], end = " ")
            cards.remove(cards[index])

        print("\n")
        print("***Player 2 Cards***")
        array_two = []
        for indexOne in range(9):
            array_two.append(cards[indexOne][0])
            print([array_two[indexOne] + " of " + cards[indexOne][1] ], end = " " )
            cards.remove(cards[indexOne])
            
        print("\n")
        print("***Player 3 Cards***")
        array_three = []
        for indexTwo in range(9):
            array_three.append(cards[indexTwo][0])
            print([array_three[indexTwo] + " of " + cards[indexTwo][1] ], end = " ")
            cards.remove(cards[indexTwo])
            
        print("\n")
        print("***Player 4 Cards***\n")
        array_four = []
        for indexThree in range(9):
            array_four.append(cards[indexThree][0])
            print([array_four[indexThree] + " of " + cards[indexThree][1] ], end = " " )
            cards.remove(cards[indexThree])

if __name__ == "__main__":
    DeckOfCards.deck_of_cards()  