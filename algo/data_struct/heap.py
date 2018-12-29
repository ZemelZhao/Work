

class NodeBinarySearchTree(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.l = None
        self.r = None

class BinarySearchTree(object):
    def __init__(self):
        self.ancestor = None

    def insert(self, node):
        if self.ancestor == None:
            self.ancestor = node
        else:
            node_temp = self.ancestor
            while True:
                if node_temp.key > node.key:
                    if node_temp.r == None:
                        node_temp.r = node
                        node.p = node_temp
                        break
                    else:
                        node_temp = node_temp.r
                elif node_temp.key < node.key:
                    if node_temp.l == None:
                        node_temp.l = node
                        node.p = node_temp
                        break
                    else:
                        node_temp = node_temp.l
                else:
                    raise KeyError(node.key)

    def search(self, key):
        node = self.ancestor
        res = None
        while True:
            if key > node.key:
                if node.r == None:
                    break
                else:
                    node = node.r
            elif key < node.key:
                if node.l == None:
                    break
                else:
                    node = node.l
            else:
                res = node
                break
        if res:
            raise KeyError(key)
        else:
            return res.data
