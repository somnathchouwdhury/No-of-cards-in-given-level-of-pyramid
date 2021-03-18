# No-of-cards-in-given-level-of-pyramid
This program shows how to find number of cards in the specified level by the user in a pyramid of cards

the formulae used here is as follows



for i in range(1,n+1):
            cards=cards+(i*2).......................(1)
            level=level+(i-1).......................(2)
            
        NoOfCards=cards+level
        return(NoOfCards%1000007)
        
This formulae can also be simplified by combining the stetements (1) & (2)
cards=cards+(i*2)+(i-1)
     =cards + 3i -1...................................(since cards and level both were used to store previous valuse therefore they can be merged)
