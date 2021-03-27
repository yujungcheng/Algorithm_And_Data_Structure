#!/usr/bin/python3
''' B-Tree Structure

         (B_Tree)
         | |
         | degree ---- Integer
         |
         (Node)
         | | |
         | | is_leaf ---- True/False
         | values ---- [integer, integer, ...]
         children ---- [(Node), (Node), ...]
                        | | |
                        | | is_leaf
                        | values
                        children
'''

class Node(object):
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.values = []
        self.children = []

    def __str__(self):

        if self.is_leaf:
            return "Leaf Node, values: %s\n" % self.values
        else:
            children_info = []
            output_str = []
            for child in self.children:
                first_value = child.values[0]
                last_value = child.values[-1]
                children_info.append("%s to %s" % (first_value, last_value))
                #print(child.__str__())

            return "Tree Node: %s values, %s children\n" \
                   "  values: %s\n" \
                   "  children: %s\n" % (len(self.values),
                                         len(children_info),
                                         self.values,
                                         children_info)



class B_Tree(object):
    def __init__(self, degree):
        self.node = Node(is_leaf=True)
        self.degree = degree  # contained 2*degree - 1 values

    def insert(self, value):

        current_node = self.node  # copy of self.node

        if len(self.node.values) == (2*self.degree) - 1:
            new_node = Node()
            self.node = new_node  # set self.node to a new Node
            new_node.children.insert(0, current_node)

            self._split_child(new_node, 0)
            self._insert_value_to_node(new_node, value)
        else:
            self._insert_value_to_node(current_node, value)

    def _insert_value_to_node(self, node, value):
        if node.is_leaf:
            # insert to the node
            i = len(node.values)
            node.values.append(value)
            while i >= 1 and node.values[i] < node.values[i-1]:
                self._swap(node.values, i, i-1)
                i -= 1
            node.values[i] = value
        else:
            # insert to a child of the node
            i = len(node.values) - 1
            while i >= 0 and value < node.values[i]:
                i -= 1
            i += 1
            #print("%s %s" % (i,len(node.children)))
            if len(node.children[i].values) == (2*self.degree) - 1:
                self._split_child(node, i)
                if value > node.values[i]:
                    i += 1
            self._insert_value_to_node(node.children[i], value)

    def _split_child(self, node, index):
        degree = self.degree

        child = node.children[index]
        new_node = Node(is_leaf=child.is_leaf)  # new child node

        node.children.insert(index+1, new_node)
        node.values.insert(index, child.values[degree-1])

        new_node.values = child.values[degree:(2*degree-1)]
        child.values = child.values[0:(degree-1)]

        if not child.is_leaf:
            new_node.children = child.children[degree:(2*degree)]
            child.children = child.children[0:(degree-1)]

    def _swap(self, list_data, x, y):
        list_data[x], list_data[y] = list_data[y], list_data[x]

    def __str__(self):
        print("\n[ Node info ]")
        print("-"*60)
        n = self.node
        children_str = '\n'.join([child.__str__() for child in n.children])
        return n.__str__()+'\n'+children_str

    def display(self):  # has bug, display incorrectly
        print("\nDisplay:")
        print("-"*40)
        queue = [self.node, '\n']
        output = []
        level_node_counter_queue = []
        temp_node_counter = 0

        level_node_count = 0
        while len(queue) > 0:
            node = queue.pop(0)

            if node == '\n':
                output.append(node)
                continue

            node_counter = 0
            for child in node.children:
                queue.append(child)
                node_counter += 1

            level_node_counter_queue.append(node_counter)
            if len(level_node_counter_queue) >= 1:
                level_node = level_node_counter_queue[0]

            if level_node_count == level_node+1:
                output.append('\n')
                level_node_count = 0
                level_node_counter_queue.pop()
            else:
                level_node_count += 1

            output.append("%s" % node.values)


        print("  ", end='')
        for item in output:
            if item != '\n':
                print("%s " % item, end='')
            else:
                print("\n  ", end='')
        print()

    def display_tree(self):
        print("\n[ Display Tree ]")
        print("-"*60)
        node_queue = [self.node, None]
        while True:

            if len(node_queue) == 0:
                break
            node = node_queue.pop(0)

            if node == None:
                print("")
                if len(node_queue) == 0:
                    break
                node_queue.append(None)
                continue
            else:
                values = map(str, node.values)
                print("%s " % ','.join(values), end='')

                children = node.children
                for child in children:
                    node_queue.append(child)


if __name__ == '__main__':
    # tree test 1
    input_list = [7, 14, 5, 2, 12, 6, 3, 11, 15, 4, 1, 8, 10, 9, 0, 13, 16, 17]
    b_tree = B_Tree(2)
    for input_value in input_list:
        b_tree.insert(input_value)

    b_tree.display_tree()
    print(b_tree)


    # tree test 2
    b_tree = B_Tree(2)
    for i in range(20):
        b_tree.insert(i)

    b_tree.display_tree()
    print(b_tree)
