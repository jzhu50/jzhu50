def string_times(str, n):
  return(str * n)

def front_times(str, n):
  deliverable = str
  if(len(str)>=3):
    deliverable = deliverable[:3]
  deliverable *= n
  return deliverable

def string_bits(str):
  deliverable = ""
  for i in range(len(str)):
    if i % 2 == 0:
      deliverable += str[i]
  return deliverable

def string_splosion(str):
  deliverables = ''
  if(len(str)>0):
    for i in range(len(str)+1):
      deliverables += str[:i]
  return deliverables

def last2(str):
  string = str[-2:]
  times = 0
  if(len(str)>2):
    for i in range(len(str)-2):
      if(string == str[i:i+2]):
        times += 1
  return times

def array_count9(nums):
  times = 0
  for i in nums:
    if (i==9):
      times += 1
  return times

def array_front9(nums):
  if(len(nums)>=4):
    for i in range(4):
     if(nums[i]==9):
       return True
  else:
    for i in range(len(nums)):
      if(nums[i]==9):
        return True
  return False

def array123(nums):
  for i in range(len(nums)-2):
    if(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
      return True
  return False

def string_match(a, b):
  times = 0
  string = ''
  for i in range(len(a)-1):
    if(a[i:i+2] == b[i:i+2]):
      times += 1
  return times

