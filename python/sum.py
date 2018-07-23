import random
import time
import sys
from pyparsems import *

def genNums(size):
  nums = []

  for i in range(size):
    nums.append(random.randint(0, 10))

  return nums

def sumList(nums):
  res_sum = sum(nums)

if __name__ == '__main__':
  if len(sys.argv) and sys.argv[1].isdigit():
    n = int(sys.argv[1])
    st = time.time()
    nums = genNums(n)
    res_sum = sumNums(nums)
    et = time.time()

    rt = et - st
    print(res_sum)
    print(rt)
    print(parseMilliSecs().parse_millisecs(rt))
