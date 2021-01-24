def harmonic(x):
  if x >1:
    return 1/x + harmonic(x-1)
  else:
    return 1/x
print(harmonic(5))