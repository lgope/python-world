class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add node
    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    # add top node
    def add_top(self, val):
        if self.head is not Node:
            node = Node(val)
            node.next = self.head
            self.head = node
            self.size += 1
        else:
            print('Node is empty run add(val) instead!')

    # add any where
    # def __add_any_where(self, node):

    # add any
    # def add_any(self, prev_node, val):
    #     new_node = Node(val)
    #
    #     node = self.head
    #     while node is not None:
    #         if node.val == prev_node:
    #             new_node.prev = node.val
    #             self.size += 1
    #             break
    #         node = node.next

    # add last node
    def add_last(self, val):
        node = Node(val)
        if self.tail is not None:
            self.tail.next = node
            self.tail = node
            self.size += 1
        else:
            print('Node is empty run add(val) instead!')

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.size -= 1

    # remove any node
    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
                # break
            node = node.next

    # remove first node
    def remove_first_node(self):
        if self.head is not None:
            self.__remove_node(self.head)

    # remove last node
    def remove_last_node(self):
        if self.tail is not None:
            self.__remove_node(self.tail)

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in values)}]"


my_list = DoubleLinkedList()

my_list.add(4)
my_list.add(5)
my_list.add(5)
my_list.add(1)
my_list.add(8)
my_list.add(8)
my_list.add(9)

print(my_list)
# my_list.remove(5)
# my_list.remove(8)
# my_list.remove_last_node()
# my_list.remove_first_node()
my_list.add_top(1)
my_list.add_top(2)
my_list.add_last(11)

print(my_list)
print(my_list.size)

# TODO: insert node any where list