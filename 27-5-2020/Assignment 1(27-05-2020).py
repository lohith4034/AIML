#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(0,5):
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")


# In[2]:


k=int(input("enter value to show"))
n=int(input('enter range'))
for i in range(1,n):
    print(k,'*',i,'=',k*i)


# In[3]:


n=int(input(''))
f1=0
f2=1
if(n>1):
    for x in range(0,n):
        print(f2,end=',')
        next=f1+f2
        f1=f2
        f2=next

    


# In[4]:


def binary(n):
   if n > 1:
       binary(n//2)
   print(n % 2,end = '')
d = int(input("enter decimal: "))
binary(d)
print()


# In[7]:


from math import sqrt
a=float(input("a=  "))
b=float(input("b=  "))
c=float(input("c=  "))
r=b**2 - 4*a*c
a1 =(((-b) + sqrt(r))/(2*a))     
b1=(((-b) - sqrt(r))/(2*a))
print("the roots are %f and %f",a1,b1)


# In[ ]:




