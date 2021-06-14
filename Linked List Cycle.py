'''

Vikas Bhat
Linked List Cycle
Type: Linked List
Time Complexity: O(n)
Space Complexity: O(n)

'''

class Node:

    def __init__(self,val):
        self.val=val
        self.next=None

class main:

    def hasCycle(self,head):

        st=set()

        while(head):
            if head in st:
                return True
            else:
                st.add(head)

            head=head.next


        return False



if __name__=="__main__":
    n=Node(3)
    n1=Node(2)
    n2=Node(0)
    n3=Node(-4)

    n.next = n1
    n1.next = n2
    n2.next = n3
    n3.next=n1

    v=main()

    m=Node(1)

    print(v.hasCycle(n))
    print(v.hasCycle(m))