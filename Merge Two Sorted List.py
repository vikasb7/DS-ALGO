'''

Vikas Bhat
Merge Two Sorted List
Type: LinkedList
Time Complexity: O(n)
Space Complexity: O(1)

'''

class Node:

    def __init__(self,val,next=None):
        self.val=val
        self.next=None

class main:

    def mergeTwoLists(self,l1,l2):
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2

        ans=res=Node(0)

        while  l1 and l2:

            if l1.val<l2.val:
                res.next=l1
                l1=l1.next
            else:
                res.next=l2
                l2=l2.next

            res=res.next


        if l1:
            res.next=l1
        if l2:
            res.next=l2

        return ans.next



if __name__=="__main__":
    n1=Node(1)
    n2=Node(2)
    n3=Node(4)
    m1=Node(1)
    m2=Node(3)
    m3 = Node(4)

    n1.next=n2
    n2.next=n3

    m1.next=m2
    m2.next=m3




    v=main()

    print(v.mergeTwoLists(n1,m1))