#!/usr/bin/env python
# coding: utf-8

# # Introduction to Progamming Languages with Python 
# ### University of Qom
# ##### Sat. 1401/09/26

# # Chapter 13

# In[2]:


import random


# In[3]:


for i in range(10):
    print(random.random())


# In[ ]:





# In[5]:


for i in range(10):
    print(int(random.random()*10))


# In[16]:


import random 
from matplotlib import pyplot as plt

l = [0]*10
for i in range(10**6):
    idx = int(random.random()*10)
    l[idx] += 1

l
    


# In[17]:


import random 
from matplotlib import pyplot as plt

l = []
for i in range(10**6):
    l.append(random.random())

plt.hist(l, bins=10)
    


# In[19]:


def rand_range(a,b):
    return int((b-a)*random.random()) + a

for i in range(10):
    print(rand_range(1,6+1))


# In[23]:


from matplotlib import pyplot as plt

def abed_range():
    return int(10*random.random())%7

l = []
for i in range(10**6):
    l.append(abed_range())

plt.hist(l, bins=6)


# In[25]:


for i in range(10):
    print(random.randint(1,7))


# In[27]:


names = ['ali', 'javad', 'hassan', 'alireza', 'hosein', 'amir']

for i in range(10):
    print(random.choice(names))


# In[37]:


dict = {'ali':'javad', 'hassan':'alireza', 'hosein':'amir'}

for i in range(10):
    print(random.choice(tuple(dict.keys())))


# In[43]:


from matplotlib import pyplot as plt

words = open('words.txt').read().replace('\n','')
dict = {}
for char in words:
    dict[char] = dict.get(char, 0)+1

freq = sorted(dict.items())
letters, frequencies = [], []
for l, f in freq:
    letters.append(l)
    frequencies.append(f)
    
plt.plot(letters, frequencies)


# In[47]:


from matplotlib import pyplot as plt
import string


words = open('words.txt').read().replace('\n','')
dict = {}
for char in words:
    dict[char] = dict.get(char, 0)+1

freq = sorted(dict.items())
frequencies = []
for l, f in freq:
    frequencies.append(f)
    
plt.plot(list(string.ascii_uppercase), frequencies)


# In[52]:


def test(a, b=2, c=4):
    print(a*b*c)
    
test(1,3,5)
test(1,3)
test(1)
test(1, c=9)
test(1, c=9, b=3)
test(c=9, b=3, a=1)


# In[63]:


import pysnooper


l = [1,2,3, [4,5, [7,8, [10, 11, 12], 9]], 10]

@pysnooper.snoop()
def rec_sum(l):
    s = 0
    for item in l:
        if isinstance(item, (int, float)):
            s += item 
        else:
            s += rec_sum(item)
#         print(s, l)
    return s

rec_sum(l)
        


# In[67]:


from math import log

digits = '0123456789ABCDEF'
ten2base = lambda n, base: (digits[n%base]+''.join([digits[(n:=n//base)%base] for _ in range(int(log(n,base)))]))[::-1]

print(ten2base(*map(int, input().split())))


# In[73]:


digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 3
b = 5
new = ''
while n!=0:
    n, r = n//b, n%b
    new = digits[r] + new

new


# In[ ]:




