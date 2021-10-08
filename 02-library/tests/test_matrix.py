#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:54:44 2021

@author: chenzhechao
"""

from cs506 import matrix
import numpy as np

test1=[[1,2,3],
       [2,3,4],
       [4,5,6]]
print("test1 is: ", (str)(test1))
print("the result of the test case is: ", (str)(matrix.get_determinant(test1)))
print("the true result is: ",(str)(np.linalg.det(np.array(test1))))


test2=[[1,2,3,4],
       [2,3,4,5],
       [3,4,5,6],
       [4,5,6,7]]
print("test2 is: ", (str)(test2))
print("the result of the test case is: ", (str)(matrix.get_determinant(test2)))
print("the true result is: ",(str)(np.linalg.det(np.array(test2))))

test3=[[1,3,2],
       [4,1,3],
       [2,5,2]]
print("test3 is: ", (str)(test3))
print("the result of the test case is: ", (str)(matrix.get_determinant(test3)))
print("the true result is: ",(str)(np.linalg.det(np.array(test3))))

test4=[[1,3,2,7,3],
       [4,1,3,9,0],
       [2,5,2,1,9],
       [10,3,7,2,1],
       [6,7,8,1,2]]
print("test4 is: ", (str)(test4))
print("the result of the test case is: ", (str)(matrix.get_determinant(test4)))
print("the true result is: ",(str)(np.linalg.det(np.array(test4))))
