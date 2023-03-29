class LL:
    def __init__(self):
        self.head=None
        self.tail=None

class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
    
class Stack:
    def __init__(self):
        pass
    n=Node(val)


def isEmpty(s):
    if s.head==None and s.tail==None:
        return True
    else:
        return False
        
def push(s,val):
    
    if s.head==None:
        s.head=n
        s.tail=n
    else:
        n.next=s.head
        s.head=n

def pop(s):
    if isEmpty(s)==True:
         print("Stack is Empty")
    else:
        print(s.head.val)
        if s.head==s.tail:
            s.head=s.head.next
            s.tail=s.head
        else:
            s.head=s.head.next

def peek(s):
    if isEmpty(s)==True:
         print("Stack is Empty")
    else:
        print(s.head.val)
    
def delete(s):
    s.head=None
    s.tail=None
    
def traverse(s):
    tmp = s.head
    while tmp.next != None:
        print(tmp.val,end="-")
        tmp = tmp.next

    print(tmp.val)


s=Stack()
push(s,1)
push(s,2)
push(s,3)
push(s,4)
traverse(s)
peek(s)
pop(s)
peek(s)
pop(s)
peek(s)
traverse(s)
delete(s)
