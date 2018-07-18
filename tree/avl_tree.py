#!/usr/bin/python3

enable_debug = True
count_debug = 0

def debug(msg):
    global enable_debug
    global count_debug
    if enable_debug:
        print("%s        count: %s" % (msg, count_debug))
        count_debug += 1


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.value_leading = '0'

    def __str__(self):
        if isinstance(self.value, int):
            if self.value_leading == '0':
                return str("%02d" % self.value)
            else:
                return str("%2d" % self.value)
        else:
            return str(self.value)


class AVL_Tree():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) >= 1:
            for i in args:
                self.insert(i)

    def insert(self, value):
        if value < -100 or value > 99:
            print("Only an integer of two digits allowed.")
            return False

        if self.node == None:
            self.node = Node(value)
            self.node.left = AVL_Tree()
            self.node.right = AVL_Tree()
            debug("  (%s) -> insert value." % value)
        else:
            if value < self.node.value:
                debug("  (%s) -> go left child. %s" % (value, self.node.value))
                self.node.left.insert(value)
            elif value > self.node.value:
                debug("  (%s) -> go right child. %s" % (value, self.node.value))
                self.node.right.insert(value)
            else:
                debug("  (%s) -> value duplicated." % value)
        self.rebalance()

    def delete(self, value):
        if self.node != None:
            if self.node.value == value:
                if self.node.left.node == None and \
                   self.node.right.node == None:
                    self.node = None
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node
                else:
                    node = self.node.right.node

                    if node != None:
                        while node.left != None:
                            if node.left.node == None:
                                break
                            else:
                                node = node.left.node
                        if node != None:
                            debug("  (%s) deleted, replaced by %s." % (self.node.value,
                                                                   node.value))
                            self.node.value = node.value
                            self.node.right.delete(node.value)
                    
                self.rebalance()
                return True
            elif value < self.node.value:
                self.node.left.delete(value)
            elif value > self.node.value:
                self.node.right.delete(value)
            self.rebalance()
        else:
            print("vlaue not found.")
            return False

    def rebalance(self):
        self.update_height(recurse=False)
        self.update_balance(recurse=False)
        while self.balance not in [-1, 0, 1]:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.left_rotate()
                    self.update_height()
                    self.update_balance()
                self.right_rotate()
                self.update_height()
                self.update_balance()

            if self.balance < -1: 
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
                    self.update_height()
                    self.update_balance()
                self.left_rotate()
                self.update_height()
                self.update_balance()

    def right_rotate(self):
        ''' top:               self.node
            middle:   left.node
            buttom:            right.node

                               left.node
                     right_node         self.node
        ''' 
        debug("  (%s) right rotate." % self.node.value) 
        top = self.node
        middle = top.left.node
        buttom = middle.right.node

        self.node = middle
        middle.right.node = top
        top.left.node = buttom

    def left_rotate(self):
        ''' top:               self.node
            middle:                     right.node
            buttom:            left.node

                               right.node
                      self.node          left.node
        ''' 
        debug("  (%s)left rotate." % self.node.value)
        top = self.node
        middle = top.right.node
        buttom = middle.left.node

        self.node = middle
        middle.left.node = top
        top.right.node = buttom

    def update_height(self, recurse=True):
        if self.node == None:
            self.height = -1
        else:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_height()
                if self.node.right != None:
                    self.node.right.update_height()
            self.height = max(self.node.left.height, 
                              self.node.right.height) + 1
            debug("  (%s) update height to %s." % (self.node.value, self.height))

    def update_balance(self, recurse=True):
        if self.node == None:
            self.balance = 0
        else:
            if recurse:
                if self.node.left != None:
                   self.node.left.update_balance()
                if self.node.right != None:
                   self.node.right.update_balance()
            self.balance = self.node.left.height - self.node.right.height
            debug("  (%s) update balance to %s."% (self.node.value, self.balance))

    def level_order_traverse(self, ignore_empty=True):
        queue = [self.node]
        output = []
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.value == '  ':
                if not ignore_empty:
                    if current_node.left == 'E' and current_node.right == 'E':
                        empty_node = Node('  ')
                        queue.append(empty_node)
                        queue.append(empty_node)
                    
                    output.append("%s" % current_node.value)
                continue
                 
            output.append("%s" % current_node)
            
            if current_node.left != None:
                if current_node.left.node != None:
                    queue.append(current_node.left.node)
                else:
                    if not ignore_empty:
                        empty_node = Node('  ')
                        empty_node.left = 'E'
                        empty_node.right = 'E'
                        queue.append(empty_node)
                
            if current_node.right != None:
                if current_node.right.node != None:
                    queue.append(current_node.right.node)
                else:
                    if not ignore_empty:
                        empty_node = Node('  ')
                        empty_node.left = 'E'
                        empty_node.right = 'E'
                        queue.append(empty_node)

        node_count = len(output)
        node = output[-1]
        while node == '  ':
            output.pop()
            node = output[-1]

        return output

    def inorder_traverse(self, ignore_empty=True):
        if self.node == None:
            if ignore_empty:
                return []
            return ['[]']

        inlist = []
        l = self.node.left.inorder_traverse(ignore_empty=ignore_empty)
        for i in l:
            inlist.append(i)

        inlist.append("%s" % self.node.value)

        l = self.node.right.inorder_traverse(ignore_empty=ignore_empty)
        for i in l:
            inlist.append(i)

        return inlist

    def display(self):
        print("\nDisplay tree:")
        bfs_list = self.level_order_traverse(ignore_empty=False)

        height = 1
        while True:
            if (2**height) > len(bfs_list):
                break
            height += 1
        
        max_length = 2**height
        node_counter = 0
        start_index = 0
        end_index = 1
        for i in range(height):
            node_count = 2**i
            space_count = int(max_length / (2**(i+1))) - 1

            start_index = node_counter
            end_index = (start_index*2) + 1

            for j in range(start_index, end_index):
                if j < len(bfs_list):
                    padding_str = "  "*space_count
                    print("%s%s%s"%(padding_str, 
                                    bfs_list[j],
                                     padding_str), end='')
                    print("  ", end='') 
            node_counter = j + 1
            print("")

        print("\n")

if __name__ == '__main__':
    input_list = [7, 14, 5, 2, 12, 6, 3, 11, 15, 4, 1, 8, 10, 9, 0, 13, 16, 17]

    avl_tree = AVL_Tree()

    print("Input value list: %s" % input_list)
    for input_value in input_list:
        avl_tree.insert(input_value)

    print("")
    print("Inorder traverse:\n%s" % avl_tree.inorder_traverse()) 

    print("")
    print("Level order traverse:\n%s" % avl_tree.level_order_traverse())

    print("")
    avl_tree.display()
 
    print("")
    print("Delete numbers 3")
    avl_tree.delete(3)
    avl_tree.display()

    print("Delete numbers 4")
    avl_tree.delete(4)
    avl_tree.display()

    print("Delete numbers 5")
    avl_tree.delete(5)
    avl_tree.display()

    print("Delete numbers 0")
    avl_tree.delete(0)
    avl_tree.display()
