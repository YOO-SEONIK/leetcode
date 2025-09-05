class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_str = s.lower()
        fin_str = []
        for char in low_str:
            if char.isalnum():
                fin_str.append(char)

        if fin_str == fin_str[::-1]:
            return True
        else:
            return False
        