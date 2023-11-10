# def max_value (nums):
#   max_num = nums[0]

#   if len(nums) > 1:
#     next_max_num = max_value(nums[1:])

#     max_num = next_max_num if next_max_num > max_num else max_num
    
#   return max_num

# print(max_value([7,9,12,-2,-22,23]))

def min_value (nums):
  min = nums[0]

  if len(nums) > 1:
    next_min = min_value(nums[1:])
    min = next_min if next_min < min else min

  return min

print(min_value([7,9,12,-2,-22,23]))
