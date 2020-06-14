def arrayBind(arr):
    def kl(f):
        res = []
        ext = res.extend
        for each in arr:
            ext(f(each))
        return tuple(res)

    return kl
