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

