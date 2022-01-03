
class Node(object):
    def __init__(self, data=0, Node_next=None):
        self.data = data
        self.next = Node_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        new_node = Node(data)
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        previous_node.next = current_node.next
        current_node = None

    def reverse_iterative(self)->None:
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def reverse_recursive(self)->None:
        def _reverse_recursive(current_node, previous_node)->Node:
            if not current_node:
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)




l = LinkedList()
l.append(5)
l.append(7)
l.append(9)
l.print()
print("**************")
l.insert(10)
l.print()
print("**************")
l.append(16)
l.remove(9)
l.print()
print("**************")
print("**************")
l.reverse_iterative()
l.print()
print("**************")
print("**************")
print("**************")
l.reverse_recursive()
l.print()



