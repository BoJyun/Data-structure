# 迷宮
import datetime


def game_maze():
    maze = [[0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]]

    next = [[0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]]

    class note():
        def __init__(self, n, m):
            self.x = [0]*n*m
            self.y = [0]*n*m
            self.f = [0]*n*m
            self.s = [0]*n*m

    n = len(maze)
    m = len(maze[0])

    book = []
    for i in range(n):
        book.append([0]*m)

    start_x = 0
    start_y = 0
    end_x = 3
    end_y = 2

    head = 0
    tail = 0

    que = note(n, m)
    que.x[tail] = start_x
    que.y[tail] = start_y
    que.f[tail] = 0
    que.s[tail] = 0
    flag = 0

    tail += 1
    book[start_x][start_y] = 1

    while head < tail:
        for i in range(4):
            # print(que.x[head], que.y[head])
            tx = que.x[head]+next[i][0]
            ty = que.y[head]+next[i][1]

            if tx >= n or tx < 0 or ty >= m or ty < 0:
                continue

            if book[tx][ty] == 0 and maze[tx][ty] == 0:
                book[tx][ty] = 1
                que.x[tail] = tx
                que.y[tail] = ty
                que.f[tail] = head
                que.s[tail] = que.s[head]+1
                tail += 1

            if tx == end_x and ty == end_y:
                flag = 1
                break
        if flag == 1:
            break
        head += 1

    print(que.s[tail-1])
    print(que.x)
    print(que.y)


# Breadth First Search with Binery Tree and Quene


class Quene():
    def __init__(self):
        self.arr = []

    def pop(self):
        return self.arr.pop(0)

    def add(self, n):
        self.arr.append(n)

    def remove(self, n):
        self.arr.remove(n)

    def is_not_Empty(self):
        if len(self.arr) != 0:
            return True


class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Binery_tree():
    def __init__(self, node=None):
        self.node = node
        # self.head=self.node #first data node
        self.quene = Quene()

    def print_list(self):
        self.BST_list = []
        if self.node != None:
            self._print(self.node, self.BST_list)
        return self.BST_list

    def _print(self, node, arr):
        if node != None:
            self._print(node.left, arr)
            arr.append(node.data)
            self._print(node.right, arr)

    def insert(self, data):
        if self.node == None:
            self.node = Node(data)
        else:
            self._insert(self.node, data)

    def _insert(self, cur_node, data):
        if cur_node.data < data:
            if cur_node.right != None:
                cur_node = cur_node.right
                self._insert(cur_node, data)
            else:
                node = Node(data)
                cur_node.right = node
        elif cur_node.data > data:
            if cur_node.left != None:
                cur_node = cur_node.left
                self._insert(cur_node, data)
            else:
                node = Node(data)
                cur_node.left = node
        else:
            raise Exception("The value is existed!")

    def get_node_by_data(self, data):
        cur_node = self.node

        while cur_node:
            if cur_node.data > data and cur_node.left != None:
                cur_node = cur_node.left
            elif cur_node.data < data and cur_node.right != None:
                cur_node = cur_node.right
            elif cur_node.data == data:
                return cur_node
            else:
                raise Exception("Node not found")
        return

    def get_node_by_data_BFS(self, data):
        cur_node = self.node

        if cur_node.left == None and cur_node.right == None:
            return cur_node

        while cur_node:
            if cur_node.data == data:
                return cur_node
            else:
                if cur_node.left:
                    self.quene.add(cur_node.left)

                if cur_node.right:
                    self.quene.add(cur_node.right)

            if self.quene.is_not_Empty:
                cur_node = self.quene.pop()

    def get_largest_node_by_node(self, node):
        if self.node == node:
            return node

        while True:
            if node.right != None:
                return node
            else:
                node = node.right

    def delete_node_data(self, data):
        node = self.get_node_by_data(data)
        node_parent = node.parent

        if node.left == None and node.right == None:
            if node_parent:
                if node.data > node_parent.data:
                    node_parent.right == None
                else:
                    node_parent.left == None
            else:
                self.node = None
        elif node.left == None and node.right != None:
            if node_parent:
                if node.data > node_parent.data:
                    node_parent.right = node.right
                else:
                    node_parent.left = node.right
            else:
                self.node = node.right
        elif node.left:
            largest_node = self.get_largest_node_by_node(data.left)

            if largest_node == node.left:
                largest_node.right = node.right
                largest_node.parent = node.parent

                if node_parent == None:
                    self.node = largest_node
                else:
                    if data > node_parent.data:
                        node_parent.right = largest_node
                    else:
                        node_parent.left = largest_node
                return

            if largest_node.left:
                largest_node.parent.right = largest_node.left
            else:
                largest_node.parent.right = None

            if node_parent:
                if node_parent.left == node:
                    node_parent.left = largest_node
                else:
                    node_parent.right = largest_node
            else:
                self.node = largest_node

            largest_node.left = node.left
            largest_node.right = node.right

            return


def fill_tree(tree):
    arr = [23, 5, 7, 3, 36, 11, 22, 16, 9, 37]
    for i in range(10):
        tree.insert(arr[i])

    return tree


tree = Binery_tree()
tree = fill_tree(tree)
print(tree.print_list())
print(datetime.datetime.now())
print(tree.get_node_by_data(22).data)
print(datetime.datetime.now())
print(tree.get_node_by_data_BFS(22).data)
print(datetime.datetime.now())
