from typing import Literal, cast

from cli.menus import display_coin_menu, display_main_menu
from gumball_machine import GumballMachine


def convert_coin_menu_choice_to_cents(choice: Literal[0, 1, 2]) -> Literal[5, 10, 25]:
    """Converts the coin menu choice to the value of the coin in cents.

    Args:
        choice (Literal[0, 1, 2]): The coin menu choice.

    Returns:
        int: the value if the coin choice in cents, nickel (5), dime (10), and quarter (25).
    """
    return cast(Literal[5, 10, 25], [5, 10, 25][choice])



class GumballMachineCLI:
    """The CLI wrapper for the gumball machine class which handles all user input."""

    def __init__(self, gumball_machine: GumballMachine):
        """Initializes the gumball machine CLI.
        """
        self.gumball_machine = gumball_machine
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
        coin_choice = display_coin_menu()
        coin_value = convert_coin_menu_choice_to_cents(coin_choice)
        self.gumball_machine.insert_coin(coin_value)
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
        self.running = False

    def run(self):
        """Runs the gumball machine loop allowing user interaction.
        """
        print("Welcome to the Gumball Machine!")
        self.running = True

        while self.running:
            main_menu_choice = display_main_menu()

            if main_menu_choice == 0:
                self.run_insert_coin()
            elif main_menu_choice == 1:
                self.run_dispense_red_gumball()
            elif main_menu_choice == 2:
                self.run_dispense_yellow_gumball()
            elif main_menu_choice == 3:
                self.run_return_change()

        print("\nThank you for using the Gumball Machine!")