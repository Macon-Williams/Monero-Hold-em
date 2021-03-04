from monero_holdem.game.holdem import Holdem
from monero_holdem.game.user import User, Bot

# g = Game()  # holdem OR blackjack
g = Holdem()


user = User("beanhead", "asdffsdfsedgfsdggs", 0)
bot = Bot("bothead")
bot2 = Bot("bigbothead")

g.add_user(user)
g.add_user(bot)
g.add_user(bot2)

g.start_game()
