from typing import Literal


class GumballMachine:
    """Mimics the state of a a gumball machine."""
    def __init__(self):
        """Initializes the gumball machine."""
        self.money = 0
    
    def get_money(self) -> int:
        """Returns the amount of money in the machine.

        Returns:
            int: The amount of money in the machine in cents.
        """
        return self.money

    def insert_coin(self, value: Literal[5, 10, 25]):
        """Inserts a coin into the machine.

        Args:
            value (int): The value of the coin in cents.
        """

        if value not in [5, 10, 25]:
            raise ValueError("Invalid coin value.")
        
        self.money += value

    def dispense_red_gumball(self) -> bool:
        """Dispenses a red gumball if there is enough money.

        Returns:
            bool: If the gumball was dispensed.
        """
        if self.money >= 5:
            self.money -= 5
            return True
        return False

    def dispense_yellow_gumball(self) -> bool:
        """Dispenses a yellow gumball if there is enough money.

        Returns:
             bool: If the gumball was dispensed.
        """
        if self.money >= 10:
            self.money -= 10
            return True
        return False

    def return_change(self) -> int:
        """Resets the machine's money to 0 and returns the change.

        Returns:
            int: The change in cents.
        """
        change = self.money
        self.money = 0
        return change

