class Queue():
    def __init__(self):
        self.list=[]

    def push(self,val):
        self.list.append(val)
    
    def pop(self):
        if self.list==[]:
            print("Stack is Empty")
        else:
            print(self.list.pop())
    
    def isEmpty(self):
        if self.list==[] or self.list==None:
            print("Stack is Empty")
        else:
            print("Stack is not Empty")
    
    def peek(self):
        if self.list==[]:
            print("Stack is Empty")
        else:
            print(self.list[-1])
    
    def delete(self):
        self.list=None
        print(self.list)
    

s=Stack()
s.push(1)
s.peek()
s.push(2)
s.peek()
s.pop()
s.peek()
s.isEmpty()
s.delete()
s.isEmpty()