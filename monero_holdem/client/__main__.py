import time
from rich import print
from pyfiglet import Figlet
import configparser

config = configparser.ConfigParser()
user_data = config.read('config.ini')


def query_yes_no(question, default="no"):
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}

    while True:
        print(question)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Not a valid response, ('y' or 'n').")


def init_user():
    time.sleep(1)
    print("There is no local user data available. I'm going to ask you a couple questions...")
    time.sleep(2)
    name = input("What should we call you? (Enter your username)\n")
    time.sleep(0.5)
    print(f"Welcome {name}! (You can always change this later).")
    time.sleep(1)
    while True:
        print("Where should your winnings and payouts go? (Enter your [bold red]XMR wallet address[/bold red]):")
        address = input()
        if len(address) == 95:
            if address[0] == '8' or address[0] == '4':
                if query_yes_no(
                        f"You entered:[bold green]\n{address}\n[/bold green]Is this absolutely correct? (Any payouts "
                        f"will become [bold red]lost in the sauce[/bold red] if the address is not valid!)"):
                    print("Ok, that address will be saved.")
                    break
            else:
                print("This is an improper address. It should start with an 8 or a 4.")
        else:
            print("This is an improper address. It should have a length of 95 characters.")
        time.sleep(0.5)

    config[name] = {'XMR_Wallet_Addr': address}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


if __name__ == '__main__':
    title_text = Figlet(font='standard')
    print(title_text.renderText("Monero Casino"))
    print("Welcome to the [bold yellow]Monero Casino![/bold yellow]")
    if not user_data:
        init_user()
    else:
        print(config.sections())
        #for section in config.sections():
        #    print(section)