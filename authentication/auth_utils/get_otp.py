import string
import random

def create_random():
    str_num = string.hexdigits
    return ''.join(random.choice(str_num) for i in range(8))
