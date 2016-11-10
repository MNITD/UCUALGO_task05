class BinarySearchTree:
    class Node:
        def __init__(self, key=None, parent=None, left=None, right=None):
            self.parent = parent
            self.key = key
            self.left = left
            self.right = right

    def build_preorder(self, parent, preorder_list, i):
        if i >= len(preorder_list) or preorder_list[i] == 0 or preorder_list is None:
            return None, i
        node = self.Node(preorder_list[i], parent, None, None)
        result = self.build_preorder(node, preorder_list, i + 1)
        node.left = result[0]
        result = self.build_preorder(node, preorder_list, result[1] + 1)
        node.right = result[0]
        return node, result[1]

    def build_inorder(self, current_node, data, i):
        if current_node.left is not None:
            i = self.build_inorder(current_node.left, data, i)
        current_node.key = data[i]
        i += 1
        if current_node.right is not None:
            i = self.build_inorder(current_node.right, data, i)
        return i

    def __init__(self, preorder_list):
        self.roott = None
        self.sum_list = []
        self.roott = self.build_preorder(None, preorder_list, 0)[0]
        preorder_list = sorted(preorder_list)
        i = 0
        for el in preorder_list:
            if el == 0:
                i += 1
        preorder_list = preorder_list[i:]
        if self.roott:
            self.build_inorder(self.roott, preorder_list, 0)

    def root(self):
        return self.roott

    def parent(self, x):
        return x.parent

    def left(self, x):
        return x.left

    def right(self, x):
        return x.right

    def key(self, x):
        return x.key

    def make_list(self, node, c):
        new_list = []
        while c > 0:
            new_list.insert(0, node)
            node = node.parent
            c -= 1
        self.sum_list.append(new_list)

    def count_sum(self, node, s, s_m=0, c=0):
        if not node:
            return
        s_m += node.key
        c += 1
        if s_m == s:
            self.make_list(node, c)
            return
        elif s_m > s:
            return
        else:
            self.count_sum(node.left, s, s_m, c)
            self.count_sum(node.right, s, s_m, c)


    def go_through_tree(self, node, s):
        if not node:
            return

        self.count_sum(node, s)
        #self.count_sum(node.left, s)
        #self.count_sum(node.right, s)

        self.go_through_tree(node.left, s)
        self.go_through_tree(node.right, s)

    def find_sum(self, s):
        self.sum_list = []
        self.go_through_tree(self.roott, s)
        return self.sum_list


bst = BinarySearchTree([3, 4, 5, 0, 0, 7, 0, 0, 6, 0, 2, 0, 0])
li = bst.find_sum(7)
for el in li:
    for el2 in el:
        print(bst.key(el2))
