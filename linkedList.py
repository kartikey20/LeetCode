from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class binarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur):
        if value < cur.value:
            if cur.left == None:
                cur.left = Node(value)
            else:
                self._insert(value, cur.left)
        elif value > cur.value:
            if cur.right == None:
                cur.right = Node(value)
            else:
                self._insert(value, cur.right)
        else:
            print("Value already in tree!")

        def height(self):
            if self.root != None:
                return self._height(self, root, 0)
            else:
                return 0

        def _height(self, cur, curHeight):
            if cur == None:
                return cur
            leftHeight = self._height(cur)


def fillTree(tree, numElem=100, maxInt=1000):
    for _ in range(numElem):
        curElem = randint(0, maxInt)
        tree.insert(curElem)
    return tree


tree = binarySearchTree()
tree = fillTree(tree)
