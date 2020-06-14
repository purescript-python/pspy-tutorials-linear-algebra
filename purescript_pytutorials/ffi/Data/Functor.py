def arrayMap(f):
    def app(arr):
        return tuple(f(e) for e in arr)

    return app
