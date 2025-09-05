class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "":
            return s2 == s3
        elif s2 == "":
            return s1 == s3
        elif s1 == "" and s2 == "":
            return s3 == ""
        
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        for one in range(len(s1) + 1):
            for two in range(len(s2) + 1):
                if one == 0 and two == 0:
                    dp[one][two] = True
                elif one == 0 and two != 0:
                    dp[one][two] = dp[one][two-1] and s2[two-1] == s3[one + two - 1]
                elif two == 0 and one != 0:
                    dp[one][two] = dp[one-1][two] and s1[one-1] == s3[one + two - 1]
                else:
                    dp[one][two] = ((dp[one-1][two] and s1[one-1] == s3[one + two - 1]) or 
                    (dp[one][two-1] and s2[two-1] == s3[one + two - 1]))

        return dp[len(s1)][len(s2)]
        