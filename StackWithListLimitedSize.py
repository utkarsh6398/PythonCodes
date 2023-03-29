class Stack():
    def __init__(self,size):
        self.list=[]
        self.size=size

    def isEmpty(self):
        if self.list==[] or self.list==None:
            return True
        else:
            return False

    def isFull(self):
        if self.size==0:
            return True
        else:
            return False
        
    def push(self,val):
        if self.isFull()==False:
            self.list.append(val)
            self.size-=1
        else:
            print("The Stack if Full")

    def pop(self):
        if self.isEmpty()==True:
            print("Stack is Empty")
        else:
            print(self.list.pop())
    
    def peek(self):
        if self.isEmpty()==True:
            print("Stack is Empty")
        else:
            print(self.list[-1])
    
    def delete(self):
        self.list=None
        print(self.list)
    
    def traverse(self):
        print(self.list[::-1])


s=Stack(2)
s.push(1)
s.peek()
s.push(2)
s.peek()
s.push(3)
s.traverse()