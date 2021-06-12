'''

Vikas Bhat
Best Time to Buy and Sell Stock
Time Complexity: O(n)
Space Complexity: O(1)

'''

class main:

    def maxProfit(self,prices):

        res=0
        min=float("inf")

        for i in prices:
            if i<min:
                min=i
            if i-min>res:
                res=i-min

        return res



if __name__=="__main__":
    v=main()
    print(v.maxProfit([7,1,5,3,6,4]))
    print(v.maxProfit([7,6,4,3,1]))
