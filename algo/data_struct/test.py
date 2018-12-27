from linked_list import LinkedListSingly, LinkedListDoubly
from stack import Stack
from queue import Queue
from hashmap import HashDirectAddress, HashChained, HashOpenAddress

print('LindedListSingly Test')
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
print()

print('LindedListDoubly Test')
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
print()

print('Stack Test')
st = Stack(2)
st.push(2)
st.push(5)
print(st.pop())
print(st.pop())
print()

print('Queue Test')
qu = Queue(2)
qu.enqueue(2)
qu.enqueue(5)
print(qu.dequeue())
print(qu.dequeue())
print()

print('Hash DirectAddressMap Test')
hda = HashDirectAddress()
hda[2] = 3
hda[8] = 16
print(hda[8])
hda.delete(8)
print()

print('Hash Chained Test')
hc = HashChained(2)
hc[2] = 3
hc[8] = 16
hc[12] = 8
print(hc[8])
print(hc[12])
hc.delete(2)
print()

print('Hash OpenAddress Test')
ho = HashOpenAddress(1)
ho[4] = 3
ho[381] = 16
ho[12] = 8
print(ho[4])
print(ho[381])
print(ho[12])
print()

