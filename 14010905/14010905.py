#!/usr/bin/env python
# coding: utf-8

# # Introduction to Progamming Languages with Python 
# ### University of Qom
# ##### Sat. 1401/09/05

# ### Algorithm, Flowchart, Problem Solving 3rd Series

# In[8]:


get_ipython().run_cell_magic('time', '', "\ndef fact(n):\n    f = 1\n    for i in range(2, n+1):\n        f = f*i\n    return f\n\ndef neper(n):\n    e = 0\n    for i in range(n+1):\n        e = e + 1/fact(i)\n    \n    return e\n\n# for i in range(20):\n#     print(i, neper(i), sep='\\t')\nneper(1000)")


# In[25]:


get_ipython().run_cell_magic('time', '', "def fact(n):\n    if n<=1: return 1\n    return n*fact(n-1)\n\ndef neper(n):\n    e = 0\n    for i in range(n+1):\n        e = e + 1/fact(i)\n    \n    return e\n\n# for i in range(20):\n#     print(i, neper(i), sep='\\t')\nneper(1000)")


# In[10]:


get_ipython().run_cell_magic('time', '', "\ndef neper(n):\n    e = 1\n    f = 1\n    for i in range(1, n+1):\n        f = f*i\n        e = e + 1/f\n    \n    return e\n\n# for i in range(20):\n#     print(i, neper(i), sep='\\t')\nneper(100000)")


# In[41]:


def birthday(n):
    year = n//100
    month = n%100
    print("saal:{:02}".format(year))
    print("maah:{:02}".format(month))

birthday(7106)


# In[62]:


def is_complete(n):
    s = 1
    for i in range(2,n//2+1):
        if n%i==0:
            s = s + i
    if s==n:
        return True
    else:
        return False
    
    
is_complete(33550336)
# is_complete(137438691328)


# In[57]:


get_ipython().run_cell_magic('time', '', 'for i in range(2, 10_000):\n    if is_complete(i):\n        print(i)')


# In[54]:


get_ipython().run_cell_magic('time', '', 'def is_complete(n):\n    s = 1\n    d = n\n    for i in range(2,n//2+1):\n        if n%i==0:\n            d = i\n            break\n    \n    for i in range(2,n//d+1):\n        if n%i==0:\n            s = s + i\n    if s==n:\n        return True\n    else:\n        return False\n    \n    \nfor i in range(2, 10_000):\n    if is_complete(i):\n        print(i)')


# In[66]:


def complete(p):
    return 2**(p-1) * (2**p-1)

for i in 2,3,5,7,11,13,17,19,23,29,31,37:
    print(complete(i))


# In[41]:


import matplotlib.pyplot as plt
import numpy as np

weights = np.linspace(50, 110)
heights = np.linspace(1.4, 2)
xx, yy = np.meshgrid(weights, heights)
zz = xx / yy**2

h = plt.contourf(weights, heights, zz)
plt.title('Body Mass Index (BMI)')
plt.xlabel('Weight in KiloGrams')
plt.ylabel('Height in Meters')
plt.colorbar()
plt.show()


print("""
    Underweight:        BMI < 18.5
    Normal     : 18.5 ≤ BMI < 25
    Overweight : 25   ≤ BMI < 30
    Obese      : 30   ≤ BMI
""")

