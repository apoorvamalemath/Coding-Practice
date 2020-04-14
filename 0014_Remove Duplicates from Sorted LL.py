#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    cur=head
    while(cur):
        temp=cur
        while(temp):
            if(temp.data==cur.data):
                cur.next=temp.next
            else:
                break
            temp=temp.next
        cur=cur.next

    return head
