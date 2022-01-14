# https://medium.com/@Kadai/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E5%A4%A7%E4%BE%BF%E7%95%B6-binary-search-tree-3c40be3204e

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None


class BST():
    def __init__(self, node=None):
        self.root = node

    def print_list(self):
        self.BST_list = []
        if self.root != None:
            self._print(self.root, self.BST_list)
        return self.BST_list

    def _print(self, node, arr):
        if node != None:
            self._print(node.left, arr)
            arr.append(node.data)
            self._print(node.right, arr)

    def get_largest_node(self, node):
        if node == self.root:
            return self.root

        while True:
            if not node.right:
                return node
            else:
                node = node.right

    def get_node_by_value(self, value):
        cur_node = self.root

        while True:
            if cur_node.data == value:
                return cur_node
            elif value < cur_node.data:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    raise Exception("Node not found")
            elif value > cur_node.data:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    raise Exception("Node not found")

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(data)
                cur_node.left.parent = cur_node
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(data)
                cur_node.right.parent = cur_node
            else:
                self._insert(data, cur_node.right)
        else:
            raise Exception("The value is existed!")

    def delete_node(self, value):
        node = self.get_node_by_value(value)
        node_parent = node.parent

        if not node.right and not node.left:
            if node_parent:
                if node_parent.left == node:
                    node_parent.left == None
                else:
                    node_parent.right == None
            else:
                self.root = None

        elif not node.left and node.right:
            if node_parent:
                if node_parent.left == node:
                    node_parent.left = node.right
                else:
                    node_parent.right = node.right
            else:
                self.root = node.right

        elif node.left:
            largst_node_left = self.get_largest_node(node.left)

            if largst_node_left == node.left:
                largst_node_left.right = node.right
                largst_node_left.parent = node.parent

                if value > node.parent.data:
                    node.parent.right = largst_node_left
                else:
                    node.parent.left = largst_node_left
                if not node_parent:
                    self.root = largst_node_left
                return

            if largst_node_left.left:
                largst_node_left.parent.right = largst_node_left.left
            else:
                largst_node_left.parent.right = None

            if node_parent:
                if node_parent.left == node:
                    node_parent.left = largst_node_left
                else:
                    node_parent.right = largst_node_left

            else:
                self.root = largst_node_left

            largst_node_left.left = node.left
            largst_node_left.right = node.right

            return


def fill_tree(tree):
    arr = [23, 5, 7, 3, 36, 11, 22, 16, 9, 37]
    for i in range(10):
        tree.insert(arr[i])

    return tree


if __name__ == '__main__':
    tree = BST()
    tree = fill_tree(tree)
    print(tree.print_list())

    tree.delete_node(5)
    print(tree.print_list())
