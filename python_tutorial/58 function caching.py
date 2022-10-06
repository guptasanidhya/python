
import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")

    some_work(3)
    some_work(1)
    some_work(2)
    # some_work(2)
    """max size 3 hai agar 1st call k baad 3 call me same function aata h to wo cache lelega warna wo laod karega"""
    print("Done... Calling again")
    start = time.time()
    some_work(3)
    some_work(10)
    end = time.time()
    tt = end - start
    print(tt)
    print("Called again")
