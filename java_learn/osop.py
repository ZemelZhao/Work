import os
import re

if __name__ == '__main__':
    a = os.listdir('.')
    for i in a:
        num = i.index('.')
        if i[num+1:] == 'class' or i[num+1:] == 'java':
            os.remove(i)
