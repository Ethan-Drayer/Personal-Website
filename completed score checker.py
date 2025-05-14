win = """   |     |   |-----|   |     |       |           |   --|--   |\\     |     || 
   |     |   |     |   |     |       |           |     |     | \\    |     || 
   |_____|   |     |   |     |       |           |     |     |  \\   |     || 
      |      |     |   |     |       |     |     |     |     |   \\  |     || 
      |      |     |   |     |       |     |     |     |     |    \\ |     || 
      |      |_____|   |_____|       |_____|_____|   __|__   |     \\|     :: """

lose = """         |     |   |-----|   |     |       |            |-----|  |----     |-----
         |     |   |     |   |     |       |            |     |  |         |
         |_____|   |     |   |     |       |            |     |  |____     |
            |      |     |   |     |       |            |     |       |    |-----
            |      |     |   |     |       |            |     |       |    |
            |      |_____|   |_____|       |_________   |_____|  _____/    |_____"""

tie = ("""---------------          ---------------          ---------------
      |                        |                  |
      |                        |                  |
      |                        |                  |
      |                        |                  | 
      |                        |                  |--------------
      |                        |                  | 
      |                        |                  | 
      |                        |                  |
      |                        |                  |
      |                   ---------------         |---------------""")

import random


def create_deck():
    deck = []
    card_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    card_suit = ['H', "S", "D", "C"]
    for suit in card_suit:
        for value in card_value:
            x = f"{value}{suit}"
            deck.append(x)
    random.shuffle(deck)
    # print(deck)

    return deck


new_deck = create_deck()

print(new_deck)


def print_cards(cards):
    # Blank message to start.
    message = ""

    # Loop through provided cards.
    for card in cards:
        # Check the value of the card.
        if card[:-1] == "A":
            value = "Ace"
        elif card[:-1] == "J":
            value = "Jack"
        elif card[:-1] == "Q":
            value = "Queen"
        elif card[:-1] == "K":
            value = "King"
        else:
            value = card[:-1]

        # Check the suit of the card.
        if card[-1:] == "S":
            suit = "Spades"
        elif card[-1:] == "D":
            suit = "Diamonds"
        elif card[-1:] == "C":
            suit = "Clubs"
        elif card[-1:] == "H":
            suit = "Heart"
        else:
            suit = "Undefined"

        # Add the value and suit of the cards to the message.
        message += f"\t{value} of {suit}\n"

    # Return the message.
    return message


def check_score(cards):
    score = 0

    # These cards have special point values.
    special_cases = ["J", "Q", "K", "A"]

    for card in cards:
        # If the card is not a special card (face, ace), add its points.
        if card[:-1] not in special_cases:
            score += int(card[:-1])
        else:
            # If the card is an ace, and 11 points can safely be added, then
            # add 11 points.
            if card[:-1] == "A" and score + 11 <= 21:
                score += 11
            # If 11 points cannot be added, then add 1 point.
            elif card[:-1] == "A" and score + 11 > 21:
                score += 1
            # Otherwise, if it's a face card, add 10 points.
            else:
                score += 10

    # Return the score of the cards.
    return score


'''
        Check is action == 'stand' or 'hit'
        if 'hit', deal another card
        if 'stand', check if they won the game
        if 'bust' or 'lose', end game with lose statement
        '''

dealer_score = 0


def player_hand():
    print(f"Player Hand: {player_cards}")


def deal_player():
    card1 = new_deck
    new_deck.remove(card1[0])
    card2 = new_deck
    new_deck.remove(card2[0])


# Initialize the player hand.
player_cards = [new_deck.pop(), new_deck.pop()]

# Display the player score.
player_hand()
player_score = check_score(player_cards)
print(f"Player's score is {player_score}")

player_bust = False

action = ""
while action != "stand":

    action = input("Would you like to 'hit' or 'stand'? ")

    # If the player hits, give them a new card.
    if action.lower() == 'hit':
        player_cards.append(new_deck.pop())
        player_hand()

        # Check if the player has busted
        player_score = check_score(player_cards)
        print(f"Player's score is {player_score}")

    if player_score > 21:
        print("You busted!")
        player_bust = True
        break
    else:
        player_bust = False

if not player_bust:
    dealer_bust = False

    # Below this point is all the new code.
    deck_of_cards = create_deck()

    # Pop two cards from the deck for the dealer. (This will eventually be
    # replaced by the actual code.)
    dealer_cards = [deck_of_cards.pop(), deck_of_cards.pop()]

    # Print each card that the dealer has.
    print("\nDealer has:")
    print(print_cards(dealer_cards))

    dealer_score = check_score(dealer_cards)

    print(f"\nDealer score is {dealer_score}")

    while dealer_score < 17:
        # Here we will deal a card and print the score.
        print("Dealer takes a card...")
        dealer_cards.append(deck_of_cards.pop())

        # Print each card that the dealer has.
        print("\nDealer has:")
        print(print_cards(dealer_cards))

        dealer_score = check_score(dealer_cards)

        print(f"\nDealer score is {dealer_score}")

        if dealer_score > 21:
            dealer_bust = True
            break

        if dealer_bust:
            print("\nDealer busted")

# insert player_score
# insert dealer_score
# if the player has 21
if player_score == 21:
    if dealer_score == 21:
        print(tie)
    else:
        print(win)
elif dealer_score == 21:  # if the dealer has 21, and player doesn't
    if player_score == 21:
        print(tie)
    else:
        print(lose)
else:  # if neither have 21
    if player_score > 21:
        print(lose)
    else:

        if dealer_score > 21:
            print(win)
        elif player_score > dealer_score:  # player's value is more than the dealer
            print(win)
        elif player_score == dealer_score:  # player's value is equal to dealer
            print(tie)
        elif player_score < dealer_score:  # player's value is less than dealer
            print(lose)
