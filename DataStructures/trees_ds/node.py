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

