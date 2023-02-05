# Gumball Machine

This is a simple CLI gumball machine written in Python 3.11. 

It comes complete with type annotations and docstrings. It also passes static type checking with `mypy`:

```
> python -m mypy .
Success: no issues found in 4 source files
```

## Usage

```bash
$ python main.py
```

## Example Output

```
Welcome to the Gumball Machine!

> What would you like to do? 

1. Insert coin
2. (5c ) Dispense red gumball
3. (10c) Dispense yellow gumball 
4. Exit and return change

* Enter your choice: 1

> Provide a coin by entering it's name. Accepted coin names are "nickel", "dime", and "quarter".
* penny

! Invalid coin. All invalid coins will be returned upon requesting your unused change.

> What would you like to do? 

1. Insert coin
2. (5c ) Dispense red gumball
3. (10c) Dispense yellow gumball 
4. Exit and return change

* Enter your choice: 1

> Provide a coin by entering it's name. Accepted coin names are "nickel", "dime", and "quarter".
* quarter

# Inserting coin...
# Your current balance is: $0.25

> What would you like to do? 

1. Insert coin
2. (5c ) Dispense red gumball
3. (10c) Dispense yellow gumball 
4. Exit and return change

* Enter your choice: 2

# Dispensing Red Gumball...
# Your current balance is: $0.20

> What would you like to do? 

1. Insert coin
2. (5c ) Dispense red gumball
3. (10c) Dispense yellow gumball 
4. Exit and return change

* Enter your choice: 2

# Dispensing Red Gumball...
# Your current balance is: $0.15

> What would you like to do? 

1. Insert coin
2. (5c ) Dispense red gumball
3. (10c) Dispense yellow gumball 
4. Exit and return change

* Enter your choice: 1

> Provide a coin by entering it's name. Accepted coin names are "nickel", "dime", and "quarter".
* half-dollar

! Invalid coin. All invalid coins will be returned upon requesting your unused change.

> What would you like to do? 

1. Insert coin
2. (5c ) Dispense red gumball
3. (10c) Dispense yellow gumball 
4. Exit and return change

* Enter your choice: 4

# Returning $0.15 in change.
# The following coins were not recognized:
# - penny
# - half-dollar

Thank you for using the Gumball Machine!
```