from Nodes import TreeNode
from Problem_Builder import TreeBuilder
from collections import deque

def get_node_input(parent):
    value = int(input("\nEnter value for new node: "))
    return TreeNode(value, parent)

def get_children_input(root_node):
    queue = deque([root_node])
    while queue:
        print("\n" + "=" * 50)  
        parent_node = queue.popleft()
        num_children = int(input(f"\nHow many children does node {parent_node.value} have? "))

        for _ in range(num_children):
            print(f"\nAdding child to node: {parent_node.value}")
            child_node = get_node_input(parent_node)
            parent_node.add_child(child_node)
            queue.append(child_node)

def find_goal_path(goal_node, root):
    frontier = [root]
    reached = set([root.value])

    while frontier:
        cur_node = frontier.pop()
        node_children = cur_node.children_nodes

        for node in node_children:
            child_value = node.value
            if child_value == goal_node:
                return node
            
            if child_value not in reached:
                reached.add(child_value)
                frontier.append(node)
            
    return None

def print_ancestry(node):
    if not node:
        print("No goal path")

    lineage = []
    while node:
        lineage.append(str(node.value))
        node = node.parent
    ancestry_str = " -> ".join(lineage[::-1])
    print(ancestry_str)

def main():

    decision = int(input("Input 0 to design tree or 1 for random tree generation: "))

    if decision == 0:
        print("\nEnter the root node:")
        root = get_node_input(None)
        get_children_input(root)
        
        goal_node = int(input("\nEnter goal node value: "))
        print("\nGoal Path: ")
        print_ancestry(find_goal_path(goal_node, root))
    elif decision == 1:
        depth = int(input("\nEnter depth for tree: "))
        tree_builder = TreeBuilder(depth)

        tree = tree_builder.build_tree()
        root = tree[0]

        goal_node = tree[1]
        print("\nGoal Node to find: ", goal_node)
        print_ancestry(find_goal_path(goal_node, root))
        

if __name__ == "__main__":
    main()
