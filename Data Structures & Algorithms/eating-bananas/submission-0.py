import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #helper function
        def k_fast_enough(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h
        #at least 1 pile
        #can always finish all piles
        #at least 1 banana in every pile
        #piles = [1,4,3,2] and h = 9 output 2

        #first determine upper bound
        max = 0
        for pile in piles:
            if (pile > max):
                max = pile
        k = max
        #then zero in on minimum
        left = 1
        right = max
        while left < right:
            k = (left+right) // 2
            if k_fast_enough(k):
                right = k
            else:
                left = k + 1
        return right

            
