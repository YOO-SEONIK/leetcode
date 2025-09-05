class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        return hex(num & 0xFFFFFFFF)[2:]
        