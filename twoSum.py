'''

Vikas Bhat
Two Sum
Time Complexity: O(n)
Space Complexity: O(n)
'''


class main:


    def twoSum(self,lis,target):

        d={}

        for i in range(len(lis)):
            if target-lis[i] in d:
                return [i,d[target-lis[i]]]
            else:
                d[lis[i]]=i

        return []


if __name__=="__main__":
    v=main()
    print(v.twoSum([2,7,11,15],9))
    print(v.twoSum([3,3], 6))
    print(v.twoSum([3, 2, 4], 6))