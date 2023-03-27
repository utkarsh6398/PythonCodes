#Remove Dup from SLL
import SLL_Class as sll

#Linked List created and values are fetched
s=sll.SinglyLinkList()
sll.getVal(s)
sll.showVal(s)

# Get the partition value
part=int(input("Enter the partition value: "))

tmp=s.head 
s1=sll.SinglyLinkList()
while tmp.next!=None:
    if tmp.val<



# tmp=s.head 
# while tmp.next!=None:
#     if tmp==s.head:
#         if tmp.val<part:
#             tmp=tmp.next
#         elif tmp.val==part:
#             tmp=tmp.next
#         else:
#             s.tail.next=tmp
#             s.head=s.head.next
#             tmp.next=None
#             tmp=s.head              
#     else:
#         if tmp.next.val<part:
#             x=tmp.next
#             tmp.next=tmp.next.next
#             x.next=s.head
#             s.head=x
#         elif tmp.next.val>part:
#             x=tmp.next
#             tmp.next=tmp.next.next
#             s.tail.next=x
#             x.next=None
#         else:
#             pass
#         tmp=tmp.next

# sll.showVal(s)