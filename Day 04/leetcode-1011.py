#1011. Capacity To Ship Packages Within D Days
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = sum(weights)

        ans = 0
        while low<=high:
            mid = (low + high)//2

            d = 1
            currentWeight = 0

            for i in range(len(weights)):
                if currentWeight + weights[i] <= mid:
                    currentWeight += weights[i]
                else:
                    d+=1
                    currentWeight = weights[i]
            if d>days:
                low = mid+1
            else:
                high = mid-1
             
        return low