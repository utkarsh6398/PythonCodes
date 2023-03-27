#Remove Dup from SLL
import SLL_Class as sll

#Linked List created and values are fetched
s=sll.SinglyLinkList()
sll.getVal(s)
sll.showVal(s)

#Empty list to hold values and check dup values
l=[]

tmp=s.head
l.append(tmp.val)

#Driver Code
while tmp != s.tail:
    if tmp.next.val in l:
        tmp.next=tmp.next.next
    else:
        l.append(tmp.val)

    tmp=tmp.next

print("LL after removing dup nodes: ")
sll.showVal(s)