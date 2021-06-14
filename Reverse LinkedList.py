'''

Vikas Bhat
Reverse LinkedList
Type: LinkedList
Time Complexity: O(n)
Space Complexity: O(1)

'''


class Node:

    def __init__(self,val,next=None):
        self.val=val
        self.next=None

class main:

    def reverseList(self,head):
        prev=None

        while(head):
            temp=head.next
            head.next=prev
            prev=head
            head=temp


        while(prev):
            print(prev.val)
            prev=prev.next


if __name__=="__main__":
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5


    v=main()

    print(v.reverseList(n1))
