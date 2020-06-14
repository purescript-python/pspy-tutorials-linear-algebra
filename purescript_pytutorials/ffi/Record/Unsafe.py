def unsafeHas(label):
    return lambda rec: label in rec


def unsafeGet(label):
    return lambda rec: rec[label]


def unsafeSet(label):
    return lambda val: lambda rec: {**rec, label: val}


def unsafeDelete(label):
    def ap(rec):
        copy = rec.copy()
        del copy[label]
        return copy

    return ap
