import time

from deck_of_cards import deck_of_cards
from Player import Player
from Table import Table

# Blind values in XMR
SMALL_BLIND = 0.005
BIG_BLIND = 0.01


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


# Assign roles (dealer, little blind, big blind)
# Probably figure out how to make this better, 3 for loops is chonky.
def assign_roles(player):
    role = ["deal", "bb", "sb"]
    # Initialize the array according to the number of players
    for i in range(len(player)):
        for j in range(len(player)):
            player[i].role.append("player")

    # Assign dealer, big blind, and small blind roles
    for i in range(len(player)):
        for j in range(len(player)):
            if j < 3:
                player[i].role[j] = role[j]

    # Stagger the roles so that each round the blinds get shifted to a new player
    for i in range(len(player)):
        player[i].role = (player[i].role[len(player[i].role) - i:len(player[i].role)] + player[i].role[
                                                                                        0:len(player[i].role) - i])


# Forces small blind and big blind to put in money before cards are drawn
def blind_bet(table, player):
    for i in range(len(player)):
        if player[i].role[0] == "bb":
            table.add_pot(player[i].bet_money(BIG_BLIND))
        if player[i].role[0] == "sb":
            table.add_pot(player[i].bet_money(SMALL_BLIND))


class Holdem(object):
    table = Table()
    deck = deck_of_cards.DeckOfCards()
    players = []

    # This is to test for now, the client will supply server with player information
    num_of_players = int(input("How many players? (1-9)"))
    for i in range(num_of_players):
        name_of_player = input(f"Name {i + 1}?")
        players.append(Player(name_of_player, 1, i))

    deck.shuffle_deck()
    assign_roles(players)
    flop(deck, table)
    time.sleep(1)
    turn(deck, table)
    time.sleep(1)
    river(deck, table)
