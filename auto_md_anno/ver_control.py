import os

class VerControl:
    def __init__(self):
        pass

    def run(self, data):
        data = data[-(data[::-1].index('_')):]
        list_version = [int(i) for i in data.split('.')]
        return '%d.%d.%d' % (list_version[0], list_version[1], list_version[2]+1)

if __name__ == '__main__':
    ver_control = VerControl()
    a = ver_control.run('haha_wordl_0.1.2')
    print(a)
