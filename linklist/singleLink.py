class Node(object):    def __init__(self, data_val=None):        self.data_val = data_val        self.next_val = Noneclass SingleLinkList(object):    def __init__(self):        self.head_val = None    def show(self):        print_val = self.head_val        while print_val is not None:            print(print_val.data_val)            print_val = print_val.next_vallist1 = SingleLinkList()list1.head_val = Node("Mon")e2 = Node("Tue")e3 = Node("Wed")e4 = Node("Fri")e5 = Node("Sun")list1.head_val.next_val = e2e2.next_val = e3e3.next_val = e4e4.next_val = e5list1.show()