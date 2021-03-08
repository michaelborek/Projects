import random
import sys

suit = ["Hearts", "Clubs", "Diamonds", "Spades"]
rank = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
value = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10,
         "Queen": 10, "King": 10, "Ace": 11}


# Cards Logic
class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]

    def __str__(self):
        return self.suit + " of " + self.rank


# Deck Logic
class Deck:
    def __init__(self):
        self.my_deck = []

        for suits in suit:
            for ranks in rank:
                new_card = Cards(suits, ranks)
                self.my_deck.append(new_card)

    def shuffle_deck(self):
        random.shuffle(self.my_deck)

    def pop_card(self):
        return self.my_deck.pop(0)

    def hit(self, card):
        return self.my_deck.append(card)


# Player Logic
class Player:
    def __init__(self, name):
        self.name = name
        self.my_cards = []
        self.my_fund = 10

    def __str__(self):
        return f"Player has {self.my_cards}."

    def hit(self, card):
        return self.my_cards.append(card)

    def bid(self):
        while True:
            print(f"You've got {self.my_fund} tokens.")
            a = input("How many tokens do you want to bid: ")
            if self.my_fund >= int(a) > 0:
                print(f"You have bid {int(a)} tokens!")
                self.my_fund -= int(a)
                return int(a)
            else:
                print("You haven't got enough tokens in your wallet.")

    def adding_tokens(self, num):
        self.my_fund += num

    def show_cards(self):
        print("Your cards:")
        for card in self.my_cards:
            print(card)

    def value_of_cards(self):
        a = 0
        for card in self.my_cards:
            a += card.value
        return a

    def clear_list(self):
        self.my_cards.clear()

    def changing_ace(self):
        for card in self.my_cards:
            if card.value == 11 or card.value == 1:
                while True:
                    a = input("You've got Ace. Please choose 1 or 11: ")
                    if int(a) == 11:
                        card.value = 11
                        break
                    elif int(a) == 1:
                        card.value = 1
                        break
                    else:
                        print("Please choose between 1 or 11!")


# Card dealer Logic
class CardDealer:
    def __init__(self):
        self.cards = []

    def get_card(self, card):
        return self.cards.append(card)

    def show_cards(self, var):
        print("Card dealer's cards:")
        if var == 1:
            for card in self.cards:
                print(card)
        else:
            print(self.cards[0])

    def value_of_cards(self):
        a = 0
        for card in self.cards:
            a += card.value

        return a

    def clear_list(self):
        self.cards.clear()


# Drawing lines (estetic)
def pointing(var):
    if var == 1:
        print("----------------------------------------------------")
    elif var == 2:
        print("------")


# GAME LOGIC
pointing(1)
print("Welcome in BlackJack by Michael Borek!")
new_player = Player(Player)

game_on = True

while game_on:
    new_deck = Deck()
    card_dealer = CardDealer()
    new_deck.shuffle_deck()
    while True:
        bid = new_player.bid()

        # Giving cards
        for cards in range(2):
            new_player.hit(new_deck.pop_card())
            card_dealer.get_card(new_deck.pop_card())

        # Showing cards
        pointing(2)
        new_player.show_cards()
        pointing(2)
        card_dealer.show_cards(0)
        pointing(2)

        # First checking if player or card dealer has 21
        if new_player.value_of_cards() == 21 and card_dealer.value_of_cards() == 21:
            print("Draw!")
            card_dealer.show_cards(1)
            result = 1
            break
        elif new_player.value_of_cards() == 21:
            print("You have 21! You win!")
            result = 2
            break
        elif card_dealer.value_of_cards() == 21:
            print("Card dealer has 21! You lose!")
            card_dealer.show_cards(1)
            result = 0
            break

        while True:
            # Player's choice
            choice = input("Do you want hit or stand?: ")
            if choice.lower() == "hit":
                new_player.hit(new_deck.pop_card())
            elif choice.lower() == "stand":
                break
            else:
                print("Please choose between hit or stand!")

        # Checking if player has 21
        if new_player.value_of_cards() == 21:
            pointing(2)
            print("You have 21! You win!")
            new_player.show_cards()
            pointing(1)
            result = 2
            break

        pointing(2)
        # Showing player all his cards
        new_player.show_cards()
        new_player.changing_ace()
        pointing(2)

        # Checking how many points has card_dealer if under 17, he hits cards
        while card_dealer.value_of_cards() < 17:
            card_dealer.get_card(new_deck.pop_card())

        if new_player.value_of_cards() > 21:
            print("You have more than 21! You lose!")
            pointing(2)
            result = 0
            break
        elif card_dealer.value_of_cards() > 21:
            print("You win! Card dealer has more than 21!")
            card_dealer.show_cards(1)
            pointing(2)
            result = 2
            break
        elif card_dealer.value_of_cards() > new_player.value_of_cards():
            print("You lose! You have less values than card dealer!")
            card_dealer.show_cards(1)
            pointing(2)
            result = 0
            break
        elif card_dealer.value_of_cards() == new_player.value_of_cards():
            print("Draw! You and card dealer have the same values.")
            card_dealer.show_cards(1)
            pointing(2)
            result = 1
            break
        elif card_dealer.value_of_cards() < new_player.value_of_cards():
            print("You win! You have more values than card dealer!")
            card_dealer.show_cards(1)
            pointing(2)
            result = 2
            break

    # Adding bids
    if result == 2:
        print(f"You've won {2*bid}!")
        new_player.adding_tokens(2*bid)
        pointing(1)
    elif result == 1:
        print(f"You've won {bid}!")
        new_player.adding_tokens(bid)
        pointing(1)
    else:
        pointing(1)

    if new_player.my_fund == 0:
        print("You haven't got no more any funds, GAME OVER!")
        sys.exit()

    # LOGIC TO RESTART
    new_player.clear_list()

    card_dealer.clear_list()

    while True:
        inf = input("Do you want play again? Yes or No: ")
        if inf.lower() == "yes":
            break
        elif inf.lower() == "no":
            sys.exit()
        else:
            print("Please choose yes or no!")

