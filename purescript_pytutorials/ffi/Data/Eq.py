def refEq(r1):
    return lambda r2: r1 is r2


def structEq(r1):
    return lambda r2: r1 == r2


eqBooleanImpl = refEq
eqIntImpl = eqNumberImpl = eqCharImpl = eqStringImpl = structEq


def eqArrayImpl(f):
    def eq_arr1(xs):
        def eq_arr2(ys):
            if len(xs) != len(ys):
                return False
            for x, y in zip(xs, ys):
                if not f(x)(y):
                    return False
            return True

        return eq_arr2

    return eq_arr1
