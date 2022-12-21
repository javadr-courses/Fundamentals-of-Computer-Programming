#!/usr/bin/env python
# coding: utf-8

# # Introduction to Progamming Languages with Python 
# ### University of Qom
# ##### Sun. 1401/09/06

# ### Problem Solving

# In[13]:


import math

def pi(n):
    p = 0
    sign = 1
    for i in range(n):
        p = p + sign * 1/(2*i+1)
        sign = sign * -1
        
    return p*4

print(pi(10000000), math.pi, sep='\n')


# In[14]:


.1+.1+.1


# In[15]:


.1+.1+.1==.3


# In[17]:


(.1+.1+.1 -.3)<.0000001


# In[18]:


.1+.1+.1 == 0.30000000000000004


# In[21]:


3e-1 == 1e-1 + 1e-1 + 1e-1


# In[22]:


def sum_digit(n):
    s = 0
    while n!=0:
        s = s + n%10
        n = n//10
    return s

sum_digit(8768768768768768)
        


# In[41]:


get_ipython().run_cell_magic('time', '', '\ndef one_digitizer(n):\n    while n>=10:\n        n = sum_digit(n)\n    return n\n\none_digitizer(9**9999)')


# In[42]:


get_ipython().run_cell_magic('time', '', '\ndef mehrpooya(n):\n    while n >= 10:\n        n = (n % 10) + (n // 10)\n    return n\n\nmehrpooya(9**9999)')


# In[43]:


def rev_num(n):
    new_num = 0
    i = 0
    while n!=0:
        new_num = new_num*10 + n%10
        n = n//10
    return new_num

rev_num(87875623513123)

