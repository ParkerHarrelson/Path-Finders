class TreeNode:
    
    def __init__(self, value, parent):
        self.children_nodes = []
        self.value = value
        self.parent = parent

    def add_child(self, child_node):
        self.children_nodes.append(child_node)

    
