#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


12 // 5


# In[2]:


12. // 5


# In[3]:


int(12. // 5)


# In[8]:


22 % 5 # 22 - (22//5)*5


# In[7]:


22 - (22//5)*5


# In[9]:


5 == 10//2


# In[11]:


.1 + .1 + .1  == .3


# In[14]:


.1 + .1 + .1  - .3 < 10**-6 # 1e-6


# In[19]:


print(1e-5+.2)


# In[20]:


12 > 4


# In[21]:


12 < True


# In[22]:


12 + True


# In[23]:


1 == True


# In[27]:


x = int(input())
if x > 0:
    print('x is positive')


# In[28]:


def area(r):
    pass


# In[29]:


def test():


# In[30]:


m = int(input())

if m==1:
    print('farvardin')
else:
    if m==2:
        print('ordibehest')
    else:
        if m==3:
            print('khordad')
        else:
            pass


# In[31]:


m = int(input())

if m==1:
    print('farvardin')
elif m==2:
    print('ordibehest')
elif m==3:
    print('khordad')
else:
    pass


# In[1]:


x = int(input())
if 0 < x:
    if x <= 12:
        print('Month number is between 1 and 12')


# In[2]:


x = int(input())
if 0 < x and x <= 12:
        print('Month number should be between 1 and 12')


# In[3]:


x = int(input())
if 0 < x < 13:
        print('Month number should be between 1 and 12')


# In[39]:


def area(r):
    return 3.14*r*r

def volume(h, r):
    return h * area(r)

volume(1,1)


# In[41]:


def test(i):
    print(i)
    test(i+1)
    
test(1)


# In[43]:


def countdown(n):
    if n==0:
        return 
    print(n)
    countdown(n-1)
    
    
countdown(5)


# In[44]:


def fact(n):
    if n==0:
        return 1
    alpha = fact(n-1)
    return n*alpha

fact(5)


# In[46]:


def fact(n, d):
    print('{}{} factorial is called!'.format(d*'  ', n))
    if n==0:
        return 1
    alpha = fact(n-1, d+1)
    return n*alpha

fact(5, 0)


# In[54]:


def fact(n, d=0):
    if n==0:
        return 1
    print('{}{} * factorial({})'.format(d*'  ', n, n-1))
    #print('%s %d * factorial(%d)' % (d*'  ', n, n-1))
    #print(d*'  ', n, ' * factorial(' , n-1, ')', sep='')
    alpha = fact(n-1, d+1)
    return n*alpha

fact(5)

