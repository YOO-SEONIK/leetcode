class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic :
                dic[s[i]] = 1
            else : 
                dic[s[i]] += 1
        check = False
        li = []
        for counting in dic :
            if dic[counting] %2 == 1 :
                check = True
            li.append(dic[counting])
        res = 0
        for i in range(len(li)) : 
            res += li[i] - (li[i] % 2)
        return res if check == False else res+1 
        