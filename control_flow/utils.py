def input_numeric(prompt):
    while True:
        try:
            value = int(input(prompt + ': '))
        except ValueError:
            print("Invalid input, please try again")
        else:
            break
    return value


def input_yes_no(prompt) -> bool:
    while True:
        value = input(prompt + ' (y/n): ')
        if value not in ("y", "n"):
            print("Invalid input, please try again")
        else:
            return value == "y"