from linked_list import *

lls = LinkedListSingly()
lls.insert(1)
lls.insert(2)
lls.insert(3)
lls.insert(4, 0)
lls.insert(15, 2)
lls.show()
lls.delete()
lls.show()
print(lls.search(2))

lld = LinkedListDoubly()
lld.insert(1)
lld.insert(2)
lld.insert(3)
lld.insert(4, 0)
lld.insert(15, 2)
lld.show()
lld.delete()
lld.show()
print(lld.search(2))

