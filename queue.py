
class Queue:



    def __init__(self, max):
        self.max = max
        self.array = [None]* max
        self.front = 0
        self.rear = 0
        self.count = 0

    def Rear(self, input):
        if self.count == self.max:
            print("Array telah mencapai batas maksimum")
            return
        
        self.array[self.rear] = input
        self.rear = (self.rear + 1) % self.max
        self.count += 1
        return

    def popFront(self):
        if self.count == 0:
            print("Array masih kosong")
        else:
            pop = self.array[self.front]
            self.front = (self.front + 1) % self.max
            self.count -= 1
            print (pop)
        
    def checkQueue(self):
        if self.count == 0:
            print("Array masih kosong")
        else:
            print (self.array[self.front])





if __name__ == "__main__":



    igho = Queue(5)

    igho.Rear(4)
    igho.Rear(3)
    igho.Rear(2)
    igho.Rear(1)
    igho.Rear(7)

    igho.checkQueue()

    igho.popFront()
    igho.popFront()

    igho.Rear(8)

    igho.popFront()

    igho.Rear(9)

    igho.checkQueue()
