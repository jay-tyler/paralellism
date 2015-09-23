# Much of the code follows after http://sebastianraschka.com/Articles/2014_multiprocessing_intro.html
# Please refer to Sebastian's terms of license; the MIT license might not apply to this code

import multiprocessing as mp
import random
import string

# Define an output queue