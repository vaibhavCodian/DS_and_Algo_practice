# class Solution(object):
#    def twoSum(self, nums, target):
#       """
#       :type nums: List[int]
#       :type target: int
#       :rtype: List[int]
#       """
#       required = {}
#       for i in range(len(nums)):
#          if target - nums[i] in required:
#             return [required[target - nums[i]],i]
#          else:
#             required[nums[i]]=i
# input_list = [2,8,12,15]
# ob1 = Solution()
# print(ob1.twoSum(input_list, 20))

class Solution(object):
    def twoSum(self, nums, target):
        required = {}
        for i in range(len(nums)):
            print(i, required, target - nums[i])
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]]=i

arr = [2,8,12,15]
sl = Solution()
print(sl.twoSum(arr, 20))