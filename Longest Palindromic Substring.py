'''

Vikas Bhat
Longest Palindromic Substring
Type: String
Time Complexity: O(n)
Space Complexity: O(1)

'''


class main:

    def longestPalindrome(self,s):

        def isPal(x,y):

            while(x>=0 and y<len(s) and s[x]==s[y]):
                x-=1
                y+=1

            return s[x+1:y]


        res=""
        for i in range(len(s)):
            a=isPal(i,i)
            if len(a) >len(res):
                res=a
            b = isPal(i, i+1)
            if len(b) > len(res):
                res=b

        return res

if __name__=="__main__":
    v=main()
    print(v.longestPalindrome("babad"))
