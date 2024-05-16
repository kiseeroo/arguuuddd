class Node:
    def __init__(self, multi_strs_in_node):
        self.multi_strs_in_node = multi_strs_in_node
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return str(self.multi_strs_in_node)
    
class Tree:
    def __init__(self, multi_strs_in_root):
        self.root = Node(multi_strs_in_root)

    def add_child(self, parent_node, multi_strs_in_child_node):
        child_node = Node(multi_strs_in_child_node)
        parent_node.add_child(child_node)
        return child_node

    def __repr__(self):
        return str(self.root)

    def iterate_strings_in_all_nodes(self, node, traversal_order='infix'):
        """
        Iterate through all strings in all nodes of the tree based on the chosen traversal order.
        
        Parameters:
            node (Node): The current node to start traversal from.
            traversal_order (str): The chosen traversal order ('infix', 'prefix', or 'postfix').
        """
        if traversal_order == 'infix':
            yield from self._infix_traversal(node)
        elif traversal_order == 'prefix':
            yield from self._prefix_traversal(node)
        elif traversal_order == 'postfix':
            yield from self._postfix_traversal(node)
        else:
            raise ValueError("Invalid traversal order")

    def _infix_traversal(self, node):
        """
        Perform infix traversal starting from the given node.
        """
        if node is not None:
            if len(node.children) >= 1:
                yield from self._infix_traversal(node.children[0])
            yield node.multi_strs_in_node
            if len(node.children) == 2:
                yield from self._infix_traversal(node.children[1])

    def _prefix_traversal(self, node):
        """
        Perform prefix traversal starting from the given node.
        """
        if node is not None:
            yield node.multi_strs_in_node
            if len(node.children) >= 1:
                yield from self._prefix_traversal(node.children[0])
            if len(node.children) == 2:
                yield from self._prefix_traversal(node.children[1])

    def _postfix_traversal(self, node):
        """
        Perform postfix traversal starting from the given node.
        """
        if node is not None:
            if len(node.children) >= 1:
                yield from self._postfix_traversal(node.children[0])
            if len(node.children) == 2:
                yield from self._postfix_traversal(node.children[1])
            yield node.multi_strs_in_node

def tree_sample():
    t = Tree(['root', 'depth_0'])
    n1 = t.add_child(t.root, ['node1', 'node_left', 'depth_1'])
    n2 = t.add_child(t.root, ['node2', 'node_right', 'depth_1'])
    n3 = t.add_child(n1, ['node3', 'node_left_left', 'depth_2'])
    n4 = t.add_child(n1, ['node4', 'node_left_right', 'depth_2'])
    t.add_child(n2, ['node5', 'node_right_left', 'depth_2'])
    t.add_child(n2, ['node6', 'node_right_right', 'depth_2'])
    t.add_child(n3, ['node7', 'node_left_left_left', 'depth_3'])
    t.add_child(n3, ['node8', 'node_left_left_right', 'depth_3'])
    t.add_child(n4, ['node9', 'node_right_left_left', 'depth_4'])

    for s in t.iterate_strings_in_all_nodes(t.root):
        print(s)
    

if __name__ == '__main__':
    tree_sample()
