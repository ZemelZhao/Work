import numpy as np
import multiprocessing as mp
import os
import hashlib


a = ''
b = hashlib.sha1(a.encode('utf8'))
print(b.hexdigest())

