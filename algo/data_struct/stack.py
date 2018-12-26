from linked_list import LinkedListSingly

class Stack(LinkedListSingly):
    def __init__(self, ceil=-1):
        super(Stack, self).__init__()
        self.ceil = ceil

    def push(self, data):
        if self.ceil > 0:
            if self.length == self.ceil:
                raise MemoryError('Stack OverFlow')
        self.insert(data, 0)

    def pop(self):
        if self.length == 0:
            raise MemoryError('Stack UnderFlow')
        return self.delete(0)
