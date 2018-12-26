from linked_list import LinkedListSingly

class Queue(LinkedListSingly):
    def __init__(self, ceil=-1):
        super(Queue, self).__init__()
        self.ceil = ceil

    def enqueue(self, data):
        if self.ceil > 0:
            if self.length == self.ceil:
                raise MemoryError('Queue OverFlow')
        self.insert(data)

    def dequeue(self):
        if self.length == 0:
            raise MemoryError('Queue UnderFlow')
        return self.delete(0)





