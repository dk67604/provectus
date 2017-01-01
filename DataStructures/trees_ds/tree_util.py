def size_tree(node):
    if node is None:
          return 0
    else:
        return size_tree(node.left)+1+size_tree(node.right)
def print_inorder(root):

    if root:
       print_inorder(root.left)
       print(root.data,end=" ")
       print_inorder(root.right)



def print_preoder(root):
    if root:
        print(root.data,end=" ")
        print_preoder(root.left)
        print_preoder(root.right)


def add_node(head,node):
    temp=head
    while(temp):
        if temp.get_next() is None:
            temp.set_next(node)
            break
        temp=temp.get_next()
    return head
