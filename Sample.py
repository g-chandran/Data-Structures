class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.failureValue = -1
    # linked list essentials
    def isListEmpty(self):
        if self.head is None:
            return True
        return False

    def listLength(self):
        length = 0
        currentNode = self.head
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def printList(self):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                currentNode = currentNode.next
    
    def isSorted(self):
        if self.isListEmpty():
            return False
        else:
            currentNode = self.head
            while True:
                nextNode = currentNode.next
                if currentNode.data > nextNode.data:
                    return False
                if nextNode.next is None:
                    break
                currentNode = currentNode.next
            return True

    # insert node
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
            currentNode.next = newNode
    
    def insertHead(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            temporaryNode = self.head
            self.head = newNode
            self.head.next = temporaryNode
            del temporaryNode

    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return
        elif position == 0:
            self.insertHead(newNode)
        else:
            currentPosition = 0
            currentNode = self.head
            while currentPosition is not position:
                currentPosition += 1
                previousNode = currentNode
                currentNode = currentNode.next
            newNode.next = currentNode
            previousNode.next = newNode

    def insertSort(self, newNode):
        if self.isListEmpty():
            self.insertEnd(newNode)
        else:
            currentPosition = 0
            currentNode = self.head
            while True:
                if currentNode.data >= newNode.data:
                    self.insertAt(newNode, currentPosition)
                    break
                elif currentNode.next is None:
                    self.insertEnd(newNode)
                    break
                currentPosition += 1
                currentNode =  currentNode.next

    def appendArray(self, newList):
        for i in newList:
            self.insertEnd(i)   
    # linked list deletion
    def deleteEnd(self):
        currentNode = self.head
        previousNode = currentNode
        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next
        if previousNode.next is None:
            self.head = None
        else:
            previousNode.next = None
            del currentNode

    def deleteHead(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            firstNode = self.head
            self.head = firstNode.next

    def deleteAt(self, position):
        if position < 0 or position >= self.listLength():
            print("Invalid Position")
        elif position == self.listLength() - 1:
            self.deleteEnd()
        elif position == 0:
            self.deleteHead()
        else:
            currentPosition = 0
            currentNode = self.head
            while currentPosition != position:
                currentPosition += 1
                previousNode = currentNode
                currentNode = currentNode.next
            previousNode.next = currentNode.next
            del currentNode
    # additional processing
    def listSum(self):
        if self.isListEmpty():
            return 0
        else:
            length = 0
            currentNode = self.head
            while currentNode is not None:
                length += currentNode.data
                currentNode = currentNode.next
            return length
    
    def listMax(self):
        if self.isListEmpty():
            return self.failureValue
        else:
            currentNode = self.head
            maximum = currentNode.data
            while currentNode is not None:
                if maximum < currentNode.data:
                    maximum = currentNode.data
                currentNode = currentNode.next
            return maximum

    def listSearch(self, value):
        if self.isListEmpty():
            return self.failureValue
        else:
            currentNode = self.head
            temporaryValue = currentNode.data
            position = 0
            while currentNode is not None:
                if currentNode.data == value:
                    return position
                currentNode = currentNode.next
                position += 1
            return self.failureValue

    def listDistinct(self):
        if self.isListEmpty():
            return self.failureValue
        else:
            currentNode = self.head
            while True:
                if 

firstNode = Node(10)
link = LinkedList()
link.insertEnd(firstNode)
secondNode = Node(20)
link.insertEnd(secondNode)
thirdNode = Node(5)
link.insertHead(thirdNode)
fourthNode = Node(15)
link.insertAt(fourthNode, 2)
newList = [Node(i) for i in range(30, 45, 5)]
link.appendArray(newList)
# print(link.listSum())
# print(link.listMax())
link.printList()
# print(link.listSearch(40))
print(link.isSorted())