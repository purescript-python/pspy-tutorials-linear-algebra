unsafeCompareImpl = lambda lt: lambda eq: lambda gt: lambda x: lambda y: (
    lt if x < y else
    eq if x == y else
    gt
)

unsafeCompareImplStruct = lambda lt: lambda eq: lambda gt: lambda x: lambda y: (
    lt if x < y else
    eq if x == y else
    gt
)

ordBooleanImpl = unsafeCompareImplStruct
ordIntImpl = ordNumberImpl = ordStringImpl = ordCharImpl = unsafeCompareImpl


def ordArrayImpl(f):
    def ap1(xs):
        def ap2(ys):
            for x, y in zip(xs, ys):
                o = f(x)(y)
                if o is not 0:
                    return o
            xlen = len(xs)
            ylen = len(ys)
            if xlen == ylen:
                return 0
            if xlen > ylen:
                return -1
            return 1

        return ap2

    return ap1
