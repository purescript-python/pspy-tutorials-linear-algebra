import sys
from warnings import warn
from time import time as timeit
_stdout = sys.stdout
_out = sys.stdout.write
_err = sys.stderr.write
_time_st = {}
_cnt_st = {}

def log(s):
    def ap():
        _out(s)
        _out('\n')
        return ()
    return ap

def info(s):
    def ap():
        _out(s)
        _out('\n')
        return ()
    return ap

def warn(s):
    def ap():
        warn(s)
        return ()
    return ap

def error(s):
    def ap():
        _err(s)
        _err('\n')
        return ()
    return ap

def time(s):
    def ap():
        _time_st[s] = timeit()
        return ()
    return ap

def timeEnd(s):
    def ap():
        ret = _time_st.get(s, '0.0')
        print(s, ':', ret, file=_stdout)
        return ret
    return ap

timeLog = timeEnd

def clear():
    return ()
