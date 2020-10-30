from monero_holdem.game import Holdem
from monero_holdem.game.user import User, Bot


# g = Game()  # holdem OR blackjack
g = Holdem()  #


user = User("beanhead", "eight@eight.com")
bot = Bot("bothead")
bot2 = Bot("bigbothead")

g.add_user(user)
g.add_user(bot)
g.add_user(bot2)

g.start_game()

