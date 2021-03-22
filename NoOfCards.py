#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 12:18:58 2021

@author: samac
"""

def CardsPyramid(n):
    cards=0
    level=0
    
#we must return -1 if the level specified is 0     
    if(n==0):
        return -1
    
#condition for levels other than 0    
    else:
        for i in range(1,n+1):
            
            #this would store No of cards in each level
            cards=cards+(i*2) 
            
            #this would store the no of cards to support the pyramid i.e. cards in between two rows
            level=level+(i-1)
            
        #adding all the cards to get total number of cards   
        NoOfCards=cards+level
        
        
        return(NoOfCards%1000007)
    
#taking input from user    
n=int(input())

#passing the value to function CardsPyramid and printing it
print(CardsPyramid(n))
