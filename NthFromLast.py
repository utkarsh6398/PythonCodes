#Remove Dup from SLL
import SLL_Class as sll

#Linked List created and values are fetched
s=sll.SinglyLinkList()
sll.getVal(s)
sll.showVal(s)

nth=int(input("Enter the nth from last to be found"))

#Plcing one pointer at the start and one pointer len-n ahead of start
tmp=s.head
tmp2=s.head
for i in range(nth-1):
    tmp2=tmp2.next

#Driver Code
while tmp2.next!=None:
    tmp=tmp.next
    tmp2=tmp2.next
print("The desired value is: ",tmp.val)