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
    def __init__(self, method=2):
        self.num_slot = 529
        self.cache = [None for i in range(self.num_slot)]
        self.method = method

    def insert(self, node):
        key_temp = self.hash_probe(node.key)
        self.cache[key_temp] = node

    def search(self, key):
        key_temp = self.hash_probe(key)
        res = self.cache[key_temp]
        if res:
            return res.data
        else:
            raise KeyError(key)

    def __setitem__(self, *args):
        node = HashNode(args[0], args[1])
        self.insert(node)

    def __getitem__(self, *args):
        return self.search(args[0])

    def __hash_function(self, key):
        A = (math.sqrt(5) - 1) / 2
        b = math.modf(key*A)[0]
        return int(self.num_slot*b)

    def __hash_function_as(self, key):
        return key % 97

    def __hash_probe_linear(self, key):
        res_temp = self.__hash_function(key)
        for i in range(self.num_slot):
            temp_key = (res_temp + i) % self.num_slot
            if self.__hash_probe_check(temp_key, key):
                return temp_key

    def __hash_probe_quad(self, key):
        res_temp = self.__hash_function(key)
        c1 = 17
        c2 = 19
        for i in range(self.num_slot):
            temp_key = (res_temp + c1*i + c2*i*i) % self.num_slot
            if self.__hash_probe_check(temp_key, key):
                return temp_key

    def __hash_probe_double(self, key):
        h1 = self.__hash_function(key)
        h2 = self.__hash_function_as(key)
        for i in range(self.num_slot):
            temp_key = (h1 + h2*i) % self.num_slot
            if self.__hash_probe_check(temp_key, key):
                return temp_key

    def __hash_probe_check(self, temp_index, key):
        if self.cache[temp_index] == None:
            return -1
        elif self.cache[temp_index].key == key:
            return 1
        else:
            return 0

    def hash_probe(self, key):
        if self.method == 0:
            return self.__hash_probe_linear(key)
        elif self.method == 1:
            return self.__hash_probe_quad(key)
        else:
            return self.__hash_probe_double(key)


class HashPerfect(object):
    def __init__(self):
        pass
