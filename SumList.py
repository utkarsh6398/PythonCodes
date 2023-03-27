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

t1=s1.head
t2=s2.head
digit1,digit2=0,0
carry=0
tmp=s3.head
while t1.next!=None or t2.next!=None:
    
    if t1.next==None:
        digit2=int(t2.val)
        t2=t2.next
        sum=digit1+digit2+carry
    elif t2.next==None:
        digit2=0
        digit1=int(t1.val)
        t1=t1.next
    else:
        digit1=int(t1.val)
        digit2=int(t2.val)
        t1=t1.next
        t2=t2.next

    #Addition code
    # print(digit1,"+",digit2)

    carry=0
    if sum>9:
        sum=sum-10
        carry=1
    n=sll.Node(sum)
    print(digit1,"+",digit2,"=",sum)
    if tmp==s3.head:
        s3.head=n
        s3.tail=n
        tmp=s3.head
    else:
        tmp.next=n
        s3.tail=n
        tmp=s3.tail



if carry==1:
    n=sll.Node(carry)
    tmp.next=n
    s3.tail=n
    tmp=s3.tail

sll.showVal(s3)