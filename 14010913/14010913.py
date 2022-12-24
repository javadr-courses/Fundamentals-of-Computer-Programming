#!/usr/bin/env python
# coding: utf-8

# # Introduction to Progamming Languages with Python 
# ### University of Qom
# ##### Sun. 1401/09/13

# # Chapter 10 : Lists

# In[3]:


def x2(x):
    return x*x

l = [1,2,3,4,5,6,7]

# for i in map(x2, l):
#     print(i)

print(list(map(x2, l)))


# In[4]:


# Mapping نگاشت
l = [1,2,3,4,5,6,7]
newl = []

for item in l:
    newl.append(item**2)

newl


# In[13]:


m = map(x2, l)
for i in m:
    print(i, end=', ')
    
print(list(m))


# In[14]:


get_ipython().run_cell_magic('time', '', 'range(100_000_000)')


# In[3]:


get_ipython().run_cell_magic('time', '', '# list(range(10_000_000))')


# In[5]:


get_ipython().run_cell_magic('time', '', 'def f(x):\n    return x**2\n\nmap(f, range(10_000_000_000))')


# In[9]:


# filtering 

l = list(range(10))
even = []
for i in l:
    if i%2==0:
#         even.append(i)
#         even = even + [i]
        even += [i]
even


# In[11]:


# reduction

l = list(range(1,101))
summation = 0
for i in l:
    summation += i
summation


# In[13]:


l = list(range(1,101))
sum(l), min(l), max(l)


# In[16]:


l = [134,45,34,36,6,7,8]
last = l.pop()
print(l, last)


# In[19]:


l = [134,45,34,36,6,7,8]
for _ in range(len(l)):
    print(l.pop(), end=', ')
print(l)


# In[20]:


l = [134,45,34,36,6,7,8]
print(l.pop(4))
print(l)


# In[22]:


l = [134,45,34,36,6,7,8]
l.insert(3, 123)
l


# In[25]:


l = [134,45,34,36,6,7,8]
l.insert(3, [1,2,3])
l


# In[24]:


l = [134,45,34,36,6,7,8]
l[3:3] = [123]
l


# In[26]:


l = [134,45,34,36,6,7,8]
l[3:3] = [1,2,3]
l


# In[28]:


l = [134,6,34,36,6,7,8,6]

l.remove(6)

ll = [134,45,34,36,6,7,8]
l[3:4] = []
l


# In[29]:


l = [134,45,34,36,6,7,8]
l[3:4] = []
l


# In[31]:


l = [134,45,34,36,6,7,8]
l[1:7:2] = ['hi', 'hello', 'hallu']
l


# In[32]:


l = [134,45,34,36,6,7,8]
l[3:7] = []
l


# In[34]:


l = [134,45,34,36,6,7,8]
l[3:7] = [3]
l


# In[35]:


l = [134,45,34,36,6,7,8]
l[3] = []
l


# In[36]:


l = [134,45,34,36,6,7,8]
del l[4]
l


# In[37]:


l = [134,45,34,36,6,7,8]
n = l.pop(4)
l, n


# In[38]:


l = [134,45,34,36,6,7,8]
n = del l[4]
l, n


# In[52]:


n = 2987987987
print(id(n))


# In[53]:


l = [134,45,34,36,6,7,8]
print(id(l))
del l[4]
print(id(l))


# In[54]:


l = [134,45,34,36,6,7,8]
print(id(l))
l[4:4] = []
print(id(l))


# In[55]:


l = [134,45,34,36,6,7,8]
print(id(l))
l.pop()
print(id(l))


# In[58]:


a = 'hi'
b = 'hi'

print(id(a), id(b), sep='\n')

b = 'hello'
print(id(a), id(b), sep='\n')


# In[59]:


a = [1,2]
b = [1,2]

print(id(a), id(b), sep='\n')

b[0] = 4
print(id(a), id(b), sep='\n')


# In[60]:


n = 8798798798
print(id(n))
n = n + 1 
print(id(n))


# In[61]:


n = 8798798798
print(id(n))
n += 1 
print(id(n))


# In[62]:


n = [1,2]
print(id(n))
n = n + [3] 
print(id(n))


# In[63]:


n = [1,2]
print(id(n))
n += [3] 
print(id(n))


# In[64]:


#https://quera.org/course/assignments/47926/problems/160762

line1 = '4'
line2 = '47 -11 26 15'

for i in map(int, line2.split()):
    if i<15: 
        print('heater')
    else:
        print('cooler')


# In[ ]:


#https://quera.org/course/assignments/47926/problems/160762

line1 = '4'
line2 = '47 -11 26 15'

for i in line2.split():
    i = int(i)
    if i<15: 
        print('heater')
    else:
        print('cooler')


# In[65]:


'ali' < 'zahra'


# In[67]:


'ali' < 'Zahra'


# In[68]:


'25' < '5'


# In[83]:


def onsify(n):
    if n%2==0 or n%5==0:
        return -1
    if n==1: return 1
    
    ones = 11
    while ones%n!=0:
        ones = ones*10 + 1
    
    return ones//n

len(str(onsify(16479)))
# onsify(2)


# In[86]:


def f(n):
    return n, n**2, n**3, n**4, n**5, n**6

for i in range(10):
    print(i, f(i))


# In[87]:


for i in range(1000000):
    if i%10 in [5,6]:
        if str(i**2).endswith(str(i)):
            print(i, i**2)
    

