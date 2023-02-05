from enum import IntEnum
from typing import List


class MenuChoice(IntEnum):
    """Represents a menu choice."""
    INSERT_COIN = 0
    DISPENSE_RED_GUMBALL = 1
    DISPENSE_YELLOW_GUMBALL = 2
    RETURN_CHANGE = 3


def ask_choice(prompt: str, choices: List[str]) -> int:
    """Prompts the user to choose from a list of choices.

    Args:
        prompt (str): The prompt to display to the user.
        choices (List[str]): The list of choices to display to the user.

    Returns:
        int: The index (starting from 0) of the choice the user made.
    """

    print('\n>', prompt, '\n')
    for i, option in enumerate(choices):
        print(f"{i + 1}. {option}")

    raw_choice: str = input("\n* Enter your choice: ")

    try:
        choice: int = int(raw_choice)
    except ValueError:
        print("Invalid input. Must be an integer.\n")
        return ask_choice(prompt, choices)

    if choice < 1 or choice > len(choices):
        print("Invalid input. The number must be between 1 and {}.\n".format(len(choices)))
        return ask_choice(prompt, choices)

    return choice - 1


def display_main_menu() -> MenuChoice:
    """Displays the main menu and prompts the user to choose an option.

    Returns:
        MenuChoice: Returns the choice the user made.
    """
    choice = ask_choice(
        "What would you like to do?",
        [
            "Insert coin",
            "(5c ) Dispense red gumball",
            "(10c) Dispense yellow gumball ",
            "Exit and return change"
        ]
    )

    return MenuChoice(choice)
