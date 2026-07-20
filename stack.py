


class Stack:
    



    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def push(self, input):
        if self.top == self.capacity -1:
            print("Array telah mencapai batas maksimum")
        else:
            self.top += 1
            self.array[self.top] = input

    def pop(self):
        if self.top < 0:
            print("Array Kosong")
        else:
            popping = self.array[self.top]
            self.top -= 1
            return popping
        
    def check(self):
        if self.top < 0:
            print("Array Kosong")
        else:
            print(self.array[self.top])




if __name__ == "__main__":

    rodri = Stack(3)
    rodri.push(5)
    rodri.push(7)
    rodri.push(10)
    rodri.push(2)
    rodri.pop()
    rodri.check()

