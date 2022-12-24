#!/usr/bin/env python
# coding: utf-8

# # Introduction to Progamming Languages with Python 
# ### University of Qom
# ##### Sun. 1401/09/27

# # Quiz: Compute lcd and gcd of two numbers

# In[7]:


m, n = 72, 14

def get_divisors(n):
    l = []
    for i in range(1, n+1):
        if n%i==0:
            l.append(i)
    return l

lm = get_divisors(m)
ln = get_divisors(n)

c = []
for i in lm:
    for j in ln:
        if i==j:
            c.append(i)
        
print(lm, ln, c)
gcd = max(c) # c[-1]
lcd = m*n//gcd

print(gcd, lcd)


# In[8]:


m, n = 72, 14

def get_divisors(n):
    l = []
    for i in range(1, n+1):
        if n%i==0:
            l.append(i)
    return l

lm = get_divisors(m)
ln = get_divisors(n)

c = []
for i in lm:
    if i in ln:
        c.append(i)
        
print(lm, ln, c)
gcd = max(c) # c[-1]
lcd = m*n//gcd

print(gcd, lcd)


# In[9]:


m, n = 72, 14

def get_divisors(n):
    l = []
    for i in range(1, int(n//2)+1):
        if n%i==0:
            l.append(i)
    return l+[n]

lm = get_divisors(m)
ln = get_divisors(n)

c = []
for i in lm:
    if i in ln:
        c.append(i)
        
print(lm, ln, c)
gcd = max(c) # c[-1]
lcd = m*n//gcd

print(gcd, lcd)


# In[18]:


# Euclidean Algorithm
m,n=72, 14

def gcd(m,n):
    while n!=0:
        m,n = n, m%n
    return m

gcd(14, 72)


# In[19]:


def gcd(m,n):
    if n==0:
        return m
    return gcd(n, m%n)

gcd(72, 14)


# In[21]:


m = 72
l = [0,1]+[0] * 10
i = 2
while m!=1:
    if m%i==0:
        l[i] += 1
        m //= i
    else:
        i += 1

l


# In[22]:


m = 72
d = {}
i = 2
while m!=1:
    if m%i==0:
        d[i] = d.get(i, 0)+1
        m //= i
    else:
        i += 1

d


# In[29]:


m, n = 72, 14
def get_prime_factors(m):
    d = {}
    i = 2
    while m!=1:
        if m%i==0:
            d[i] = d.get(i, 0)+1
            m //= i
        else:
            i += 1
    return d

def gcd(m,n):
    dm, dn = map(get_prime_factors, (m,n))

    gcd = 1
    for key in dm:
        if key in dn:
             gcd *= key**(min(dm[key], dn[key]))

    return gcd

gcd(m,n)


# In[42]:


get_ipython().run_cell_magic('time', '', "def get_divisors(n):\n    l = []\n    for i in range(1, int(n//2)+1):\n        if n%i==0:\n            l.append(i)\n    return l+[n]\n\ndef is_prime(n):\n    l = get_divisors(n)\n    return len(l)==2\n        \n# for i in range(1000):\n#     if is_prime(i):\n#         print(i, end=', ')\nl = []\nfor i in range(10000):\n    if is_prime(i):\n        l.append(i)")


# In[40]:


get_ipython().run_cell_magic('time', '', 'def is_prime(n):\n    if n<2: return False\n    if n==2: return True\n    for i in range(3, n, 2):\n        if n%i==0:\n            return False\n    return True\n        \nl = []\nfor i in range(10000):\n    if is_prime(i):\n        l.append(i)')


# ## Finding prime numbers 

# In[96]:


get_ipython().run_cell_magic('time', '', 'def is_prime(n):\n    if n<2: return False\n    if n==2: return True\n    for i in range(3, int(n//2)+1, 2):\n        if n%i==0:\n            return False\n    return True\n        \nl = []\nfor i in range(100000):\n    if is_prime(i):\n        l.append(i)')


# In[91]:


get_ipython().run_cell_magic('time', '', 'def is_prime(n):\n    if n<2: return False\n    if n==2: return True\n    for i in range(3, int(n**.5)+1, 2):\n        if n%i==0:\n            return False\n    return True\n        \nl = []\nfor i in range(1000000):\n    if is_prime(i):\n        l.append(i)')


# In[51]:


l  = ['ali' ,'hassan', 'hosein']
for i, name in enumerate(l):
    print(i, name)
    
for i in enumerate(l):
    print(i)


# In[90]:


get_ipython().run_cell_magic('time', '', 'n = 1000000\nall_nums = [False,False] + [True]*(n-2) # 0,1,2,3,4,5, .... , 100\nfor i in range(2, n):\n    if all_nums[i]==True:\n        for j in range(i+i, n, i):\n            all_nums[j] = False\n    \nprimes = []\nfor i, num in enumerate(all_nums):\n    if num==True:\n        primes.append(i)')


# In[89]:


get_ipython().run_cell_magic('time', '', 'n = 1000000\nall_nums = [False,False] + [True]*(n-1) # 0,1,2,3,4,5, .... , 100\nfor i in range(2, n):\n    if all_nums[i]==True:\n        all_nums[i+i::i] = [False]*(int((n-i)//i))\n    \nprimes = []\nfor i, num in enumerate(all_nums):\n    if num==True:\n        primes.append(i)')


# In[98]:


get_ipython().run_cell_magic('time', '', 'n = 1000000\nall_nums = [False,False] + [True]*(n-1) # 0,1,2,3,4,5, .... , 100\nall_nums[2::2] = [False]*int(n//2)\nfor i in range(3, n, 2):\n    if all_nums[i]==True:\n        all_nums[i*i::i] = [False]*(int((n-(i*i)+i)//i))\n    \nprimes = []\nfor i, num in enumerate(all_nums):\n    if num==True:\n        primes.append(i)')


# In[ ]:




