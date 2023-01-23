class Node:
    def __init__(self, value):
        self.value = value

        self.left_child = None

        self.right_child = None

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

    def __str__(self):
        if self.left_child:
            left_child_value = self.left_child.value

        else:
            left_child_value = None

        if self.right_child:
            right_child_value = self.right_child.value

        else:
            right_child_value = None

        return str({"value": self.value, "left_child": left_child_value, "right_child": right_child_value})


class Tree:
    def __init__(self, first_node, grow_func=None):
        self.nodes = [first_node]

        self.grow_func = grow_func

    def grow_one(self):
        for node in self.get_leaves():
            left_value, right_value = self.grow_func(node.value)

            if left_value is None:
                node.left_child = None

            elif left_value > 1:
                node.left_child = Node(left_value)

                self.nodes.append(node.left_child)

            if right_value is None:
                node.right_child = None

            elif right_value > 1:
                node.right_child = Node(right_value)

                self.nodes.append(node.right_child)


    def grow_n(self, n):
        for i in range(n):
            self.grow_one()

    def get_leaves(self):
        leaves = []

        for node in self.nodes:
            if node.is_leaf():
                leaves.append(node)

        return leaves

    def get_first_node(self):
        return self.nodes[0]

    def get_values(self):
        return [node.value for node in self.nodes]

    def get_size(self):
        return len(self.nodes)

    def get_lineages(self, current_node=None, lineages=None):
        if current_node is None:
            assert lineages is None, "if current_node None, lineages must be None too."

            current_node = self.get_first_node()

            lineages = [[self.get_first_node()]]

        if current_node.left_child is not None and current_node.right_child is None:
            lineages[-1].append(self.get_lineages(current_node.left_child, lineages))

        elif current_node.left_child is None and current_node.right_child is not None:
            lineages[-1].append(self.get_lineages(current_node.right_child, lineages))

        elif current_node.left_child is not None and current_node.right_child is not None:
            lineages.append(lineages[-1])

            lineages[-2].append(self.get_lineages(current_node.left_child, lineages))

            lineages[-1].append(self.get_lineages(current_node.right_child, lineages))

        else:  # is leaf
            return lineages


if __name__ == "__main__":
    import collatz

    collatz_tree = Tree(Node(1), grow_func=collatz.reverse_step)

    collatz_tree.grow_n(2)

    # for node in collatz_tree.nodes:
    #     print(node)

    print(collatz_tree.get_size())

    lineages = collatz_tree.get_lineages()