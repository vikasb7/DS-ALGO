'''

Vikas Bhat
Container With Most Water
Time Complexity: O(n)
Sapce Complexity: O(1)

'''


class main:

    def maxArea(self,height):

        area=1
        s=0
        e=len(height)-1


        while s<e:

            area= max(area,(e-s)*min(height[s],height[e]))

            if height[s]<=height[e]:
                s+=1
            else:
                e-=1

        return area


if __name__=="__main__":
    v=main()
    print(v.maxArea([1,8,6,2,5,4,8,3,7]))
    print(v.maxArea([1,1]))
    print(v.maxArea([4,3,2,1,4]))