'''
    Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
'''
def sign(x):
    if x == 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 1
   