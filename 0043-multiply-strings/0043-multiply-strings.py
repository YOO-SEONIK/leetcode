class Solution:
    def pow(self, n):
        result = 1
        for i in range(1,n):
            result = result * 10
        return result


    def multiply(self, num1: str, num2: str) -> str:
        sum = 0
        for i in range(len(num1)-1,-1,-1):  # 스트링길이가 3이라면 i는 2부터 거꾸로 2,1,0
            for j in range(len(num2)-1,-1,-1):
                numberPosition1 = self.pow(len(num2)-j)  # 자리 수 구하기
                numberPosition2 = self.pow(len(num1)-i)  # 자리 수 구하기
                sum += (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))*numberPosition1*numberPosition2
        return str(sum)
        