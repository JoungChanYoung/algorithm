''' #example input
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None
    def insert(self, data1, data2, data3):
        self.root = self._insert_value(self.root, data1,data2,data3)
    def _insert_value(self, node, data1, data2, data3):
        if node is None:
            node = Node(data1)
            node.left = Node(data2)
            node.right = Node(data3)
        else:
            if data1 != node.data:
                #삽입할 노드 위치 탐색(재귀)
                self._insert_value(node.left, data1, data2, data3)
                self._insert_value(node.right, data1, data2, data3)
            else:
                if data2 != '.':
                    node.left = Node(data2)
                if data3 != '.':
                    node.right = Node(data3)
        return node

    def preorder_traversal(self,node):
        print(node.data,end="")
        if node.left is not None:
            self.preorder_traversal(node.left)
        if node.right is not None:
            self.preorder_traversal(node.right)

    def inorder_traversal(self,node):
        if node.left is not None:
            self.inorder_traversal(node.left)
        print(node.data,end="")
        if node.right is not None:
            self.inorder_traversal(node.right)

    def postorder_traversal(self,node):
        if node.left is not None:
            self.postorder_traversal(node.left)
        if node.right is not None:
            self.postorder_traversal(node.right)
        print(node.data,end="")

N = int(input())
bt = BinaryTree()
#bulid tree
for x in range(N):
    str = input().split()
    bt.insert(str[0],str[1],str[2])

#print(bt.root)
bt.preorder_traversal(bt.root)
print("")
bt.inorder_traversal(bt.root)
print("")
bt.postorder_traversal(bt.root)
