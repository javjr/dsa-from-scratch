
class Node:


    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None




class Linked:



    def __init__(self):
        self.head = None
        self.max = 5
        self.count = 0

    def insert_front(self, data):

        if self.count == self.max:
            print("Tempat Penuh")
            return
        
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
        
        new_node.next = self.head
        self.head = new_node
        self.count += 1


    def insert_back(self, data):
        if self.count == self.max:
            print("Tempat Penuh")
            return
        
        new_node = Node(data)

        if self.head is None:
            self.insert_front(data)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        
        new_node.prev = current
        current.next = new_node
        self.count += 1


    def insert_after(self, data, target_node):
        if self.count == self.max:
            print("Tempat Penuh")
            return
        
        new_node = Node(data)

        if self.head is None:
            self.insert_front(data)
            return
        
        current = self.head

        while current is not None and current.data != target_node:
            current = current.next
        
        if current is None :
            print("Node target tidak ditemukan")
            return
        
        new_node.prev = current
        new_node.next = current.next
        if new_node.next is not None:
            new_node.next.prev = new_node
        current.next = new_node
        self.count += 1

    def delete_front(self):
        if self.head is None:
            print("Empty")
            return
        
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        self.count -= 1
        
    def delete_target(self, target):
        if self.head is None:
            print("Empty")
            return
        
        if target == self.head.data:
            self.delete_front()
            return
        
        current = self.head
        while current is not None and current.data != target:
            current = current.next

        if current is None:
            print("Target tidak ditemukan")
            return
        if current.next is not None:
            current.next.prev = current.prev
        current.prev.next = current.next

        self.count -= 1
        
    

    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next








if __name__ == "__main__":


    
    tryya = Linked()

    tryya.insert_front(2)
    tryya.insert_front(9)

    tryya.display()

    tryya.insert_back(5)
    tryya.insert_back(3)
    tryya.insert_after(8,5)

    print("\n")
    tryya.display()

    tryya.delete_front()


    tryya.display()

    tryya.delete_target(8)

    
    tryya.display()