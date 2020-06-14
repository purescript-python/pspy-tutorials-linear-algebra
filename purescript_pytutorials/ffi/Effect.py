import itertools


def pureE(a):
    return lambda: a


def bindE(a):
    return lambda f: lambda: f(a())()


def untilE(f):
    def ap():
        while not f():
            pass
        return ()

    return ap


def whileE(f):
    def ap_a(a):
        def ap():
            while f():
                a()
            return ()

        return ap

    return ap_a


def forE(lo):
    def ap_hi(hi):
        def ap_f(f):
            def ap():
                for i in range(lo, hi):
                    f(i)()

            return ap

        return ap_f

    return ap_hi


def foreachE(as_):
    def ap_f(f):
        def ap():
            for a in as_:
                f(a)()

        return ap

    return ap_f
