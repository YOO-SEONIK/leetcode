class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        output = [-1 for _ in range(k)]
        
        def combination(index, selected):
            if selected == k:
                answer.append(output[:])
                return
            if index > n:
                return
            
            output[selected] = index
            combination(index+1, selected+1)
            combination(index+1, selected)
        
        combination(1, 0)
        return answer
        