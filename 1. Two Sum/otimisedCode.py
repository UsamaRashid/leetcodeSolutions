class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # creating a hashmap
        hashmap = {}
        for i in range(len(nums)):
            valToSearch = target - nums[i]
            if hashmap.get(valToSearch) is not None:
                return [hashmap[valToSearch], i]
            hashmap[nums[i]] = i
        return []

    # explanation on : https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATzf
