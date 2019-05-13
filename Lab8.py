"""
Course CS2302 MW 1:30-2:50pm
Instructor:Fuentes, Olac
Tovar, Brianna
Date of last modification: 4/29/2019
8th Lab
This lab is about using the Backtracking method, all of its phases,
for these select problems.
"""
import random
import numpy as np
from math import *
import time

def equal(f1, f2,tries=1000,tolerance=0.0001): #random algorithm to find how similar
    for i in range(tries):
        x = random.random()
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True 

def subsetsum(S,last,goal):
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last]) # Take S[last]
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]

def edit_distance(s1,s2): #gives distance between both, such as words
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] ==s2[j-1]:
                d[i,j] =d[i-1,j-1]
            else:
                n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                d[i,j] = min(n)+1
    #print(d)          
    return d[-1,-1]
        
#####################
a= 'sin(t)'
b= 'cos(t)'
c= 'tan(t)'
"""
d= 'sec(t)'
"""
e= '-sin(t)'
f= '-cos(t)'
g= '-tan(t)'
h= 'sin(-t)'
i= 'cos(-t)'
j= 'tan(-t)'
k= 'sin(t)/cos(t)'
l= '(2*sin(t/2))*cos(t/2)'
"""
m= 'sin^2*t'
n= '1-(cos^2)*t'
"""
o= '1-(cos(2*t))/2'
p= '1/cos(t)'

List=[a,b,c,e,f,g,h,i,j,k,l,o,p]
t=random.uniform(-math.pi,math.pi)

#Part 1
def RandCompare(L): #will create all combinations of variables to test each is equal
    #for loop to go through characters A thru P
    for i in range(len(L)):
        for j in range(len(L)):#another loop for different variable
            f1=L[i]#setting variable w/ 'i' value
            print(f1,' t is: ',t)
            f2=L[j]
            print(f2,' t is: ',t)#setting variable w/ 'j' value
            print('Are they equal?  ',equal(f1,f2))#check if equal
            
start=time.time()
print(RandCompare(List))
end=time.time()
print('Running time in seconds: ',end-start)

#Part 2
    
Set=[1,2,3,4,5]
    
def Sum(S):#getting the sum
    sum=0
    for n in range(0,len(S)):
        sum+=S[n]
    return sum
    
def solvPartition_Back(S):
    one=set()
    two=set()
    #creating two subsets of S
    while len(S)!=0 and len(S)!=1:#checking to only use actual partitions
        i=len(S)//2
        if sum[0:i]==sum[i:]:#testing if first half of set is equal to second half
            one.append(range(S[0:i]))#appends values if statement is true
            two.append(range(S[i:]))
        return one,two
    print("No partition")
    
"""
solvPartition_Back(Set)
"""