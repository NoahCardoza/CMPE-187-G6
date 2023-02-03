from typing import List, Literal, cast


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


def display_main_menu() -> Literal[0, 1, 2, 3]:
    """Displays the main menu and prompts the user to choose an option.

    Returns:
        int: Returns the index of the choice the user made.
    """
    return cast(
        Literal[0, 1, 2, 3],
        ask_choice(
            "What would you like to do?",
            [
                "Insert coin",
                "(5c ) Dispense red gumball",
                "(10c) Dispense yellow gumball ",
                "Exit and return change"
            ]
        )
    )

def display_coin_menu() -> Literal[0, 1, 2]:
    """Displays the coin menu and prompts the user to choose an option.

    Returns:
        int: Returns the index of the choice the user made.
    """
    return cast(
        Literal[0, 1, 2], 
        ask_choice(
            "Provide a nickel, dime, or quarter to the gumball machine:",
            [
                "Nickel",
                "Dime",
                "Quarter"
            ]
        )
    )