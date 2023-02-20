#   1: def consider_student() -> Result:
#   2:     if not (18 <= input_numeric(prompts.AGE) <= 24):
#   3:         return Result.INELIGIBLE
#   4:     
#   5:     if not input_yes_no(prompts.CA_RESIDENCY)\
#   6:        and not input_yes_no(prompts.PART_TIME_WORK)\
#   7:        and not input_yes_no(prompts.PARENTS_LIVED_IN_CA)\
#   8:        and not input_yes_no(prompts.VOLUNTEER):
#   9:
#  10:        if input_numeric(prompts.INCOME) < 5000:
#  11:            return Result.DEAN
#  12:        return Result.INELIGIBLE
#  13:
#  14:     return Result.ELIGIBLE