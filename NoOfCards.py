#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 12:18:58 2021

@author: samac
"""

def CardsPyramid(n):
    cards=0
    level=0
    
    
    if(n==0):
        return -1
    
    
    else:
        for i in range(1,n+1):
            cards=cards+(i*2)
            level=level+(i-1)
            
        NoOfCards=cards+level
        return(NoOfCards%1000007)
    
    
n=int(input())
print(CardsPyramid(n))