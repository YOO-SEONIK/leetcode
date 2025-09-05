class Solution:
    def countAndSay(self, n: int) -> str:
        string = '1'
        
        for i in range(n-1):
            past = string[0]
            count = 1
            new_string = ''
            
            for digit in string[1:]:
                if digit == past:
                    count += 1
                else:
                    new_string += str(count) + str(past)
                    past = digit
                    count = 1
            
            new_string += str(count) + str(past)
            string = new_string
        
        return string
        