import time
start_time = time.time()
import random
def fact(k):
    if(k==1):
        return 1
    return k*fact(k-1)
a=input()
b=len(a)
c=fact(b)
l=[a]
while len(l)<c-1:
    t=""
    e=a
    while len(t)<b:
        m=random.choice(e)
        e=list(e)
        e.remove(m)
        e=''.join(e)
        if m not in t:
            t+=m
    if t not in l:
        l.append(t)
print(l)
'''
# Python code to demonstrate  
# to find all permutation of 
# a given string 
  
# Initialising string 
ini_str = "abc"
  
# Printing initial string 
print("Initial string", ini_str) 
  
# Finding all permuatation 
result = [] 
  
def permute(data, i, length):  
    if i == length:  
        result.append(''.join(data) ) 
    else:  
        for j in range(i, length):  
            # swap 
            data[i], data[j] = data[j], data[i]  
            permute(data, i + 1, length)  
            data[i], data[j] = data[j], data[i]   
permute(list(ini_str), 0, len(ini_str)) 
  
# Printing result 
print("Resultant permutations", str(result))
'''
print("--- %s seconds ---" % (time.time() - start_time))
