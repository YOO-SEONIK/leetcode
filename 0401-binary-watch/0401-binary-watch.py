from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for h in range(12):
            for m in range(60):
                if (h.bit_count() + m.bit_count()) == turnedOn:  # Py3.8+
                    ans.append(f"{h}:{m:02d}")
        return ans
        