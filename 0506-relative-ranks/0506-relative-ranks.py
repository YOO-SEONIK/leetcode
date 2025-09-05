class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score= sorted(score, reverse=True)
        rank_score = {}
        for i in range(len(sorted_score)):
            if i == 0:
                rank_score[sorted_score[i]] = 'Gold Medal'
            elif i == 1:
                rank_score[sorted_score[i]] = 'Silver Medal'
            elif i == 2:
                rank_score[sorted_score[i]] = 'Bronze Medal'
            else:
                rank_score[sorted_score[i]] = str(i+1)
        
        return [rank_score[s] for s in score]
        