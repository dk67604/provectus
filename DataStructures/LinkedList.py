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
def print_linked_list(list):
    """
    Method print the Linked list
    :param head: Pointer to Linked List head
    :return:
    """
    temp=list.head
    string=[]
    if temp is None:
        print ("None")
    while (temp):

        string.append(str(temp.get_data()))
        temp=temp.next_node
    temp="-->".join(string)
    print(temp)
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
    return head

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
        return None
    else:
        if head.get_data() == key:
            return head
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

def add_node(list,node):
    temp=list.head
    while(temp):
        if temp.get_next() is None:
            temp.set_next(node)
            break
        temp=temp.get_next()
    return list

def get_tail(list):
    temp=list.head
    while(temp):
        temp=temp.get_next()
    return temp

def get_node_position(position,list):
    temp=list.head
    i=0
    if(position==0):
        return temp
    while(temp):
        i+=1
        if(i==position):
            temp=temp.get_next()
            break
        temp=temp.get_next()
    return temp


def find_intersect(first_list,second_list):
    size_first=size_recursive(first_list.head)
    size_second=size_recursive(second_list.head)
    tailfirst=get_tail(first_list)
    tailsecond=get_tail(second_list)
    if(tailfirst!=tailsecond):
        print("No intersection exist")
        return None
    if size_first>=size_second:
        print("First list get chopped")
        chop_position=size_first-size_second
        start=get_node_position(chop_position,first_list)
        temp=second_list.head
        while(temp):
            if(temp==start):
                return temp
            start=start.get_next()
            temp=temp.get_next()

    if size_first<size_second:
        print("Second List get chopped")
        chop_position=size_second-size_first
        start=get_node_position(chop_position,second_list)
        temp=first_list.head
        while(temp):
            if(temp==start):
                return temp
            start=start.get_next()
            temp=temp.get_next()


def detect_remove_loop(list):
    slow=list.head
    fast=list.head.get_next()
    while(fast is not None):
        if(fast.get_next() is  None):
            break
        if slow==fast:
            break
        slow=slow.get_next()
        fast=fast.get_next().get_next()
    if slow == fast:
        slow=list.head
        while(slow!=fast.get_next()):
            slow=slow.get_next()
            fast=fast.get_next()
        fast.set_next(None)
    return list
    




def create_input_1():
    x = Node(15)
    list = LinkedList()
    list.head = x
    list =insert_node(list,15,60)
    list =insert_node(list,60,45)

    list =insert_node(list,45,90)
    list =insert_node(list,90, 35)
    list =insert_node(list,35, 60)
    print("*********Fist List*******")
    print_linked_list(list)
    y=Node(34)
    second_list=LinkedList()
    second_list.head=y
    second_list=insert_node(second_list,34,65)
    node=search_recursive(90,list.head)
    second_list=add_node(second_list,node)
    print("********Second List*********")
    print_linked_list(second_list)
    return list,second_list

def create_input_2():
    x=Node(15)
    list=LinkedList()
    list.head=x
    list = insert_node(list, 15, 60)
    list = insert_node(list, 60, 45)
    list = insert_node(list, 45, 22)
    list = insert_node(list, 22, 90)
    list = insert_node(list, 90, 65)
    node=search_recursive(60,list.head)
    list=add_node(list,node)
    print("15-->\"60\"-->45-->90--65")
    list=detect_remove_loop(list)
    print_linked_list(list)

def create_input_3():
    x=Node('a')

    list=LinkedList()
    list.head=x
    list = add_node(list, Node('c'))
    list = add_node(list,Node('c'))
    # list = add_node(list, Node('d'))
    list = add_node(list, Node('c'))
    list = add_node(list, Node('b'))
    list = add_node(list,Node('a'))
    return list

def front_back_split(list):
    slow=list.head
    fast=list.head
    while(fast is not None and fast.get_next() is not None):
        fast=fast.get_next().get_next()
        slow=slow.get_next()
        
def move_last_element_front(list):
    start=list.head
    end=list.head
    prev=None
    while(end and end.get_next()):
        prev=end
        end=end.get_next()
    end.set_next(start)
    prev.set_next(None)
    list.head=end
    print_linked_list(list)

def reverse_alternates_k_nodes(head,k):
    current=head
    prev=None
    count=0
    next_ptr=None
    if head is None:
        return None
    while(current is not None and count < k):
        count+=1
        next_ptr=current.get_next()
        current.set_next(prev)
        prev=current
        current=next_ptr
    #print (current.data)
    if(head is not None):
        head.set_next(current)
    count=0
    while(count<k-1 and current is not None):
        count+=1
        current=current.get_next()
    #print(current.data)
    if (current is not None):
         current.set_next(reverse_alternates_k_nodes(current.get_next(),k))
    return prev



def reverse_linklist(list):
    temp = list.head
    if temp is None:
        return None

    prev=None
    while(temp):
        next=temp.get_next()
        temp.set_next(prev)
        prev=temp
        temp=next

    list.head=prev
    return list

def recursive_reverse_util(head,current,previous):
    if current.get_next() is None:
        head=current
        current.set_next(previous)
    next=current.get_next()
    current.set_next(previous)
    recursive_reverse_util(head,next,current)



def revesre_linkedlist(head):
    if head is None:
        return None
    recursive_reverse_util(head,head,None)

def find_middle(list):
    temp=list.head
    next=list.head
    prev_middle=None
    while((next is not None) and (next.get_next() is not None)):
        prev_middle=temp
        temp=temp.get_next()
        next=next.get_next().get_next()
    return temp,prev_middle

def check_palindrome(list):
    head_temp=list.head
    head=list.head
    size_list=size(list.head)
    temp=None
    print("Size:",size_list)
    middle,prev_middle=find_middle(list)

    while (head):
        if (head == prev_middle):
            prev_middle.set_next(None)
        head = head.get_next()
    if(size_list%2!=0):
        temp=middle.get_next()
    if (size_list % 2 == 0):
        temp=middle
    prev = None
    while (temp):
        next = temp.get_next()
        temp.set_next(prev)
        prev = temp
        temp = next
    middle=prev
    print("LinkedList Palindrome:",compare_list(head_temp,middle))




def compare_list(head1,head2):
    temp1=head1
    temp2=head2

    while(temp1 is not None and temp2 is not None):
        if(temp1.get_data()==temp2.get_data()):
            temp1=temp1.get_next()
            temp2=temp2.get_next()
        else:
            return False
    if (temp1 is None and temp2 is None):
        return True
    return False

###########################
# Code to test the abobe methods
###########################
if __name__ == "__main__":
     #head = Node(13)
     #list =LinkedList()
    # double_link_list=LinkedList()
    # double_link_list.head=head
     #list.head=head
    #singly_linked_list(head)
    # print("Size of Linked List:",size(head))
    # list=add_front_head(list,89)
    # print_linked_list(list.head)
    # print("Size after adding an element at head:", size(list.head))
    # insert_node(list,13,17)
    # print_linked_list(list.head)
    # print("Next insertion")
    # insert_node(list, 89, 91)
    # print_linked_list(list.head)
    # print("Size after insertion:", size(list.head))
    # data=search_kth_elemnet(7,list.head)
    # print(data)
    # left=partition(list.head,17)
    # print_linked_list(left.head)
    # list=delete_node(list,91)
    # print("Size after deletion:", size_recursive(list.head))
    # print_linked_list(list.head)
    # result=search_recursive(23,list.head)
    # if (result is None):
    #     print("Not found")
    # else:
    #     print("Data found:",result.data)
    # doubly_linked_list(head)
    # print_linked_list(double_link_list.head)
    # first_list,second_list=create_input_1()
    # temp = find_intersect(list, second_list)
    # print("Intersect element:", temp.data)
     #create_input_2()
     list=create_input_3()
     print_linked_list(list)
     # reverse_list=reverse_linklist(list)
     # print("************Reverse***********")
     # print_linked_list(reverse_list)
     # middle=find_middle(list)
     # print("Middle Element")
     # print(middle.data)
     check_palindrome(list)
     x=Node(15)
     temp_list=LinkedList()
     temp_list.head=x
     temp_list=insert_node(temp_list,15,78)
     temp_list = insert_node(temp_list, 78, 55)
     temp_list = insert_node(temp_list, 55, 65)
     temp_list = insert_node(temp_list, 65, 35)
     temp_list = insert_node(temp_list, 35, 45)
     temp_list = insert_node(temp_list, 45, 23)
     temp_list = insert_node(temp_list, 23, 67)
     temp_list = insert_node(temp_list, 67, 90)
     print_linked_list(temp_list)
     prev=reverse_alternates_k_nodes(temp_list.head,3)
     temp_list.head=prev
     print_linked_list(temp_list)


     #move_last_element_front(temp_list)
