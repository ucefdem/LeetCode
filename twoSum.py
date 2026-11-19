class SimpleHashMap:
  def __init__(self, size):
    self.buckets = [[] for _ in range(size)]
    
  def _bucket(self, key):
    return self.buckets[hash(key) % len(self.buckets)]
  
  def put(self, key, value):
    bucket = self._bucket(key)
    for pair in bucket:
      if pair[0] == key:
        pair[1] = value
        return
    bucket.append([key, value])
    
  def get(self, key):
    bucket = self._bucket(key)
    for k,v in bucket:
      if k == key: return v
    return None
  
  def remove(self, key):
    bucket = self._bucket(key)
    for i, pair in enumerate(bucket):
      if pair[0] == key:
        del bucket[i]
        return True
    return False

def twoSum(nums, target):
  HashMap = SimpleHashMap(1000)
  for i in range(len(nums)):
    curr = nums[i]
    x = target - curr
    v = HashMap.get(x)
    if v != None: return [i, v]
    HashMap.put(curr, i)
    
print(twoSum([3,19,0,-11,5,8], 13))   
print(twoSum([1,2,3,4,5], 9))   
print(twoSum([1,2,3,4,5], 3))   
print(twoSum([4, 6, 1, 8, 2, 5], 13))   
print(twoSum([3,2,4], 6))   


    