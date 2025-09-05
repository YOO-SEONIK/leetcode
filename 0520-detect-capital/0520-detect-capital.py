class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if word.capitalize() == word or word.isupper() or word.islower() else False
        