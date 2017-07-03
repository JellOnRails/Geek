class Node:
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None


class Tree:
	def __init__(self):
		self.root = None


def get_height(root):
	
	if root == None:
		return -1

	return max(get_height(root.left), get_height(root.right)) + 1
	

def is_balanced(root):

	if root == None:
		return True

	height_diff = get_height(root.left) - get_height(root.right)
		
	if abs(height_diff) > 1:
		return False
	else:
		return is_balanced(root.left) && is_balanced(root.right)
