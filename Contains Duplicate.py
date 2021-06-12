'''

Vikas Bhat
Contains Duplicate
Time Complexity: O(n)
Space Complexity: O(n)
'''

class main:

    def containsDuplicate(self,nums):

        return len(nums)!=len(set(nums))



if __name__=="__main__":
    v=main()
    print(v.containsDuplicate([1,2,3,1]))
    print(v.containsDuplicate([1,2,3,4]))
    print(v.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

