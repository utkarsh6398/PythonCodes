class SinglyLinkList:
    def __init__(self):
        self.head=None
        self.tail=None

class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def showVal():
    tmp = s.head
    while tmp.next != None:
        print(tmp.val,end="-")
        tmp = tmp.next

    print(tmp.val)

def insertBefore(v):
    n=Node(v)
    n.next=s.head
    s.head=n

def insertAfter(v):
    n=Node(v)
    print(n.val)
    s.tail.next=n
    s.tail=n

def insertMid(v,pos):
    if pos==1:
        Bef()
    elif pos>1:
        n = Node(v)
        index = pos-2
        tmp = s.head
        while index>0:
            tmp=tmp.next
            index-=1

        n.next=tmp.next
        tmp.next=n

def deleteNode(pos):
    if s.head==s.tail:
        s.head,s.tail=None,None
    elif pos==1:
        s.head=s.head.next
    elif pos == -1:
        tmp = s.head
        while tmp.next!=s.tail:
            tmp = tmp.next

        s.tail=tmp
        tmp.next = None
    else:
        tmp=s.head
        index=pos-2
        while index>0:
            tmp=tmp.next
            index-=1

        tmp.next=tmp.next.next

def deleteDup():
    l=[]
    tmp = s.head
    l.append(tmp.val)
    while tmp.next!= None:
        if tmp.next.val in l:
             tmp.next=tmp.next.next
        else:
            l.append(tmp.next.val)
        tmp = tmp.next



def backTraverse():
    tmp=s.head
    end=s.tail
    while s.head!=end:
        while tmp.next!=end:
            tmp=tmp.next
        print(tmp.next.val,end=">")
        end=tmp
        tmp=s.head
    print(s.head.val)

s=SinglyLinkList()
n1=Node(1)
n2=Node(2)
n3=Node(1)
n4=Node(4)
s.head=n1
s.tail=n4
n1.next=n2
n2.next=n3
n3.next=n4

cont='n'
cont = input("Start?Y/N:")
while cont!='n':
    a = input("Where?B/M/A/E/R/D:")
    if a == 'b':
        v = input("Val:")
        insertBefore(v)
        showVal()
    elif a == 'a':
        v = input("Val:")
        insertAfter(v)
        showVal()
    elif a=='m':
        print("Curr LL:",end=' ')
        showVal()
        v = input("Val:")
        pos = int(input("Pos:"))
        insertMid(v,pos)
        showVal()
    elif a=='r':
        backTraverse()
    elif a=='d':
        deleteDup()
        showVal()
    else:
        print("Curr LL:", end=' ')
        showVal()
        pos = int(input("Pos:"))
        deleteNode(pos)
        showVal()

    cont = input("More?Y/N:")