'''

Vikas Bhat
Longest Substring Without Repeating Characters
Type: String
Time Complexity: O(n)
Space Complexity: O(1)

'''

class main:

    def lengthOfLongestSubstring(self,s):

        if len(s)<1:
            return 0
        d={}
        start=0
        end=0
        res=float("-inf")

        while(end<len(s)):

            if s[end] in d and d[s[end]]>=start:
                start= d[s[end]]+1
            res=max(res,end-start+1)
            d[s[end]]=end
            end+=1

        return res




if __name__=="__main__":
    v=main()
    print(v.lengthOfLongestSubstring("abcabcbb"))
    print(v.lengthOfLongestSubstring("bbbbb"))
    print(v.lengthOfLongestSubstring("pwwkew"))
    print(v.lengthOfLongestSubstring(""))

