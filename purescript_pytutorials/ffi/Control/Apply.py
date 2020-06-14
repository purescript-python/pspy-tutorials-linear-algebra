def arrayApply(fs):
    def ap(xs):
        return tuple(f(x) for f in fs for x in xs)

    return ap
