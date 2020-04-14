class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
            return
        temp=self.head
        while(temp.next):
            tem=temp.next
        temp.next=new_node
        return self.head

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next
        print()

if __name__ == "__main__":
    llist=LinkedList()
    n=int(input())
    for i in range(n):
        data=int(input())
        head=llist.insert(data)
    llist.printList()
