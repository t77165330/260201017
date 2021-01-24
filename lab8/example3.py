import random

def get_rand_list():
    b = 0
    e = 10
    N = 5
    return random.sample(range(b,e),N)
a = get_rand_list()
b = get_rand_list()
print(a)
print(b)
def get_overlap(a,b):
  x = ""
  for i in a:
    if i in b:
      x += "," + str(i)
  print(x[1:])
get_overlap(a,b)