#!/usr/bin/env python
# coding: utf-8

# # Introduction to Progamming Languages with Python 
# ### University of Qom
# ##### Sat. 1401/08/22

# ### Iteration ---> LOOPs

# In[4]:


x,y,z = map(int, input().split())
print(x,y,z)


# In[8]:


f = input()
int(float(f))


# In[11]:


n = 4
for i in range(n):
    print('hi')


# In[12]:


n = 4
for i in range(n):
    print(i)


# In[14]:


n = 4
for i in range(n):
    print(i, end=' ')


# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 - 2

x = np.arange(-3, 3, .1)
plt.plot(x, f(x))
plt.plot([-3,  3], [0,0])


# In[38]:


def f(x):
    return x**2 - 2

def fp(x):
    return 2*x


x = 9*10**9

for i in range(100):
    x = x - f(x)/fp(x)

print(x, 2**.5, x-2**.5, sep='\n')


# In[41]:


i = 0
while i<10:
    print(i)
    i = i+1


# In[42]:


n = int(input('> '))

while not 1<=n<=12:
    n = int(input('> '))
    


# In[43]:


while True:
    n = int(input('> '))
    if 1<=n<=12:
        break
    


# In[45]:


for i in range(10000000):
    
    if i>10:
        break
    print(i)


# In[46]:


for i in range(100):
    if i%2: # i%2==1
        print(i, end=' ')


# In[47]:


for i in range(1, 100, 2):
    print(i, end=' ')


# In[52]:


for i in range(100):
    if i%2==0:
        continue
    print(i, end=' ')


# In[53]:


n = 10
while n>0:
    print(n)
    n = n -1


# In[55]:


def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
        
    return f

fact(5)


# In[57]:


def fact(n):
    f = 1
    i = 1
    while i<=n:
        f = f*i
        i = i+1
    return f

fact(5)


# In[71]:


get_ipython().run_cell_magic('time', '', 'def fib(n):\n    f0 = 0\n    f1 = 1\n    for i in range(1,n):\n        f2 = f1+f0\n        f0 = f1\n        f1 = f2\n    return f2\n\nfib(5000)\n        ')


# In[85]:


get_ipython().run_cell_magic('time', '', 'def fibR(n):\n    if n<=1:\n        return n\n    return fibR(n-1)+fibR(n-2)\n\n\nfibR(30)')


# In[79]:


get_ipython().run_cell_magic('time', '', 'def fib(n):\n    f0 = 0\n    f1 = 1\n#     if n<=1: \n#         return n \n    f2 = n\n    \n    i = 1\n    while i<n:\n        f2 = f1+f0\n        f0 = f1\n        f1 = f2\n        i = i+1\n    return f2\n\nfib(0)')

