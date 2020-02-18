class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

    def append(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    
    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
                print("Invalid position")
                return
        if position is 0:
            self.insertHead(newNode)
            return
        else:
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = newNode
                    newNode.next = currentNode
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def deleteHead(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            self.head = self.head.next

    def deleteAt(self, position):
        if position < 0 or position >= self.listLength():
            print("Invalid Position")
            return
        elif self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    def printList(self):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                currentNode = currentNode.next
        
linkedList = LinkedList()
firstNode = Node(10)
linkedList.append(firstNode)
secondNode = Node(20)
linkedList.append(secondNode)
thirdNode = Node(15)
linkedList.insertAt(thirdNode, 0)
linkedList.deleteAt(1)
linkedList.deleteHead()
linkedList.printList()