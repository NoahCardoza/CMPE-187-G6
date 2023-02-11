"""
A student is eligible for scholarships if he satisfies the below conditions:

A. Student is between the  age 18 and 24 (boundary value included)

B. Student has lived in California for last 2 years, if he fails this criterion, check if satisfies D.

C. Has worked part time for at least for 6 months in the relevant field of study, if he fails this criterion, check if satisfies E.

D. Parents of the student have paid California state tax for at least 1 year in their lifetime.

E. Has volunteered for a cause and has a valid proof of it.

F. Has household income less than 5000$ per annum then one need not satisfy criteria C, he will be redirected to "Dean for consideration"

--------------------------------------------------------------------------

Here are the conditions for a student's scholarship eligibility again:

1. Age: The student MUST be between 18 and 24 years of age

2. CA Residency (one of these conditions MUST be met):

a. The student has lived in California for the last two years 

    b. The student has worked in California (part time or full time) at least for six months

    c. The student's parents have lived in California for at least one year

    d. The student has volunteered for a public cause in California and show proof of it 

3. Dean's Consideration

    a. If the student doesn't meet the residency requirement but has household income of less than $5000, the application may be granted eligibility by the Dean.
"""

def input_numeric(prompt):
    while True:
        try:
            value = int(input(prompt))
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

def should_be_sent_to_dean():
    income = input_numeric("Enter your household income: ")
    if income < 5000:
        return True
    return False

def main():
    age = input_numeric("Enter your age: ")
    if age < 18 or age > 24:
        print("0")
        return
    
    if should_be_sent_to_dean():
        print("Dean for consideration")
        return
    
    ca_residency = input_yes_no("Have you lived in California for the last two years?")
    if not ca_residency:
        parents_have_paid_tax = input_yes_no("Have your parents paid California state tax for at least one year in their lifetime?")
        if not parents_have_paid_tax:
            print("0")
            return

    part_time_work = input_yes_no("Have you worked part time for at least for 6 months in the relevant field of study?")
    if not part_time_work:
        volunteer = input_yes_no("Have you volunteered for a cause and have a valid proof of it?")
        if not volunteer:
            print("0")
            return
    
    print("1")

if __name__ == '__main__':
    main()
