from Sample import *

linkedList = LinkedList()
lst = [Node(x) for x in range(5, 30, 5)]
node = Node(35)
second = Node(40)
for i in range((len(lst))):
    linkedList.insertEnd(lst[i])
linkedList.insertEnd((node))
linkedList.insertEnd(second)

# val = int(input("Enter position: "))
# print(linkedList.getN(val))
print(linkedList.listLength(), linkedList.getMiddle())
linkedList.printList()