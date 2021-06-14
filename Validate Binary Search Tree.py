'''
Vikas Bhat
Vaalidate Binary Search Tree
Type: String
Recursive:
Time Complexity: O(n)
Space Complexity: O(1)
Iterative:
Time Complexity: O(n)
Space Complexity: O(n)

'''

class TreeNode:

    def __init__(self,val=0,left=None,right=None):
        self.left=left
        self.right=right
        self.val=val

class main:

    # Recursive
    def isValidBST(self,root):

        def helper(node, minval, maxval):

            if not node:
                return True

            if node.val >= maxval:
                return False

            if node.val <= minval:
                return False

            return helper(node.left, minval, node.val) and helper(node.right, node.val, maxval)

        return helper(root, float("-inf"), float("inf"))

    # Iterative

    def isValidBST1(self,root):

        st=[(root,float("inf"),float("-inf"))]

        while st:

            node,max_val,min_val=st.pop()

            if not node:
                continue

            if not min_val<node.val<max_val:
                return False

            st.append((node.left,node.val,min_val))
            st.append((node.right, max_val, node.val))

        return True


if __name__=="__main__":
    t1=TreeNode(2)
    t1.left=TreeNode(1)
    t1.right=TreeNode(3)

    t2=TreeNode(1)
    t2.left=TreeNode(2)
    t2.right= TreeNode(3)

    v=main()

    print(v.isValidBST(t1))
    print(v.isValidBST(t2))
    print(v.isValidBST1(t1))
    print(v.isValidBST1(t2))

