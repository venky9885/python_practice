# head - [1 | Next] - [2|Next] - Null
# search O(n), del,insert O(1)


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LL():
    def __init__(self):
        self.head = None

    def printll(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
 #!At Start

    def insertll(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    # At midle
    
