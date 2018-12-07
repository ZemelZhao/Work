import numpy as np
import multiprocessing as mp
import time

class A(mp.Process):
    def __init__(self, data):
        super(A, self).__init__()
        self.data = data

    def run(self):
        while True:
            time.sleep(0.5)
            self.data[:9] = self.data[3:]
            self.data[9: ] = [3, 4, 5]

class B(mp.Process):
    def __init__(self, data):
        super(B, self).__init__()
        self.data = data

    def run(self):
        while True:
            time.sleep(0.5)
            temp = np.frombuffer(self.data.get_obj()).reshape(4, 3)
            print(temp)

if __name__ == '__main__':
    shared_arr = np.arange(12)
    shared_arr = mp.Array('d', shared_arr)
    a = A(shared_arr)
    b = B(shared_arr)
    a.start()
    b.start()
