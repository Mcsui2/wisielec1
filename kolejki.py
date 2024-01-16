class LIFO:
    def __init__(self):
        self.last =0
        self.buffer =[]
    def push(self,element):
        self.last +=1
        self.buffer.append(element)
    def pop(self):
        if self.last != 0:
            self.last -=1
            return self.buffer.pop(-1)
        
        else:
            print("Queue is empty!")
    def show(self):
        print(self.buffer)


class FIFO:
    def __init__(self):
        self.last =0
        self.buffer =[]
    def push(self,element):
        self.last +=1
        self.buffer.append(element)
    def pop(self):
        if self.last != 0:
            self.last -=1
            return self.buffer.pop(0)
        
        else:
            print("Queue is empty!")
    def show(self):
        print(self.buffer)










a = LIFO()
b = LIFO()
a.push(2)
a.push(1)
a.push(3)
a.push(7)
a.show()
a.pop()
a.show()
b.show()
