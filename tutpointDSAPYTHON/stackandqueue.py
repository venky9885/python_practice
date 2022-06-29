

#! Stack push
import collections


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use peek to look at the top of the stack

    def peek(self):
        return self.stack[-1]


AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())


#!pop

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

# Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()


AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
print(AStack.remove())


#! Queue Insert
class Queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self, dataval):
        # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False

    def size(self):
        return len(self.queue)


TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size())


#!Queue Delete

class Queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self, dataval):
        # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False
# Pop method to remove element

    def removefromq(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")


TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.removefromq())
print(TheQueue.removefromq())


#!Hashmap is dictionary
#!Heaps from heap
#! Deque from collections

DoubleEnded = collections.deque(["Mon", "Tue", "Wed"])
DoubleEnded.append("Thu")

print("Appended at right - ")
print(DoubleEnded)

DoubleEnded.appendleft("Sun")
print("Appended at right at left is - ")
print(DoubleEnded)

DoubleEnded.pop()
print("Deleting from right - ")
print(DoubleEnded)

DoubleEnded.popleft()
print("Deleting from left - ")
print(DoubleEnded)
