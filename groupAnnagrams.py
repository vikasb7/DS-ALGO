'''

Vikas Bhat
Group Anagrams
Type: String
Time Complexity: O(n)
Space Complexity: O(n)

'''


class main:
    def groupAnagrams(self, strs):

        d = {}

        for i in strs:
            temp = "".join(sorted(i))
            if temp not in d:
                d[temp] = [i]

            else:
                d[temp].append(i)

        return d.values()


if __name__=="__main__":
    v=main()
    print(v.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(v.groupAnagrams([""]))
    print(v.groupAnagrams(["a"]))