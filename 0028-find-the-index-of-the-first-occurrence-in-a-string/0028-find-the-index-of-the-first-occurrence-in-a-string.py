class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len, n_len = len(haystack), len(needle)

        for idx in range(h_len - n_len + 1):
            if haystack[idx:idx+n_len] == needle:
                return idx
            
        return -1
        