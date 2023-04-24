import multiprocessing

def spin_off(funct):
    p = multiprocessing.Process(target=funct)
    p.start()
    # p.join()
    return p
