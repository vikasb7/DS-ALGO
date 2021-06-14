'''

Vikas Bhat
Valid Palindrome
Type: String
Time Complexity: O(n)
Space Complexity: O(1)

'''


class main:

    def isPalindrome(self,s):

        res=""

        for i in s:
            if i.isalnum():
                res+=i.lower()



        return res==res[::-1]



if __name__=="__main__":
    v=main()
    print(v.isPalindrome("A man, a plan, a canal: Panama"))
    print(v.isPalindrome("race a car"))

