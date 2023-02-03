from cli import GumballMachineCLI
from gumball_machine import GumballMachine


def main():
    """The main function of the program. Runs the gumball machine event loop.
    """
    machine = GumballMachine()
    GumballMachineCLI(machine).run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
