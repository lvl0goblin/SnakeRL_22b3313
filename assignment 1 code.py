# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 06:54:10 2024

@author: ASHWIN S


-------------------------------------------------------------------------------"""
import numpy as np
        
n = int(input("Enter Number of nodes: "))
M= np.array(list(map(float, input("Enter numbers separated by spaces: ").split())))
M = M.reshape(n,n)
start = int(input("Enter row number of starting node (matrix index): "))
T = int(input("Enter time in seconds: "))
M = np.linalg.matrix_power(M, T)
print(M)
ending_state = int(input("Enter row number of ending node (matrix index): "))
end = M[start]
print(M[start].sum())
print (end)



