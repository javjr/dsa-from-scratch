
class Node:


    def __init__(self,data):
        self.data = data
        self.next = None
        




class Linked:

    
    def __init__(self):
        self.head = None
        self.max = 5
        self.count = 0

    def insert_front(self, data):
        if self.count == self.max:
            print("Tempat Telah Penuh")
            return
        
        new_node = Node(data)
        
        new_node.next = self.head 
        self.head = new_node
        self.count += 1

    def insert_back(self, data):
        if self.count == self.max:
            print("Tempat Telah Penuh")
            return
        
        new_node = Node(data)
        
        if self.head == None:
            self.insert_front(data)
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node #bug
        self.count += 1

    def insert_after(self, node_target, data):
        if self.count == self.max:
            print("Tempat Telah Penuh")
            return

        current = self.head
        while current.next is not None and current.data != node_target:
            current = current.next

        if current.next is None:
            print("Target node tidak ditemukan")
            return
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node 
        self.count += 1

    def reverse(self):
        current = self.head
        prev = None
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
            
    
    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next





if __name__ == "__main__":

    trial = Linked()

    trial.insert_front(9)
    trial.insert_back(6)
    trial.insert_back(4)
    trial.insert_after(6,5)
    trial.display()
            
        

