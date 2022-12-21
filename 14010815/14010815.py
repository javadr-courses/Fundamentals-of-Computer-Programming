#!/usr/bin/env python
# coding: utf-8

# # Introduction to Programming Languages with Python 
# ### University of Qom
# #### Sunday 1401/08/15
# 

# In[2]:


def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
        
fact(5)
    


# In[3]:


def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
        
fact(5)    


# In[5]:


def fact(n, depth=0):
    if n==0:
        return 1
    
    print("{}{} * factorial({})".format(depth*"  ", n, n-1))
    return n * fact(n-1, depth+1)
        
fact(5)


# In[4]:


0 * 'hi'


# In[9]:


def fact(n, depth=0):
    if n==0:
        return 1
    
    return n * fact(n-1, depth+1)
        
fact(2000)


# In[12]:


def test_stack_depth(n=0):
    print(n, end=', ')
    test_stack_depth(n+1)
    
test_stack_depth()


# In[13]:


# n = input()
# n = int(n)

n = int(input())


# In[16]:


# m, n = input().split()
# m, n = map(int, (m,n))

m, n = map(int, input().split())
print(type(m))


# In[17]:


def test(n):
    return int(n)**2

m, n = map(test, input().split())
print(m,n)


# In[ ]:


# Koch snowflake
# https://en.wikipedia.org/wiki/Koch_snowflake

import turtle
t = turtle.Turtle()
t.speed(0)

def koch(x, d):
    if d==0:
        return

    koch(x, d-1)
    t.fd(x)
    t.lt(60)
    koch(x, d-1)
    t.fd(x)
    t.rt(120)
    koch(x, d-1)
    t.fd(x)
    t.lt(60)
    koch(x, d-1)
    # t.fd(x)

def draw(x, d):
    for i in range(3):
        koch(x/3**d, d)
        t.fd(x/3**d)
        t.rt(120)

# the following is to adjust the picture in the middle of screen.
t.penup()
t.bk(350)
t.lt(90)
t.fd(200)
t.rt(90)
t.pendown()

draw(650, 4)
turtle.mainloop()

