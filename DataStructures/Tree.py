from queue_ds import Queue
import linked_list as ld
import math
class TreeNode:

    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def size(node):
    if node is None:
          return 0
    else:
        return size(node.left)+1+size(node.right)
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



def insert_leftmost(root,left):
    if root is None:
        return None
    if root.left is None:
        root.left=left
        return root
    temp = root.left
    prev=None
    while(temp is not None):
        prev=temp
        temp=temp.left
    if  prev.left is None:
        prev.left= left
    return root


def insert_rightmost(root,right):
    if root is None:
        return None
    if root.right is None:
        root.right=right
        return root
    temp = root.right
    prev=None
    while(temp is not None):
        prev=temp
        temp=temp.left
    if  prev.right is None:
        prev.right= right
    return root

def add_to_queue(root,queue):
    queue.enqueue(root)
    queue_temp=Queue()

    queue_temp.enqueue(root)
    while(queue.size()>0):
        temp = queue.dequeue()

        if temp.left is not None:
            queue_temp.enqueue(temp.left)
            queue.enqueue(temp.left)
        if temp.right is not None:
            queue_temp.enqueue(temp.right)
            queue.enqueue(temp.right)

    return queue_temp

def minimal(input_array):
    return minimal_tree_bst(input_array,0,len(input_array)-1)

def minimal_tree_bst(input_array,low,high):
    temp1=low
    temp2=high
    if(temp2<temp1):
        return None
    middle=int(math.ceil((temp1+temp2)/2))
    root=TreeNode(input_array[middle])
    root.left=minimal_tree_bst(input_array,temp1,middle-1)

    root.right=minimal_tree_bst(input_array,middle+1,temp2)
    return root

def mirror_tree(root):
  if root is None:
      return root
  if root is not None:
      left=mirror_tree(root.left)
      right=mirror_tree(root.right)
      root.left=right
      root.right=left
      return root

def delete_tree(root):
    if root is None:
        return
    delete_tree(root.left)
    delete_tree(root.right)
    root=None



def root_to_leaf(root,path,pathlen):
    if root is None:
        return
    if root is not None:
        path.insert(pathlen,root.data)
        pathlen+=1
    if root.left is None and root.right is None:
        print("\n",path)
    else:
        root_to_leaf(root.left,path,pathlen)
        root_to_leaf(root.right,path,pathlen)

    path.pop()
def insert_right(root,queue,node):
    temp=queue
    current=temp.dequeue()
    if current.right is None:
        current.right=node
        return root
    return insert_right(current,temp,node)




if __name__ == '__main__':
    root=TreeNode(13)
    root.left=TreeNode(17)
    root.right=TreeNode(19)
    root.right.left=TreeNode(78)
    root.left.left=TreeNode(56)
    root.left.right=TreeNode(23)
    value=size(root)
    print(value)
    print_inorder(root)
    left=TreeNode(45)
    right=TreeNode(67)
    insert_leftmost(root,left)
    print("Left node added")
    print_inorder(root)
    insert_rightmost(root,right)
    print("Right node added")
    print("=============Inorder=============")
    print_inorder(root)
    print("\n=========Preorder============")
    print_preoder(root)
    queue=Queue()

    queue_1=add_to_queue(root,queue)
    print("\nSize:",queue_1.size())
    while queue_1.size()>0:
        print(queue_1.dequeue().data)

    arr=[1,2,3,4,5,6,7,8,9,10]
    bst=minimal(arr)
    # print("\nBinary Tree Inorder: ")
    # print_inorder(bst)
    # print("\nBinary Tree Preorder: ")
    # print_preoder(bst)
    # reverse_bst=mirror_tree(bst)
    # print("\nReverse Binary Tree Inorder: ")
    # print_inorder(reverse_bst)
    # print("\nReverse Binary Tree Preorder: ")
    # print_preoder(reverse_bst)



    #print("\nSize:",size(delete_tree(reverse_bst)))
    # node=TreeNode(34)
    # root_new=insert_right(root,queue,node)
    # print("=============Inorder=============")
    # print_inorder(root)
    # print("\n=========Preorder============")
    # print_preoder(root)

