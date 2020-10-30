from monero_holdem.game import Holdem
from monero_holdem.game.user import User, Bot


# g = Game()  # holdem OR blackjack
g = Holdem()  #


user = User("beanhead", "eight@eight.com")
bot = Bot("bothead")

g.add_user(user)
g.add_user(bot)

g.start_game()

