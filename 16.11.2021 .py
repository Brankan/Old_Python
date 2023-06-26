

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            # The item is the 1st item
            self.head = current.getNext()
        else:
            if current.getNext() is None:
                self.tail = previous  # in case the current tail is removed
            previous.setNext(current.getNext())
        self.length -= 1

    def append(self, item):
        temp = Node(item)
        last = self.tail
        if last:
            last.setNext(temp)
        else:
            self.head = temp
        self.tail = temp
        self.length += 1

    def insert(self, index, item):
        temp = Node(item)
        current = self.head
        previous = None
        count = 0
        found = False
        if index > self.length-1:
            raise IndexError('List Index Out Of Range')
        while current is not None and not found:
            if count == index:
                found = True
            else:
                previous = current
                current = current.getNext()
                count += 1
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        self.length += 1

    def index(self, item):
        pos = 0
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                pos += 1
        if not found:
            raise ValueError('Value not present in the List')
        print(pos)
        return pos

    def pop(self, index=None):
        if index is None:
            index = self.length-1
        if index > self.length-1:
            raise IndexError('List Index Out Of Range')
        current = self.head
        previous = None
        found = False
        if current:
            count = 0
            while current.getNext() is not None and not found:
                if count == index:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
                    count += 1
            if previous is None:
                self.head = current.getNext()
                if current.getNext() is None:
                    self.tail = current.getNext()
            else:
                self.tail = previous
                previous.setNext(current.getNext())
        self.length -= 1
        return current.getData()
    def printList(self):
        node= self.head
        while node is not None:
            print(node.data)
            node = node.next


    def getIndex(self,item):
        cur_idx=0
        cur_node=self.head
        while cur_node.next:
            cur_node=cur_node.next
            if cur_node.data==item: return cur_idx
            cur_idx+=1
        return None      

list = UnorderedList()
list.append(0)
list.append(10)
list.pop(0)
print("_")
list.printList( )

