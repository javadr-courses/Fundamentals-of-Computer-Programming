#!/usr/bin/env python
# coding: utf-8

# # Saturday 14010807
# 

# In[1]:


type(32)


# In[3]:


t = type(32.3)
print(t)


# In[4]:


output = print(1)


# In[5]:


type(output)


# In[6]:


type(help(type))


# In[7]:


int('32a')


# In[9]:


bin(345), bin(-345)


# In[10]:


oct(345)


# In[11]:


hex(345)


# In[12]:


help(int)


# In[13]:


int('32a', 16)


# In[14]:


int('32a', 100)


# In[16]:


import math
math


# In[17]:


help(math)


# In[18]:


math.sin(30)


# In[19]:


math.pi


# In[20]:


math.sin(math.pi/6)


# In[21]:


math.sin


# In[22]:


def print_twice():
    print()
    print()
    
print_twice()


# In[23]:


def print_twice(s):
    print(s)
    print(s)
    
print_twice('hi students!')


# In[24]:


def add(m,n):
    print(m+n)
    
add(3,4)


# In[25]:


o = add(3,4)
print(o)


# In[28]:


def add(m,n):
    summation = m+n
    return summation

output = add(3,4)
print(output*2)


# In[33]:


# fruitful function

def area(r):
    return 3.14 * r * r

def cylinder_volume(h, r):
    a = area(r)
    return h * a

print(cylinder_volume(10,12))


# In[35]:


from  math import pi, e, sin, tan

sin(pi)


# In[37]:


from math import *

tan(pi)

