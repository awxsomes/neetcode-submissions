class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        for i in range(len(temperatures)-1):
            stack = [temperatures[i]]
            for j in range(i+1, len(temperatures)):

                if stack[0] < temperatures[j]:
                    days.append(len(stack))
                    break
                stack.append(temperatures[j])
            if len(stack) == len(temperatures) - i:
                days.append(0)
            

        days.append(0)
        return days