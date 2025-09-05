class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        chars = Counter(magazine)

        for c in ransomNote:
            if c not in chars or chars[c] <= 0:
                return False
            chars[c] -= 1
        return True
        