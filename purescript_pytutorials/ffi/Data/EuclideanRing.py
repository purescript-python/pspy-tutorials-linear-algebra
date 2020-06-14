def intDegree(x):
    return min(abs(x), 2147483647)


def intDiv(x):
    return lambda y: (
        0 if y is 0 else
        x // y if y > 0 else
        x // -y
    )


def intMod(x):
    return lambda y: (
        0 if y is 0 else
        x % abs(y)
    )


def numDiv(n1):
    return lambda n2: n1 / n2
