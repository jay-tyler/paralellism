# Much of this code follows verbatim after
# http://sebastianraschka.com/Articles/2014_multiprocessing_intro.html
# Please refer to Sebastian's terms of license; the MIT license might not apply to this code

import multiprocessing as mp

def cube(x):
    return x ** 3

# 1. apply() factorization
pool = mp.Pool(processes=4)
results = [pool.apply(cube, args=(x,)) for x in range(1,7)]
print(results)

# 2. map() factorization; equivalent to 1
pool = mp.Pool(processes=4)
results = pool.map(cube, range(1, 7))
print(results)