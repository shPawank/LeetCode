class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

count=0

node1 = ListNode(7)
node2 = ListNode(9)
node3 = ListNode(12)
node4 = ListNode(45)
node5 = ListNode(27)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

head=node1
current=head

while current:
    print(current.val)
    current=current.next


# print(node1.val)
# print(node2.val)
# print(node3.val)
# print(node1.next.next.val)

def print_list(head):
    current=head
    val=[]
    while current:
        vals.append(str(current.val))
        current=current.next
    print("->", join(vals) if vals else "Empty")



def count_nodes(head):
    count=0
    current=head
    while current:
        count+=1
        current=current.next
    return count

print(count_nodes(head))





def count_n(head):
    c=0
    current=head
    while current:
        c+=1
        current=current.next
    return c
print(count_n(head))
