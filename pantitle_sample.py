import math
import time

import pantilthat


while True:    
  X, Y = input().split()
  X = int(X)
  Y = int(Y)

  r = math.sqrt((X-1) ** 2 + (Y - 1) ** 2) 
  eps = 0.000001

  alpha = math.atan((Y-1)/(X-1+eps)) * (180/math.acos(-1)) 
  
  theta = 90/(1 - math.log(1/(r+1)) - eps)

  print(alpha)
  print(theta)

  pantilthat.pan(alpha)
  pantilthat.tilt(theta)

  time.sleep(0.005)
