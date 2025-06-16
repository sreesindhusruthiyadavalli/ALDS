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
def breadth_first_search_iter(root):
	if root is None:
		return []

	values = []
	queue = [ root ]
	while queue:
		current = queue[0]
		del queue[0]
		values.append(current.val)
		if current.left is not None:
			queue.append(current.left) 
		if current.right is not None:
			queue.append(current.right)
		for x in queue:
			print(x.val)

	return values


# Recursive approach
def breadth_first_search_recur(root):
	if root is None:
		return []
	res = [ root. val]
	print(res)	
	left_values = res + breadth_first_search_recur(root.left)
	right_values = res + breadth_first_search_recur(root.right)	
	# return res + left_values + right_values
	return res 

print(breadth_first_search_recur(a))






