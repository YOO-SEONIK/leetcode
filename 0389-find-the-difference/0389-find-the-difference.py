from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt_s = Counter(list(s))
        cnt_t = Counter(list(t))
        
        s_keys = list(cnt_s.keys())
        
        for key in s_keys:
            cnt_t[key] = cnt_t[key] - cnt_s[key]
            
        t_items = [item[0] for item in cnt_t.items() if item[1] != 0]
        
        answer = "".join(t_items)      
        
        return answer
        