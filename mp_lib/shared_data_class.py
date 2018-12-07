import multiprocessing as mp
import time

class SharedData(object):
    shared_data = 0

class A(mp.Process):
    def __init__(self, data):
        super(A, self).__init__()
        self.data = data

    def run(self):
        while True:
            time.sleep(0.5)
            print('b_address', self.data)
            print('a_data', id(self.data.shared_data))
            print('a_class', id(self.data))
            self.data.shared_data += 1

class B(mp.Process):
    def __init__(self, data):
        super(B, self).__init__()
        self.data = data

    def run(self):
        while True:
            time.sleep(0.5)
            print('b_address', self.data)
            print('b_data', id(self.data.shared_data))
            print('b_class', id(self.data))
            print(self.data.shared_data)

if __name__ == '__main__':
    data = SharedData()
    a = A(data)
    b = B(data)

    a.start()
    b.start()


