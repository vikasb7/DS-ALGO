'''

Vikas Bhat
Palindromic Substrings
Type: String
Time Complexity: O(n)
Space Complexity: O(1 )

'''

class main:

    def countSubstrings(self,s):

        self.ans=0

        def isPal(l,r):
            while(l>=0 and r<len(s)):
                if s[l]!=s[r]:
                    break
                self.ans+=1
                l-=1
                r+=1


        for  i in range(len(s)):
            isPal(i,i)
            isPal(i,i+1)


        return self.ans


if __name__=="__main__":
    v=main()
    print(v.countSubstrings("abc"))
    print(v.countSubstrings("aaa"))