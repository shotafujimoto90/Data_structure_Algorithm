from __future__ import annotations


class Node(object):
    def __init__(self, data: any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):
    def __init__(self, head: Node = None):
        self.head = head

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        current_node = self.head

        if current_node is None:
            current_node = new_node
            self.head = current_node
            return
        while current_node.next:
            next_head = current_node.next
            prev_head = current_node.prev
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node
        new_node.next = None

    def insert(self, data: any) -> None:
        new_node = Node(data)
        current_node = self.head
        if current_node is None:
            current_node = new_node
            self.head = current_node
            return
        current_node.prev = new_node
        new_node.next = current_node
        self.head = new_node
        new_node.prev = None

    def remove(self, data: any) -> None:
        current_node = self.head
        if self.head is None:
            return None
        if current_node and current_node.data == data:
            current_node = None
            self.head = None
            return
        while current_node and current_node.data != data:
            current_node = current_node.next
        if current_node is None:
            return None
        elif current_node.next is None:
            prev_node = current_node.prev
            current_node = None
            prev_node.next = None
        else:
            prev_node = current_node.prev
            next_node = current_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None

    def reverse_iterative(self) -> None:
        current_node = self.head
        prev_temp_node = None
        if current_node is None:
            return
        while current_node:
            prev_temp_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_temp_node
            current_node = current_node.prev
        if prev_temp_node:
            self.head = prev_temp_node.prev

    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node):
            if current_node is None:
                return None
            prev_temp_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_temp_node
            if current_node.prev is None:
                return current_node

            return _reverse_recursive(current_node.prev)
        self.head =_reverse_recursive(self.head)


d_l = DoublyLinkedList()
d_l.remove(1)
d_l.append(1)
d_l.append(2)
d_l.append(3)
d_l.append(2)
d_l.append(5)
d_l.append(10)
d_l.insert(9)
d_l.insert(20)
d_l.print()
print("*************")
d_l.remove(2)
d_l.print()
print("*************")
d_l.reverse_iterative()
d_l.print()
print("*************")
d_l.reverse_recursive()
d_l.print()
