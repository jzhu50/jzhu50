def count_evens(nums):
  times = 0
  for i in nums:
    if i % 2 == 0:
      times += 1
  return times

def big_diff(nums):
  return max(nums) - min(nums)
    
'sum(array) sums numbers in a list'

def centered_average(nums):
  max_value = max(nums)
  min_value = min(nums)
  nums.remove(min_value)
  nums.remove(max_value)
  average = sum(nums)/len(nums)
  return average

def sum13(nums):
  total = 0
  i = 0
  while i < len(nums):
    if nums[i] == 13:
      i += 2 'skip the element right after it'
    else:         
     total += nums[i]
     i += 1
  return total

def sum67(nums):
  deliverable = 0
  ignore = False
  for i in nums:
    if i == 6:
      ignore = True
    if not ignore:
      deliverable += i
    if i == 7 and ignore:
      ignore = False
  return deliverable

def has22(nums):
  hasTwos = False
  for i in range(len(nums)-1):
    if i != 0:
      if nums[i] == 2 and (nums[i+1] == 2 or nums[i-1] == 2):
        hasTwos = True
    else:
      if nums[i] == 2 and nums[i+1] == 2:
        hasTwos = True
  return hasTwos