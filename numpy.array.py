# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:02:00 2022

@author: DELL
"""

import numpy as np
 #vectors are one dimentional arrays
 #matrices are two dimentional arrays
 
 my_list = [1,2,3,4,5]
 print(my_list)
 np.array(my_list)
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_matrix)
print(np.array(my_matrix))
print(np.array(my_list))

np.arange(0,10)
np.arange(0,10,3)
np.zeros(10)
np.zeros((10,10))
np.ones((10,10))

#linspace

np.linspace(0,10,3)
np.linspace(0,10,50)

#Eye Mthhod (To creat Identical Matrix)

np.eye(5)

#Random
#rand

np.random.rand(10,10)

#randn
np.random.randn(10)
np.random.randn(10,10)

#randint

np.random.randint(0,5,10)

#arr

arr = np.arange(25)
ranarr = np.random.randint(0,50,10)

arr
ranarr

#reshape
 
arr.reshape(5,5) 
ranarr.reshape(5,2)
ranarr.reshape(2,5)

ranarr.max()
ranarr.min()

#Broadcasting

arr_2d= np.array(([1,2,3],[4,5,6],[7,8,9]))
arr_2d
arr_2d[:2,:2]
arr_2d[1:,1:]

np_2d=np.array(([5,10,15],[20,25,30],[35,40,45],[50,55,60],[65,70,75]))
np_2d
np_2d[[2,3,4]]
np.sin(arr)
np.log(arr)
#Boolean Data Type = Conditional Statements like True & False

arr = array(1,2,3,4,5,6,7,8,9,10)
arr
bool_arr=arr>7


arr=np.arange(0,10)
arr
arr+arr
arr*arr
arr/arr
#nan=not a number
1/arr
arr**2
arr
#sqrt=square root
np.sqrt(arr)
np.exp(arr)

#When a lot of saries with the same index number come together, it is known as a Dataframe.

import pandas as pd
#Groupb
data = {'company':[ 'goog','goog','msft','msft','fb','fb']}

