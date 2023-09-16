import multiprocessing
from functools import wraps


def spin_off(funct):
    """this function is a wrapper that is supposed to allow you to call a function asynchronously
    it's efficacy is in question"""
    @wraps(funct)
    def wrapper(*args, **kwargs):
        p = multiprocessing.Process(target=funct, args=args, kwargs=kwargs)
        p.start()
        return p
    return wrapper