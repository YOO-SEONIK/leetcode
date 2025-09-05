class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        L = len(s)
        
        if L == 1:
            return s
        
        ans = ""
        ans += (s[0: L % k])
        
        for i in range(L % k, L, k):
            if len(ans) > 0:
                ans += '-'
            ans += s[i: i + k]
            
        return (ans)
        