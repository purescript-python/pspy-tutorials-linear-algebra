import json
from io import StringIO
showIntImpl = showNumberImpl = str

# TODO: tentatively use this, but not sure if this would
#   cause compatibility issues.
showCharImpl = repr

showStringImpl = json.encoder.encode_basestring


def showArrayImpl(f):
    def ap(xs):
        if not xs:
            return '[]'
        io_buffer = StringIO()
        write = io_buffer.write

        xs = iter(xs)
        write('[')
        write(f(next(xs)))
        for each in xs:
            # prefer an whilespace separator
            write(', ')
            write(f(each))
        write(']')
        return io_buffer.getvalue()

    return ap


def cons(head):
    return lambda tail: (head, *tail)


def join(separator):
    return lambda xs: separator.join(xs)
