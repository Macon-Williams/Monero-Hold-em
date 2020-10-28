import time

from deck_of_cards import deck_of_cards
from Player import Player
from Table import Table


def player_draw(deck, player):
    for i in range(2):
        for j in range(len(player)):
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
    num_of_players = int(input("How many players? (1-9)"))
    for i in range(num_of_players):
        name_of_player = input(f"Name {i+1}?")
        player.append(Player(name_of_player, 1, i))
    table = Table()
    deck.shuffle_deck()
    # Assign initial role (Dealer, little blind, big blind)
    for i in range(len(player)):
        if i == 0:
            player[i].role.append("Dealer")

    flop(deck, table)
    table.list_cards()

    time.sleep(1)
    turn(deck, table)
    river(deck, table)
    print("\nTable: ")
    table.list_cards()
