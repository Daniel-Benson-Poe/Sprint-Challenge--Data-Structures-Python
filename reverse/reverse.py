class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        current = node  # set current position to node
        prev = prev  # set prev to prev
        while current is not None:  # run loop until current position holds None value
            current_iter = current.get_next()  # set iterator to current's next node
            current.next_node = prev  # set current's next node to prev
            prev = current  # set prev to current node
            current = current_iter  # set current to iterator node
        self.head = prev  # set self.head to prev
