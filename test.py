class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedlinkedList:
    def __init__(self):
        self.head = None

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def listLength(self):
        if self.isListEmpty():
            return 0
        else:
            currentNode = self.head
            length = 0
            while currentNode is not None:
                length += 1
                currentNode = currentNode.next
            return length

    def insertEnd(self, newNode):
        if self.isListEmpty():
            self.head = newNode
        else:
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
            currentNode.next = newNode

    def insertAt(self, position, newNode):
        if self.isListEmpty():
            self.head = newNode
        else:
            currentPosition = 0
            currentNode = self.head
            while currentPosition != position:
                currentPosition += 1
                previousNode = currentNode
                currentNode = currentNode.next
            newNode.next = currentNode
            previousNode.next = newNode

    def insertSort(self, newNode):
        if self.isListEmpty():
            self.insertEnd(newNode)
        else:
            currentNode = self.head
            currentPosition = 0
            while currentNode.data <= newNode.data:
                currentPosition += 1
                currentNode = currentNode.next
            self.insertAt(currentPosition, currentNode)
    
    def appendList(self, newList):
        for i in newList:
            self.insertEnd(i)

    def printlinkedList(self):
        if self.isListEmpty():
            print("Empty List")
            return
        else:
            currentNode = self.head
            while currentNode is not None:
                print(currentNode.data)
                currentNode = currentNode.next

firstNode = Node(15)
linkedList = LinkedlinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node(20)
linkedList.insertEnd(secondNode)
# valueList = [x for x in range(10, 100, 10)]
# nodeList = [Node(x) for x in range(10, 60, 10)]
# print(nodeList)
# linkedList.appendList(nodeList)
thirdNode = Node(17)
linkedList.insertSort(thirdNode)
print(linkedList.listLength())
print("<< ----------------------- >>")
linkedList.printlinkedList()