class Node:
    def __init__(self, value):
        self.value = value

        self.left_child = None

        self.right_child = None

        self.parent = None

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

    def set_left_child(self, left_child):
        self.left_child = left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

    def set_parent(self, parent):
        self.parent = parent

    def __str__(self):
        try:
            left_child_value = self.left_child.value

        except AttributeError:
            left_child_value = ""

        try:
            right_child_value = self.right_child.value

        except AttributeError:
            right_child_value = ""

        return f'Node(' \
               f'\n\tvalue: {self.value},' \
               f'\n\tleft_child_value: {left_child_value},' \
               f'\n\tright_child_value: {right_child_value}' \
               f'\n)'


class Tree:
    def __init__(self, first_node, grow_func=None):
        self.nodes = [first_node]

        self.grow_func = grow_func

    def grow_one(self):
        for node in self.get_leaves():
            left_value, right_value = self.grow_func(node.value)

            if left_value is None:
                node.set_left_child(None)

            elif left_value > 1:
                node.set_left_child(Node(left_value))

                node.left_child.set_parent(node)

                self.nodes.append(node.left_child)

            if right_value is None:
                node.set_right_child(None)

            elif right_value > 1:
                node.set_right_child(Node(right_value))

                node.right_child.set_parent(node)

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

    def get_lineages(self):
        lineages = []

        for leaf in self.get_leaves():
            current_lineage = []

            member = leaf

            while member:
                current_lineage.append(member)

                member = member.parent

            lineages.append(current_lineage)

        return lineages

    def print_lineages(self):
        k = 0

        for lineage in self.get_lineages():
            print("Lineage " + str(k))

            for node in lineage[::-1]:
                print("\n".join(['\t' + x for x in str(node).split("\n")]))

            k += 1

            print("")


if __name__ == "__main__":
    import collatz

    collatz_tree = Tree(Node(1), grow_func=collatz.reverse_step)

    collatz_tree.grow_n(5)

    # for node in collatz_tree.nodes:
    #     print(node)

    # print(collatz_tree.get_size())

    collatz_tree.print_lineages()

    lineages = collatz_tree.get_lineages()
