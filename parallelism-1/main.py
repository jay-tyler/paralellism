# Much of the code follows verbatim after
# http://sebastianraschka.com/Articles/2014_multiprocessing_intro.html
# Please refer to Sebastian's terms of license; the MIT license might not apply to this code

import multiprocessing as mp
import random
import string

# Define an output queue
output = mp.Queue()

# define a example function
def rand_string(length, output):
    """Generate a random string of numbers, lower- and uppercase chars"""
    rand_str = ''.join(random.choice(
                   string.ascii_lowercase
                   + string.ascii_uppercase
                   + string.digits)
                for i in range(length))
    output.put(rand_str)

# Setup a list of processes that we want to run
processes = [mp.Process(target=rand_string, args=(5, output)) for x in range(5)]

# Running each process
for p in processes:
    p.start()

# Exiting each completed process
for p in processes:
    p.join()

#
results = [output.get() for p in processes]

print(results)