import math
import time

import pantilthat

EPS = 0.000001

while True:    
  X, Y = input().split()
  X = int(X)
  Y = int(Y)


  r = math.sqrt(X ** 2 + Y ** 2) 
  
  alpha = 0
  theta = 0

  alpha = math.atan((Y)/(X+EPS)) * (180/math.acos(-1))  
  if alpha > 0: alpha = min(alpha, 90)
  else: alpha = max(alpha, -90)
  
  theta = 90/(1 - math.log(1/(r+1)) - EPS)
  theta = min(theta, 90)

  print(alpha)
  print(theta)

  pantilthat.pan(alpha)
  pantilthat.tilt(theta)

  
'''
import threading
import time

alpha = 0
theta = 0

def com():
    global alpha
    global theta
    while True:
        alpha, theta = map(int, input().split())

def main():
    global alpha
    global theta

    alpha_now = 0
    theta_now = 90

    thread1 = threading.Thread(target=com)
    thread1.start()

    while True:
        alpha_nxt = alpha
        theta_nxt = theta
        print(str(alpha_now) + ' to ' + str(alpha_nxt))
        print(str(theta_now) + ' to ' + str(theta_nxt))
        time.sleep(10)
        alpha_now = alpha_nxt
        theta_now = theta_nxt

main()
'''
