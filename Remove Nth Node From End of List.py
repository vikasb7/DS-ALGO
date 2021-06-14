'''

Vikas Bhat
Remove Nth Node From End of List
Type: LinkedList
Time Complexity: O(n)
Space Complexity: O(1)

'''


class Node:

    def __init__(self,val,next=None):
        self.val=val
        self.next=next


class main:

    def removeNthFromEnd(self,head,n):

        dummy=head
        res=head
        c=0

        while(dummy):
            c+=1
            dummy=dummy.next

        if n==c:
            return head.next


        for i in range(c-n-1):
            head=head.next

        head.next=head.next.next

        return res


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

    print(v.removeNthFromEnd(n1,2))

