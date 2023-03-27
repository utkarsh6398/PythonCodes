class SinglyLinkList:
    def __init__(self):
        self.head=None
        self.tail=None

class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def showVal(s):
    tmp = s.head
    while tmp.next != None:
        print(tmp.val,end="-")
        tmp = tmp.next

    print(tmp.val)

def getVal(s):
    tmp=None
    nodes=int(input("Enter no of Nodes: "))
    for i in range(0,nodes):
        val=int(input("Enter the value of the node: "))
        n=Node(val)
        if s.head==None:
            s.head=n
            tmp=s.head
        else:
            tmp.next=n
            tmp=tmp.next

    s.tail=tmp

