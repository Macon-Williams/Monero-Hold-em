import time

from deck_of_cards import deck_of_cards
from Player import Player
from Table import Table


def player_draw(deck, player):
    for i in range(2):
        for j in player:
            player[j].cards.append(deck.give_first_card())


def flop(deck, table):
    # Burn a card
    deck.give_first_card()
    for i in range(3):
        table.cards.append(deck.give_first_card())
    table.flop = True


def turn(deck, table):
    # Burn a card
    deck.give_first_card()
    table.cards.append(deck.give_first_card())
    table.turn = True


def river(deck, table):
    # Burn a card
    deck.give_first_card()
    table.cards.append(deck.give_first_card())
    table.river = True


def initial_bet(deck, table, player):
    player_draw(deck, player)


class Holdem(object):
    deck = deck_of_cards.DeckOfCards()
    player = []
    role = ["deal", "bb", "sb"]
    num_of_players = int(input("How many players? (1-9)"))
    for i in range(num_of_players):
        name_of_player = input(f"Name {i+1}?")
        player.append(Player(name_of_player, 1, i))
    table = Table()
    deck.shuffle_deck()

    # Assign roles (Dealer, little blind, big blind)
    # Probably figure out how to make this better, 3 for loops is chonky.

    # Initialize the array
    for i in range(len(player)):
        for j in range(len(player)):
            player[i].role.append("player")

    # Assign dealer, big blind, and small blind rounds
    for i in range(len(player)):
        for j in range(len(player)):
            if j < 3:
                player[i].role[j] = role[j]

    # Rotate turns around
    for i in range(len(player)):
        player[i].role = (player[i].role[len(player[i].role) - i:len(player[i].role)] + player[i].role[0:len(player[i].role) - i])

    flop(deck, table)
    table.list_cards()

    time.sleep(1)
    turn(deck, table)
    river(deck, table)
    print("\nTable: ")
    table.list_cards()
