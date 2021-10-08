#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:55:55 2021

@author: chenzhechao
"""
import copy

def get_determinant(matrix):
    for row in matrix:
        if len(matrix)!=len(row):
            return ValueError("It is not square matrix")
    if len(matrix)==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    res=0
    for column in range(len(matrix[0])):
        next=copy.deepcopy(matrix[1:])
        for i in next:
            del i[column]
        if column%2==0:    
            res+=matrix[0][column]* (get_determinant(next))
        else:
            res-=matrix[0][column]* (get_determinant(next))
    return res


    