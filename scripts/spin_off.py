import multiprocessing
from functools import wraps

def spin_off(funct):
    @wraps(funct)
    def wrapper(*args, **kwargs):
        p = multiprocessing.Process(target=funct, args=args, kwargs=kwargs)
        p.start()
        return p
    return wrapper