class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) idea: check if the difference exist
        # within the nums using a map
        map = dict()
        for i in range(len(nums)):
            # check if the difference is already
            # in the map
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            # if we cannot find,
            # map the current number to its index
            map[nums[i]] = i
        return
