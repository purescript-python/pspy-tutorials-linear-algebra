def concatString(s1):
    return lambda s2: s1 + s2


def concatArray(xs):
    return lambda ys: (
            ys if not xs else
            xs if not ys else
            xs + ys
    )