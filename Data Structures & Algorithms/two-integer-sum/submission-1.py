class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        result = []
        for i in range(len(nums)):
            if target - nums[i] in dict:
                result.append(dict[target - nums[i]])
                result.append(i)
                return result
            dict[nums[i]] = i
        #dict 3: 0
        #dict 4: 1
        #dict 5: 2
        #dict 6: 3
