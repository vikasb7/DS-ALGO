'''

Vikas Bhat
Valid Anagram
Type: String
Time Complexity: O(n log n)
Space Complexity: O(1)

'''

class main:

    def isAnagram(self,s,t):

        if len(s)!=len(t):
            return False

        return sorted(s)==sorted(t)


if __name__=="__main__":
    v=main()
    print(v.isAnagram("anagram","nagaram"))
    print(v.isAnagram("car","rat"))
