import SLL_Class as sll

s=sll.SinglyLinkList()


# tmp=None
# nodes=int(input("Enter no of Nodes"))
# for i in range(0,nodes):
#     val=int(input("Enter the value of the node"))
#     n=sll.Node(val)
#     if s.head==None:
#         s.head=n
#         tmp=s.head
#     else:
#         tmp.next=n
#         tmp=tmp.next

# s.tail=tmp
sll.getVal(s)
sll.showVal(s)

