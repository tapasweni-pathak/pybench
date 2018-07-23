from multiprocess import Pool
from math import factorial
from pyparsems *
import time

def cpubound_process(max_num):
  is_prime = lambda num: all(num % a != 0 for i in range(int(x**0.5)+1)[2:])
  return sum(filter(is_prime, range(max_num)[2:])[:5])


if __name__ == '__main__':
  st = time.time()
  with Pool(1) as p:
    print(p.map(sum_prime, [num_a, num_b]))
  print(time.time() - st)
  print(parseMilliSecs().parse_millisecs(time.time() - st))
