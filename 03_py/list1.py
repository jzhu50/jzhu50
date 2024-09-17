def first_last6(nums):
  return(nums[0] == 6 or nums[len(nums)-1] == 6)

def same_first_last(nums):
  if len(nums)>=1 and (nums[0] == nums[-1]):
    return True
  else:
    return False

def make_pi():
  return [3,1,4]

def common_end(a, b):
  if len(a)>=1 and len(b)>=1:
    if a[0]==b[0] or a[-1]==b[-1]:
      return True
    else:
      return False
  else:
    return False

def sum3(nums):
  return nums[0]+nums[1]+nums[2]

def rotate_left3(nums):
  return [nums[1]]+[nums[2]]+[nums[0]]

def reverse3(nums):
  return([nums[2],nums[1],nums[0]])

'max() finds the biggest number'
'.append() adds an element to the array'

def max_end3(nums):
  largest = 0
  array = []
  for i in nums:
    largest = nums[0]
    if i > largest:
      largest = nums[2]
  array.append(largest)
  array.append(largest)
  array.append(largest)
  return array

def sum2(nums):
  if len(nums)>=2:
      return nums[0]+nums[1]
  elif 0<len(nums)<2:
      return nums[0]
  elif len(nums)==0:
      return 0
    
def middle_way(a, b):
  array = [a[1], b[1]]
  return array

def make_ends(nums):
  if(len(nums)>=1):
    array = [nums[0],nums[-1]]
  return array

def has23(nums):
  for i in nums:
    if i == 2 or i == 3:
      return True
  return False

