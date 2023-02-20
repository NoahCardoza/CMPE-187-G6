from enum import Enum

import prompts
from utils import input_numeric, input_yes_no


class Result(Enum):
    ELIGIBLE = "1"
    INELIGIBLE = "0"
    DEAN = "Dean for consideration"


# def consider_student() -> Result:
#     if 18 <= input_numeric(prompts.AGE) <= 24:
    
#         if input_yes_no(prompts.CA_RESIDENCY):
#             if input_yes_no(prompts.PART_TIME_WORK)
#             else:
#                 if input_yes_no(prompts.PARENTS_LIVED_IN_CA):
#                     else
#                 if input_yes_no(prompts.VOLUNTEER):
#                     else
#             return Result.ELIGIBLE
#         else:
#             if input_numeric(prompts.INCOME) < 5000:
#                 return Result.DEAN
#             return Result.INELIGIBLE
#     else:
#         return Result.INELIGIBLE


def consider_student() -> Result:
    if not (18 <= input_numeric(prompts.AGE) <= 24):
        return Result.INELIGIBLE
    
    if not input_yes_no(prompts.CA_RESIDENCY) and not input_yes_no(prompts.PART_TIME_WORK) and not input_yes_no(prompts.PARENTS_LIVED_IN_CA) and not input_yes_no(prompts.VOLUNTEER):

        if input_numeric(prompts.INCOME) < 5000:
            return Result.DEAN
        return Result.INELIGIBLE

    return Result.ELIGIBLE

def consider_student(age, ca_residency, part_time_work, parents_lived_in_ca, volunteer, income):
    if not (18 <= age <= 24):
        return Result.INELIGIBLE
    
    if not ca_residency and not part_time_work and not parents_lived_in_ca and not volunteer:

        if income < 5000:
            return Result.DEAN
        return Result.INELIGIBLE

    return Result.ELIGIBLE


def main():
    print(consider_student().value)


if __name__ == '__main__':
    main()
