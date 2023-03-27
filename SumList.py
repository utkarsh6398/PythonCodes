#Remove Dup from SLL
import SLL_Class as sll

#Linked List created and values are fetched
s1=sll.SinglyLinkList()
s2=sll.SinglyLinkList()
s3=sll.SinglyLinkList()
sll.getVal(s1)
sll.getVal(s2)
sll.showVal(s1)
sll.showVal(s2)

#Head pointers for the two LL
t1=s1.head
t2=s2.head
digit1,digit2=0,0
carry=0

#Driver Code
while t1!=None or t2!=None:
    
    if t1==None:
        digit1=0
        digit2=int(t2.val)
        t2=t2.next
    elif t2==None:
        digit2=0
        digit1=int(t1.val)
        t1=t1.next
    else:
        digit1=int(t1.val)
        digit2=int(t2.val)
        t1=t1.next
        t2=t2.next

    #Addition code
    sum=digit1+digit2+carry
    carry=0
    if sum>9:
        sum=sum-10
        carry=1
    
    #Adding sum of each digit to a new node in reverse order
    n=sll.Node(sum)
    if s3.head==None:
        s3.head=n
        s3.tail=n
    else:
        n.next=s3.head
        s3.head=n


if carry==1:
    n=sll.Node(carry)
    n.next=s3.head
    s3.head=n

sll.showVal(s3)