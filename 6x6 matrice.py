# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import numpy as np


def convertXtoInt(x):
    y=0
    for row in range(x.shape[0]):
        for column in range(x.shape[1]):
            y+=x[row,column]
    return (y)


def main():
    a=np.array([[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,0,1,0,0]])
    b=np.array([[0,1,0],[0,1,0],[0,1,0]])
    c=np.zeros((6,6))
    for row in range(c.shape[0]):
        for column in range(c.shape[1]):
            x=a[row:row+3,column:column+3]*b
            x=convertXtoInt(x)
            c[row,column]=x
    print(c)
    
    
            
    
if __name__=='__main__':
    main()