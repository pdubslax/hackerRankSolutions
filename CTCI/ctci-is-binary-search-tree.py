INT_MAX = 99999999
INT_MIN = -99999999

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_binary_search_tree_(root):
   return help(root,INT_MIN,INT_MAX)

def help(root,mini,maxi):
    if root is None:
        return True
    if root.data < mini or root.data > maxi:
        return False
    return help(root.left,mini,root.data - 1) and help(root.right,root.data + 1,maxi)



root = node(4)
root.left = node(2)
root.right = node(5)
root.left.left = node(1)
root.left.right = node(3)

print check_binary_search_tree_(root)
