""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def isBinarySearchTree(root):
    return check_binary_search_tree_(root)


def check_binary_search_tree_(root):
    return check_binary_search_tree_util(root, 0, 10**4)


def check_binary_search_tree_util(root, mini, maxi):
    if root is None:
        return True
    
    if root.data < mini or root.data > maxi:
        return False
    
    return check_binary_search_tree_util(root.left, mini, root.data - 1) and\
        check_binary_search_tree_util(root.right, root.data + 1, maxi)