def boolConj(b1):
    return lambda b2: b1 and b2


def boolDisj(b1):
    return lambda b2: b1 or b2


def boolNot(b):
    return not b
