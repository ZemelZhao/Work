#!/usr/bin/env python3

class NodeSingly(object):
    def __init__(self, data):
        self.next = None
        self.data = data

class NodeDoubly(object):
    def __init__(self, data=None):
        self.data = data
        self.next = self
        self.prev = self

class LinkedListSingly(object):
    def __init__(self):
        self.head_node = NodeSingly(None)
        self.length = 0

    def insert(self, data, loc=None):
        if loc == None:
            loc = self.length
        if loc > self.length:
            raise IndexError('list index out of range')
        else:
            self.length += 1
            node_new = NodeSingly(data)
            node = self.head_node.next
            if loc == 0:
                self.head_node.next = node_new
                node_new.next = node
            else:
                for i in range(loc-1):
                    node = node.next
                node_new.next = node.next
                node.next = node_new

    def delete(self, loc=None):
        if loc == None:
            loc = self.length - 1
        if loc > self.length or self.length == 0:
            raise IndexError('list index out of range')
        else:
            node = self.head_node.next
            temp = node.data
            self.length -= 1
            if loc == 0:
                self.head_node.next = node.next
            else:
                for i in range(loc-1):
                    node = node.next
                    temp = node.data
                node.next = node.next.next
        return temp


    def search(self, loc=None):
        if loc == None:
            loc = self.length - 1
        if loc >= self.length or self.length == 0:
            raise IndexError('list index out of range')
        else:
            node = self.head_node.next
            if loc == 0:
                return node.data
            else:
                for i in range(loc):
                    node = node.next
                return node.data

    def show(self):
        node = self.head_node.next
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

class LinkedListDoubly(object):
    def __init__(self):
        self.node_sent = NodeDoubly()
        self.length = 0

    def insert(self, data, loc=None):
        if loc == None:
            loc = self.length
        if loc > self.length:
            raise IndexError('list index out of range')
        else:
            self.length += 1
            node_new = NodeSingly(data)
            node = self.node_sent.next
            if loc == 0:
                self.node_sent.next = node_new
                node_new.next = node
                node_new.prev = self.node_sent
            else:
                for i in range(loc-1):
                    node = node.next
                node_new.next = node.next
                node_new.prev = node
                node.next = node_new

    def delete(self, loc=None):
        if loc == None:
            loc = self.length - 1
        if loc > self.length or self.length == 0:
            raise IndexError('list index out of range')
        else:
            node = self.node_sent.next
            self.length -= 1
            if loc == 0:
                self.node_sent.next = node.next
                node.next.prev = self.node_sent
            else:
                for i in range(loc-1):
                    node = node.next
                node.next = node.next.next
                node.next.prev = node

    def search(self, loc=None):
        if loc == None:
            loc = self.length - 1
        if loc >= self.length or self.length == 0:
            raise IndexError('list index out of range')
        else:
            node = self.node_sent.next
            if loc == 0:
                return node.data
            else:
                for i in range(loc):
                    node = node.next
                return node.data

    def show(self):
        node = self.node_sent.next
        while node is not self.node_sent:
            print(node.data, end=' ')
            node = node.next
        print()

