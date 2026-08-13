class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tail, head, best = 0,1,0

        while head < len(prices):
            if(prices[head]>prices[tail]):
                best = max(prices[head]-prices[tail], best)
            else:
                tail=head
            head +=1

        return best