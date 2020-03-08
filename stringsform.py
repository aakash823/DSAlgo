def stringform(one,two,three):
    third = "".join((one,two))
    if sorted(third) == sorted(three):
        return True
    return False



print(stringform('a','b','ab'))
