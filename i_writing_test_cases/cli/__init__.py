from typing import List

from cli.menus import MenuChoice, display_main_menu
from gumball_machine import Coin, GumballMachine


class GumballMachineCLI:
    """The CLI wrapper for the gumball machine class which handles all user input."""

    def __init__(self, gumball_machine: GumballMachine):
        """Initializes the gumball machine CLI.
        """
        self.gumball_machine = gumball_machine
        self.unrecognized_coins: List[str] = []
        self.running = False

    def format_machine_balance_line(self) -> str:
        """Prints the current balance of the gumball machine.

        Returns:
            str: The formatted string of the current balance of the gumball machine.
        """
        return "# Your current balance is: ${:.2f}".format(self.gumball_machine.get_money() / 100)
    
    def run_insert_coin(self):
        """Provided a coin choice menu to the user and inserts the coin value into the gumball machine.
        """
        print("\n> Provide a coin by entering it's name. For example nickel, dime, quarter, etc.:",)
        coin_choice = input("* ")
        coin_choice_clean = coin_choice.strip().lower()

        if coin_choice_clean == "nickel":
            coin = Coin.NICKEL
        elif coin_choice_clean == "dime":
            coin = Coin.DIME
        elif coin_choice_clean == "quarter":
            coin = Coin.QUARTER
        else:
            print("\n! Invalid coin. All invalid coins will be returned upon requesting your unused change.")
            self.unrecognized_coins.append(coin_choice)
            return
        
        self.gumball_machine.insert_coin(coin)
        print('\n# Inserting coin...\n{}'.format(self.format_machine_balance_line()))

    def run_dispense_red_gumball(self):
        """Dispenses a red gumball to the user if there is enough money.
        """
        success = self.gumball_machine.dispense_red_gumball()
        if success:
            print("\n# Dispensing Red Gumball...")
        else:
            print("\n! Not enough money to dispense this gumball.")
        print(self.format_machine_balance_line())
    
    def run_dispense_yellow_gumball(self):
        """Dispenses a yellow gumball to the user if there is enough money.
        """
        success = self.gumball_machine.dispense_yellow_gumball()
        if success:
            print("\n# Dispensing Yellow Gumball...")
        else:
            print("\n! Not enough money to dispense this gumball.") 
        print(self.format_machine_balance_line())
    
    def run_return_change(self):
        """Withdraws the remaining money in the gumball machine and prints the value to the user.
        """
        change = self.gumball_machine.return_change()
        print("\n# Returning ${:.2f} in change.".format(change / 100))
        
        if self.unrecognized_coins:
            print("# The following coins were not recognized:")
            for coin in self.unrecognized_coins:
                print("# - {}".format(coin))
            self.unrecognized_coins = []

        self.running = False

    def run(self):
        """Runs the gumball machine loop allowing user interaction.
        """
        print("Welcome to the Gumball Machine!")
        self.running = True

        while self.running:
            main_menu_choice = display_main_menu()

            if MenuChoice.INSERT_COIN == main_menu_choice:
                self.run_insert_coin()
            elif MenuChoice.DISPENSE_RED_GUMBALL == main_menu_choice:
                self.run_dispense_red_gumball()
            elif MenuChoice.DISPENSE_YELLOW_GUMBALL == main_menu_choice:
                self.run_dispense_yellow_gumball()
            elif MenuChoice.RETURN_CHANGE == main_menu_choice:
                self.run_return_change()

        print("\nThank you for using the Gumball Machine!")