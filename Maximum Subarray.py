'''

Vikas Bhat
Maximum Subarray
Time Complexity: O(n)
Space Complexity: O(1)

'''

class main:

    def maxSubArray(self,lis):
        total_sum= float("-inf")
        curr_sum= float("-inf")

        for i in lis:
            curr_sum=max(i,curr_sum+i)
            total_sum=max(curr_sum,total_sum)

        return total_sum




if __name__=="__main__":
    v=main()
    print(v.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(v.maxSubArray([1]))
    print(v.maxSubArray([5,4,-1,7,8]))