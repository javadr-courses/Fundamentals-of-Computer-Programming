#!/usr/bin/env python
# coding: utf-8

# # Introduction to Progamming Languages with Python 
# ### University of Qom
# ##### Sat. 1401/09/19

# # Chapter 11 : Dictionaries

# In[2]:


mydict = dict()

mydict


# In[3]:


mydict = {}

mydict


# In[4]:


mydict = {}

mydict['name'] = 'ali'
mydict['family'] = 'alavi'
mydict['age'] = 19
mydict[12] = 754

mydict


# In[5]:


mydict[[1,2]] = 'yes'


# In[7]:


mydict[12.2] = 'hi'
mydict


# In[9]:


mydict = {1:12.2, 'name':'ali', 'age':12}
mydict


# In[10]:


mydict[12421.0]


# In[15]:


print(mydict, 'ali' in mydict, 1 in mydict, sep='\n')


# In[16]:


mydict.keys()


# In[17]:


mydict.values()


# In[19]:


list(mydict.items())


# In[22]:


def hist_sent(s):
    d = dict()
    
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
#         print(d)
    return d

hist_sent('hello worlds!')
            


# In[23]:


def hist_sent(s):
    d = dict()
    
    for char in s:
        d[char] = d.get(char, 0) + 1
    return d

hist_sent('hello worlds!')


# In[28]:


fin = open('words.txt')
data = fin.read()
# print(data)
fin.close()


# In[29]:


fin = open('words.txt')
data = fin.read()
fin.close()

alph_dict = {}
for char in data:
    alph_dict[char] = alph_dict.get(char, 0)+1
print(alph_dict)


# In[37]:


total = sum(alph_dict.values()) - alph_dict['\n']
freq = []
for key in alph_dict:
    if key=='\n': continue
#     print(key, "{:.2f}%".format(alph_dict[key]/total * 100))
    freq.append([key, alph_dict[key]/total * 100])
sorted(freq)


# In[46]:


total = sum(alph_dict.values()) - alph_dict['\n']
freq = []
for key in alph_dict:
    if key=='\n': continue
#     print(key, "{:.2f}%".format(alph_dict[key]/total * 100))
    freq.append([key, round(alph_dict[key]/total * 100, 2)][::-1])
newl = []
for item in sorted(freq, reverse=True):
    newl.append([item[1], item[0]])
    
newl


# In[48]:


mydict = {1: 12.2, 'name': 'ali', 'age': 12}
del mydict[1]
mydict


# In[50]:


mydict = {1: 12.2, 'name': 'ali', 'age': 12}
value = mydict.pop(1)
print(mydict, value, sep='\n')


# In[51]:


mydict = {1: 12.2, 'name': 'ali', 'age': 12}
mydict.clear()
mydict


# In[52]:


a = {1: 12.2, 'name': 'ali', 'age': 12}
b = a
b[1] = 14
a


# In[55]:


a = {1: 12.2, 'name': 'ali', 'age': 12}
b = a.copy()
b[1] = 14
print(a, b, sep='\n')


# In[60]:


get_ipython().run_cell_magic('time', '', '\ndef fib(n):\n    if n<= 1:\n        return 1\n    return fib(n-1)+fib(n-2)\n\nfib(30)')


# In[60]:


get_ipython().run_cell_magic('time', '', '\ndef fib(n):\n    if n<= 1:\n        return 1\n    return fib(n-1)+fib(n-2)\n\nfib(30)')


# In[65]:


get_ipython().run_cell_magic('time', '', '\ndef fib(n):\n    f0 = 1\n    f1 = 1\n    for i in range(n-1):\n        f2 = f1 + f0\n        f0 = f1\n        f1 = f2\n    return f2\n\nfib(3000)')


# In[67]:


def fib(n, depth=0):
    if n<= 1:
        return 1
    print('  '*depth, 'fib({})+fib({})'.format(n-1, n-2))
    return fib(n-1, depth+1)+fib(n-2, depth+1)

fib(6)


# In[75]:


get_ipython().run_cell_magic('time', '', '\n# Memorization \n\nfib_dict = {1:1, 2:1}\n\ndef fib_RM(n):\n    if n in fib_dict:\n        return fib_dict[n]\n    fib_dict[n] = fib_RM(n-1) + fib_RM(n-2)\n    return fib_dict[n]\n\nfib_RM(1000)')


# In[77]:


a = 0

def test():
    a = 1 # local variable
    
test()
a


# In[79]:


a = 0

def test():
    global a # global variable
    a = 1
    
test()
a


# In[80]:


a = [1,2]

def test():
    a.append(3)
    
test()
a


# In[81]:


get_ipython().run_cell_magic('time', '', '\n# Memorization \n\ndef fib_RM(n):\n    fib_dict = {1:1, 2:1} #local dict, which will be reset in every call\n    if n in fib_dict:\n        return fib_dict[n]\n    fib_dict[n] = fib_RM(n-1) + fib_RM(n-2)\n    return fib_dict[n]\n\nfib_RM(20)')


# In[86]:


from math import sqrt

get_ipython().run_line_magic('timeit', 'sqrt(100)')


# In[84]:


get_ipython().run_line_magic('timeit', '100*100')


# In[85]:


get_ipython().run_line_magic('timeit', '100**.5')


# ### Excercises 

# In[91]:


l = ['ali', 'jav', 'hos', 'moh']

for i in l:
    for j in range(3):
        print(i[j], end=' ')
    print()


# In[92]:


l = ['ali', 'jav', 'hos', 'moh']

for i in range(3):
    for j in l:
        print(j[i], end=' ')
    print()

