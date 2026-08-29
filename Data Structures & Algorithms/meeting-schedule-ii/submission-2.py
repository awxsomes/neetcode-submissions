"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        start.sort()
        end = [i.end for i in intervals]
        end.sort()

        # startpointer = 0
        endpointer = 0
        maxcounter = 0
        currcounter = 0
        for startpointer in range(len(start)):
            currcounter += 1
            while start[startpointer] >= end[endpointer]:
                currcounter -= 1
                endpointer += 1
            maxcounter = max(maxcounter, currcounter)
        return maxcounter
        
