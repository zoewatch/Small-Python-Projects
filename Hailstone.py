#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:21:21 2020

@author: zoewatch
"""

def hailstone (a):
    b = 0
    while a > 1:
        if a % 2 == 0:
            print (a,"is even, so I take half:" , a//2 )
            a = a//2
        else:
            print (a, "is odd, so I make 3n+1:", 3*a+1 )
            a = 3*a+1
        b = b + 1
    print ("The process took", b, "steps to reach 1.")
            
    
if __name__ =="__main__":
    hailstone()
    