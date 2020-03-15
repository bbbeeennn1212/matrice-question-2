# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 02:41:11 2020

@author: UseR
"""


import numpy as np


def convertXtoScalarNUM(x):
    y=0
    for row in range(x.shape[0]):
        for column in range(x.shape[1]):
            y+=x[row,column]
    return (y)

def filterr(a,b):
    res= np.zeros((a.shape[0]-2,a.shape[1]-2))
    for row in range(res.shape[0]):
        for column in range(res.shape[1]):
            x=a[row:row+3,column:column+3]*b
            x=convertXtoScalarNUM(x)
            res[row,column]=x
    return (res)


def main():
    a=np.array([[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0]])
    b=np.array([[0,1,0],[0,1,0],[0,1,0]])
    res=filterr(a,b)
    print(res)
    while res.shape[0]>b.shape[0]:
        res=filterr(res,b)
        print (res)
    
    
    
            
    
if __name__=='__main__':
    main()