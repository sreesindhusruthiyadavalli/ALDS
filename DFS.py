class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f



# Iterative approach
def depth_first_search_iter(root):
	if root is None:
		return []

	values = []
	stack = [ root ]
	# if node:
	#		lst.append(node)
	while stack:
		current = stack.pop()
		values.append(current.val)
		if current.right is not None:
			stack.append(current.right) 
		if current.left is not None:
			stack.append(current.left)

	return values


# Recursive approach
def depth_first_search_recur(root):
	if root is None:
		return []
	left_values = depth_first_search_recur(root.left)
	right_values = depth_first_search_recur(root.right)	
	return [ root.val, *left_values, *right_values]	

print(depth_first_search_recur(a))





