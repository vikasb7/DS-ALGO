'''

Vikas Bhat
Climbing Stairs
Type: Array/List
Type: DP
Time Complexity: O(n)
Sapace Complexity: O(1)

'''

class main:

    def climbStairs(self,n):

        if n==1:
            return 1
        if n==2:
            return 2

        prev=0
        curr=1

        for i in range(n):
            prev,curr=curr,curr+prev

        return curr





if __name__=="__main__":
    v=main()
    print(v.climbStairs(2))
    print(v.climbStairs(3))