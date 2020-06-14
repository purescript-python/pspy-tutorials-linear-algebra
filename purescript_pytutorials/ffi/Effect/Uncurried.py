from py_sexpr.stack_vm.emit import module_code
from py_sexpr.terms import *

__all__ = []
G = globals()


def make_mkEffectFn(n: int):
    myname = 'mkEffectFn{}'.format(n)
    args = ["x{}".format(i) for i in range(n)]
    fn = 'fn'
    fcall = var(fn)
    for each in args:
        fcall = call(fcall, var(each))
    fcall = call(fcall)
    meta_code = make_mkEffectFn.__code__
    ast = metadata(
        meta_code.co_firstlineno,
        1,
        meta_code.co_filename,
        define(myname, [fn], define(None, args, fcall)),
    )
    code = module_code(ast, name=__name__, filename=__file__)

    G[myname] = eval(code)
    __all__.append(myname)


# assert print(mkEffectFn1(lambda x: lambda :2 + x)(3)) == 5


def make_runEffectFn(n: int):
    myname = 'runEffectFn{}'.format(n)
    args = ["x{}".format(i) for i in range(n)]
    fn = 'fn'
    fcall = call(var(fn), *map(var, args))
    lam = define(None, [], fcall)
    for arg in reversed(args):
        lam = define(None, [var(arg)], lam)

    meta_code = make_runEffectFn.__code__
    ast = metadata(
        meta_code.co_firstlineno,
        1,
        meta_code.co_filename,
        lam,
    )
    code = module_code(ast, name=__name__, filename=__file__)

    G[myname] = eval(code)
    __all__.append(myname)


for i in range(10):
    make_mkEffectFn(i)
    make_runEffectFn(i)
