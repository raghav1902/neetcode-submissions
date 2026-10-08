class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mydict = {}

        for i in range (len(nums)):
            if target - nums[i] in mydict:
                return [mydict[target - nums[i]], i]
            mydict[nums[i]] = i
rel = Solution()
a = rel.twoSum([3,4,5,6],7)
print(a)