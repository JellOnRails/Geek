def check_height(root):
	
	if root == None:
		return -1

	left_height = check_height(root.left)
	if not left_height:
		return None

	right_height = check_height(root.right)
	if not right_height:
		return None

	height_diff = abs(left_height - right_height)
	if height_diff > 1:
		return None
	else: 
		return max(left_height, right_height) + 1


def is_balanced(root):

	return check_height(root) != None