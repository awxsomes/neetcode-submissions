class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)

        stack = [] 
        for i in range(len(temperatures)):
            while(stack and temperatures[i] > stack[-1][0]):
                temp, ind = stack.pop()
                days[ind] = i-ind
            stack.append([temperatures[i], i])
        return days