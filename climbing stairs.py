def climbstairs (n):
  steps=[]
  steps.climb (1),
  steps.climb (2),
  for i in range (2,n):
    steps.climb(f[i-1]+f[i-2])
  return steps [n-1]
n=3
print("climb stairs (n)")
  
  
