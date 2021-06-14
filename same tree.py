'''

Vikas Bhat
Same Tree
Type:  Tree
Time Complexity: O(n)
Space Complexity: O(1)

'''

class TreeNode:

    def __init__(self,val=0,left=None,right=None):
        self.left=left
        self.right=right
        self.val=val

class main:


    #Recursive


    def sameTree(self,root1,root2):

        if root1 and not root2:
            return False

        if root2 and not root1:
            return False

        if not root1 and not root2:
            return True

        if root1.val!=root2.val:
            return False

        return self.sameTree(root1.left,root2.left) and self.sameTree(root1.right,root2.right)

if __name__=="__main__":
    t1=TreeNode(1)
    t1.left=TreeNode(2)
    t1.right=TreeNode(3)

    t2=TreeNode(1)
    t2.left=TreeNode(2)
    t2.right= TreeNode(3)

    v=main()

    print(v.sameTree(t1,t2))