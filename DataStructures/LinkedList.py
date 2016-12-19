class Node:
    """
    Node class
    """

    def __init__(self,data=None,next_node=None,previous_node=None ):
        """
        Initialize the property of node
        :param data: node data
        :param next_node:next node
        :param previous_node: previous node
        """
        self.data=data
        self.next_node=next_node
        self.previuos_node=previous_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self,new_node_data):
        self.data=new_node_data

    def set_next(self,new_node_next):
        self.next_node=new_node_next

    def set_previous(self, new_node_previous):
        self.previuos_node = new_node_previous

class LinkedList:
    """
    Linked List Class
    """
    def __init__(self):
        self.head = None


#########################################################
# Following methods includes LinkedList basic operation
# and the problems of CTCI(Cracking the Code Interview)
##########################################################
def print_linked_list(head):
    """
    Method print the Linked list
    :param head: Pointer to Linked List head
    :return:
    """
    temp=head
    while (temp):
        print(temp.get_data())
        temp=temp.next_node

def singly_linked_list(head):
    """
    Method to create singly linked list
    :param head: Pointer to Linked List head
    :return:
    """
    first = Node(15)
    second = Node(19)
    head.set_next(first)
    first.set_next(second)
    print_linked_list(head)

def doubly_linked_list(head):
    """
    Method to create doubly-linked list
    :param head: Pointer to Linked List head
    :return:
    """
    first=Node(29)
    second=Node(56)
    third=Node(34)
    head.set_next(first)
    first.set_previous(head)
    first.set_next(second)
    second.set_previous(first)
    second.set_next(third)
    third.set_previous(second)

def add_front_head(list,x):
    """
    Method to add an element at head position in existing List
    :param list: Linkedlist
    :param x: Element need to be added
    :return: Linked list with new element added
    """
    new_node=Node(x)
    new_node.next_node=list.head
    list.head=new_node
    return list

def insert_node(list,previous_node,new_node):
    """
    Method to add element at n'th position
    :param list: Linked List
    :param previous_node: Node after which new element needs to be added
    :param new_node: New elemnt required to add in Linked List
    :return:  Linked list with new element added
    """
    temp=list.head
    while(temp):
        if temp.get_data()==previous_node:
            x=Node(new_node)
            x.next_node=temp.get_next()
            temp.next_node=x
        temp=temp.next_node
    return list

def delete_node(list,key):
    """
    Method to remove the element from Linked List
    :param list: Linked List
    :param key: Element required to be deleted
    :return: Linked list having requested element removed
    """
    temp=list.head
    prev=temp
    if temp.get_data()==key:
        list.head=temp.next_node
        return list

    while(temp):
        if temp.get_data()==key:
            break
        prev=temp
        temp=temp.next_node
    if temp is None:
        print("The key requested for deletion is not present")
        return list
    prev.next_node=temp.next_node
    temp=None
    return list


def size(head):
    """
    Method to find the size of Linked List using iterrative version
    :param head: Pointer to Linklist head
    :return: Size of the Linked list
    """
    count=0
    temp=head
    while(temp):
        count+=1
        temp=temp.next_node
    return count

def size_recursive(head):
    """
    Method: Recursive version to find size of Linked List
    :param head: Pointer to Linklist head
    :return: Size of Linked List
    """
    if head is None:
        return 0
    else :
        return 1+ size_recursive(head.get_next())
    
def search_recursive(key,head):
    """
     Method to search an element using recursive version
    :param key: Key required to find the element in Linked List
    :param head: Pointer to Linked List head
    :return:
    """
    if head is None:
        return 'Key not found'
    else:
        if head.get_data() == key:
            return 'Key found'
        else:
          return search_recursive(key,head.get_next())


def search_kth_elemnet(position,head):
    """
    Method to find the Kth element from the last postition
    :param position: Kth element postion from the last
    :param head: Pointer to Linklist head
    :return: Value of the Kth element
    """
    temp1=head
    temp2=None
    step=0
    while(temp1):
        step+=1
        if(step<position):
         temp1=temp1.get_next()
        elif (step==position):
            temp2=head
            temp1=temp1.get_next()
        else:
            temp2=temp2.get_next()
            temp1=temp1.get_next()
    if(temp2 is None):
        return '%dth element is greater than size of linked list' % position
    return temp2.get_data()

def partition(head,key):
    """
    CTCI Problem 2.4
    :param head: Pointer to to Linked List Head
    :param key: Key where partition is required
    :return: Required Linked List with requested partition
    """
    left=LinkedList()
    left.head=None
    right=LinkedList()
    right.head=None
    temp=head
    leftptr=None
    rightptr=None
    while(temp):
        if(temp.get_data()<key):
            x=Node(temp.get_data())
            if(left.head is None):
                left.head=x
                leftptr=left.head
            else:
                leftptr.set_next(x)
                leftptr=leftptr.get_next()
        if(temp.get_data()>=key):
            y=Node(temp.get_data())
            if(right.head is None):
                right.head=y
                rightptr=right.head
            else:
                rightptr.set_next(y)
                rightptr=rightptr.get_next()
        temp=temp.get_next()
    leftptr.set_next(right.head)

    return left




###########################
# Code to test the abobe methods
###########################
if __name__ == "__main__":
    head = Node(13)
    list =LinkedList()
    double_link_list=LinkedList()
    double_link_list.head=head
    list.head=head
    singly_linked_list(head)
    print("Size of Linked List:",size(head))
    list=add_front_head(list,89)
    print_linked_list(list.head)
    print("Size after adding an element at head:", size(list.head))
    insert_node(list,13,17)
    print_linked_list(list.head)
    print("Next insertion")
    insert_node(list, 89, 91)
    print_linked_list(list.head)
    print("Size after insertion:", size(list.head))
    data=search_kth_elemnet(7,list.head)
    print(data)
    left=partition(list.head,17)
    print_linked_list(left.head)
    list=delete_node(list,91)
    print("Size after deletion:", size_recursive(list.head))
    print_linked_list(list.head)
    result=search_recursive(23,list.head)
    print(result)
    doubly_linked_list(head)
    print_linked_list(double_link_list.head)





