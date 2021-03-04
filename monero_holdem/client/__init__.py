from user import User
from pyfiglet import Figlet


def log(val):
    print(val)


class Client(object):
    def __init__(self, name, address):
        user = User(name, address)


if __name__ == '__main__':
    title_text = Figlet(font='standard')
    print(title_text.renderText("Monero Casino"))
    name = input("Enter your username:\n")
    print(f"Welcome {name}! (You can always change it later).")

    confirmed = False
    while not confirmed:
        address = input("Carefully copy and paste your XMR wallet address here:\n")
        print(f"You entered:\n{address}\nIs this absolutely correct? (Any payouts will become lost in the sauce if "
              f"the address is not valid!)")
        confirm = input("Y/N?")
        if "y" == confirm or "Y" == confirm:
            print("Ok, don't blame me if you lose all your money!")
            confirmed = True
