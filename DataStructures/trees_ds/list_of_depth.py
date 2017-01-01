from trees_ds import node
from trees_ds import linked_list
from trees_ds import tree_node,tree_util

def create_tree():
    root = tree_node.TreeNode(13)
    root.left = tree_node.TreeNode(17)
    root.right = tree_node.TreeNode(19)
    root.right.left = tree_node.TreeNode(78)
    root.right.right = tree_node.TreeNode(25)
    root.left.left = tree_node.TreeNode(56)
    root.left.right = tree_node.TreeNode(23)
    root.left.left.left = tree_node.TreeNode(34)
    root.right.left.right = tree_node.TreeNode(89)
    return root

def create_list_of_depth(root):
    list_of_depth=[]
    return depth_of_list(root,list_of_depth,0)


def depth_of_list(root,list_of_depth,level):
    node=None
    if root is None:
        return
    if len(list_of_depth)==level:
        node=node.Node(data=root.data)
        list_of_depth.append(node)
    else:
        node=list_of_depth[level]

    if root.left is not None:
        depth_of_list(root.left,list_of_depth,level+1)

    if root.right is not None:
        depth_of_list(root.right,list_of_depth,level+1)
    node=tree_util.add_node(node, node.Node(root.data))
    return list_of_depth




if __name__ == '__main__':
  treeroot=create_tree()
  tree_util.print_inorder(treeroot)
  print("")
  tree_util.print_preoder(treeroot)
  list_ofdepth=create_list_of_depth(treeroot)
  print("")
  for i in range(0,len(list_ofdepth)):
      node=list_ofdepth[i]
      temp=node
      print("Level%d" %i)
      while temp.next_node is not None:
          print(temp.get_next().data,end=" ")
          temp=temp.next_node
      print("")

