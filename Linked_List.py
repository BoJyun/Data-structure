class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SingleList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        length = 1
        current_node = self.head
        while current_node.next != None:
            length += 1
            current_node = current_node.next

        return length

    def __str__(self):
        current_node = self.head
        chain = []
        index = 1
        while current_node != None:
            chain.append("[{0}]{1}".format(index, current_node.data))
            index += 1
            current_node = current_node.next

        return "-->".join(chain)

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node.next

    def delete_all(self):
        current_node = self.head

        while current_node.next != None:
            self.tail = current_node.next
            current_node = self.tail
        self.tail.next = None

    def insert(self, index, data):

        if self.head == None:
            print("YOu can only use \"append function\" to add the data")

        if 1 > index or index > len(self):
            print("{} is not in range of the List".format(index))

        elif index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            new_node = Node(data)
            cur_inx = 1
            current_node = self.head
            while cur_inx+1 != index:
                cur_inx += 1
                current_node = self.head.next

            new_node.next = current_node.next
            current_node.next = new_node

    def delete(self, index):

        cur_indx = 1
        currnet_node = self.head
        while cur_indx+1 != index:
            current_node = current_node.next
            cur_indx += 1
        previous_node = current_node
        current_node = current_node.next

        if index == len(self):
            previous_node.next = current_node.next
        elif index == len(self):
            previous_node.next = None
            self.head = previous_node
        else:
            print("index is out of range")

    def reverse(self):

        previous_node = None
        currnet_node = self.head
        next_node = currnet_node.next
        self.tail = currnet_node

        while next_node is not None:
            currnet_node.next = previous_node
            previous_node = currnet_node
            currnet_node = next_node
            next_node = currnet_node.next

        currnet_node.next = None
        self.head = currnet_node

########################################


class Node2():
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prve = prev


class DoublyList():
    def __init__(self):
        self.head = None

    def __str__(self):
        chain = []
        while self.head != None:
            chain.append(self.head.data)
            self.head = self.head.next

        return "->".join(chain)

    def push(self, data):  # front
        new_Node = Node2(data)

        if self.head == None:
            self.head = new_Node
        else:
            new_Node.next = self.head
            self.head.prev = new_Node
            self.head = new_Node

    def append(self, data):  # end
        new_Node = Node2(data)

        if self.head == None:
            self.head = new_Node
            return

        while self.head.next != None:
            self.head = self.head.next

        new_Node.prev = self.head
        self.head.next = new_Node

    def insert(self, prev_node, data):
        new_node = Node2(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    def delete(self, delete_node):

        if self.head == delete_node:
            self.head = delete_node.next
            return

        if delete_node.prev != None:
            delete_node.prev.next = delete_node.next

        if delete_node.next != None:
            delete_node.next.prev = delete_node.prev

        del delete_node

    def reverse(self):
        return
