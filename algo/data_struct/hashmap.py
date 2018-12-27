from linked_list import LinkedListSingly
import math
import random

class LinkedListHash(LinkedListSingly):
    def __init__(self):
        super(LinkedListHash, self).__init__()

    def delete(self, data):
        if self.length == 0:
            return -1
        else:
            node = self.head_node
            for i in range(self.length):
                node = node.next
                if node.data.key == data:
                    self.length -= 1
                    node.next = node.next.next
                    return 0
        return -1

    def search(self, data):
        if self.length == 0:
            return False
        else:
            node = self.head_node
            for i in range(self.length):
                node = node.next
                if node.data.key == data:
                    return node.data.data


class HashNode(object):
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data



class HashDirectAddress(object):
    def __init__(self):
        self.table = [None for i in range(1000)]

    def insert(self, node):
        self.table[node.key] = node

    def delete(self, key):
        self.table[key] = None

    def search(self, key):
        res = self.table[key]
        if res:
            return self.table[key].data
        else:
            raise KeyError(key)

    def __setitem__(self, *args):
        node = HashNode(args[0], args[1])
        self.insert(node)

    def __getitem__(self, *args):
        return self.search(args[0])


class HashChained(object):
    def __init__(self, hash_method=2):
        self.num_slot = 23
        self.visited = False
        self.cache = [LinkedListHash() for i in range(self.num_slot)]
        self.hash_method = hash_method

    def insert(self, node):
        key_temp = self.hash_function(node.key)
        self.cache[key_temp].insert(node)

    def delete(self, key):
        key_temp = self.hash_function(key)
        res = self.cache[key_temp].delete(key)
        if res:
            raise Warning('Key Warning: %d' % key)

    def search(self, key):
        key_temp = self.hash_function(key)
        res = self.cache[key_temp].search(key)
        if res is False:
            raise KeyError(key)
        return res

    def hash_function(self, key):
        if self.hash_method == 0:
            return self.__hash_function_div(key)
        elif self.hash_method == 1:
            return self.__hash_function_times(key)
        else:
            return self.__hash_function_universal(key)

    def __hash_function_div(self, key):
        return key % self.num_slot

    def __hash_function_times(self, key):
        A = (math.sqrt(5) - 1) / 2
        b = math.modf(key*A)[0]
        return int(self.num_slot*b)

    def __hash_function_universal(self, key):
        if not self.visited:
            self.visited = True
            self.a = random.randint(1, 100)
            self.b = random.randint(1, 20)
            self.p = 97
        return ((self.a*key + self.b) % self.p) % self.num_slot

    def __setitem__(self, *args):
        node = HashNode(args[0], args[1])
        self.insert(node)

    def __getitem__(self, *args):
        return self.search(args[0])


class HashOpenAddress(object):
    def __init__(self):
        self.

