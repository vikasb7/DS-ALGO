'''

Vikas Bhat
Product of Array Except Self
Time Complexity : O(n)
Space Complexity: O(n)

'''

class main:

    def productExceptSelf(self,nums):
        res = [1]
        left = 1

        for i in range(len(nums) - 1, 0, -1):
            res.append(res[-1] * nums[i])

        res=res[::-1]

        for j in range(0,len(nums)):
            res[j]*=left
            left*=nums[j]

        return res




if __name__=="__main__":
    v=main()
    print(v.productExceptSelf([1,2,3,4]))
    print(v.productExceptSelf([-1,1,0,-3,3]))
