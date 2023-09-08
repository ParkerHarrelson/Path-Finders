from Nodes import TreeNode
from collections import deque
import random

class TreeBuilder:

    def __init__(self, depth):
        self.depth = depth


    def random_children(self, min=1, max=10):
        return random.randint(min, max)

    
    def build_tree(self):
        root = TreeNode(1, None)
        queue = deque([(root, 1)])
        current_value = 2

        while queue:
            node, node_depth = queue.popleft()

            if node_depth < self.depth:
                num_children = self.random_children() 
                for _ in range(num_children):
                    child = TreeNode(current_value, node)
                    node.add_child(child)
                    queue.append((child, node_depth + 1))
                    current_value += 1
                    
        return [root, current_value - 1]
