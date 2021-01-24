import time

def timer(x):
  print(x)
  if x > 0:
    time.sleep(1)
    return timer(x-1)
  else:
    return print("TIME IS UP !!!")
x = int(input("Enter the integer to count down: "))
timer(x)
  