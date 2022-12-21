#!/usr/bin/env python
# coding: utf-8

# In[4]:


m = 2
n = 3
o = 4
min(m,n,o), max(m,n,o), m+n+o


# In[5]:


abs(-3)


# In[2]:


import turtle
turtle


# In[3]:


bob = turtle.Turtle()


# In[4]:


help(bob)


# In[ ]:


import turtle

bob = turtle.Turtle()
# bob.speed(0)

bob.fd(100) # bob.forward(100)
bob.rt(60)
bob.fd(100) # bob.forward(100)
bob.rt(60)
bob.fd(100) # bob.forward(100)
bob.rt(60)
bob.fd(100) # bob.forward(100)
bob.rt(60)
bob.fd(100) # bob.forward(100)
bob.rt(60)
bob.fd(100) # bob.forward(100)
bob.rt(60)
 
turtle.mainloop()


# In[16]:


for booq in range(4):
    print('hi students!')


# In[ ]:


import turtle

bob = turtle.Turtle()
# bob.speed(0)

for i in range(6):
    bob.fd(100) # bob.forward(100)
    bob.rt(60)
 
turtle.mainloop()
    


# In[ ]:


import turtle

bob = turtle.Turtle()
bob.speed(0)

def n_angle(n):
    for i in range(n):
        r = 180 - (n-2)*180/n
        bob.fd(100) # bob.forward(100)
        bob.rt(r)

n_angle(10)

turtle.mainloop()


# In[ ]:


import turtle

bob = turtle.Turtle()
bob.speed(0)

def n_angle(t, n, length):
    for i in range(n):
        r = 180 - (n-2)*180/n
        t.fd(length) # bob.forward(100)
        t.rt(r)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

n_angle(bob, 10, 100)
square(bob, 100)

turtle.mainloop()


# In[ ]:


import turtle

bob = turtle.Turtle()
bob.speed(0)

def n_angle(t, n, length=200):
    for i in range(n):
        r = 180 - (n-2)*180/n
        t.fd(length) # bob.forward(100)
        t.rt(r)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

n_angle(bob, 10)

square(bob, 100)

turtle.mainloop()


# In[ ]:


import turtle
import math

bob = turtle.Turtle()
bob.speed(0)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

circle(bob, 200)

turtle.mainloop()


# In[ ]:


import turtle
import math

bob = turtle.Turtle()
bob.speed(0)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r, x=0, y=0):
    t.penup()
    t.fd(x)
    t.lt(90)
    t.fd(y-r)
    t.pendown()
    t.rt(90)
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

circle(bob, 100, 200, -100)

turtle.mainloop()


# In[ ]:


import turtle
import math

bob = turtle.Turtle()
bob.speed(0)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(bob, 100, 40)

turtle.mainloop()


# In[17]:


def doc_test():
    """
    Hi, This is my 
    first docstring in Python.
    """
    print()
    
    
help(doc_test)


# In[20]:


import math
help(math.sin)


# In[ ]:


def area(r):
    """
    Return the area of given circle
    r is the radius of a cricle 
    """
    return math.pi * r*r 


# In[ ]:


import turtle
import math

bob = turtle.Turtle()
bob.speed(0)

def rectangle(t, w, h):
    for i in range(2):
        t.fd(w)
        t.lt(90)
        t.fd(h)
        t.lt(90)

for i in range(100):
    rectangle(bob, 70, 50)
    bob.fd(10)
    bob.lt(5)
    

turtle.mainloop()


# In[ ]:


import turtle
import math

bob = turtle.Turtle()
bob.speed(0)
bob.shape('turtle')

def rectangle(t, w, h):
    for i in range(2):
        t.fd(w)
        t.lt(90)
        t.fd(h)
        t.lt(90)

n = 20
for i in range(40):
    bob.circle(n)
    n = n + 3
    #bob.fd(10)
    #bob.lt(5)
n = 20
bob.lt(180)
for i in range(40):
    bob.circle(n)
    n = n + 3
    

turtle.mainloop()

