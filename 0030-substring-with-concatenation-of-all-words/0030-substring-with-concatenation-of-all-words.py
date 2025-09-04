class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answer = []
        n = len(s)
        sorted_words = sorted(words)
        word_size = len(words[0])
        start = 0
        end = word_size * len(words)

        while end <= n:
            substring_words = [s[i:i + word_size] for i in range(start, end, word_size)]
            if sorted(substring_words) == sorted_words:
                answer.append(start)

            start += 1
            end += 1
            
        return answer
        