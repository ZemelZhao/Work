import os
import re

if __name__ == '__main__':
    a = int(input('Dir').strip())
    os.mkdir('%d' % a)
    os.system('touch %d/Solution.java' % a)
    os.system('touch %d/README.md' % a)

