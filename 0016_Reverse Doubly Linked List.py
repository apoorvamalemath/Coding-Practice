def reverse(head):
    cur=head
    while(cur):
        temp=cur.prev
        cur.prev=cur.next
        cur.next=temp
        cur=cur.prev
    if temp is not None: 
        head = temp.prev 
    return head
