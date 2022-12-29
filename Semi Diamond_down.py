## Pattern Printing 
# *        *
# **      **
# ***    ***
# ****  ****
# **********

# Lince Pattern Printing Solution for Diamond 


#n=5

n= int(input())

for i in range(1,n+1):
    
    
    for j in range(i):
        print("*",end="")
    for a in range(n-i):
        print(" ",end="")
    for a in range(n-i):
        print(" ",end="")
        
    for j in range(i):
        print("*",end="")
    print()

    
