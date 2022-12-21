#!/usr/bin/env python
# coding: utf-8

# # Introduction to Progamming Languages with Python 
# ### University of Qom
# ##### Sat. 1401/08/28

# ### Chapter 8: Strings

# In[1]:


s = "hello worlds!"
s[0]


# In[2]:


s[14]


# In[3]:


s[2.1]


# In[4]:


s[5]


# In[5]:


for i in range(len(s)):
    print(s[i])


# In[7]:


l = len(s)
s[l-1]


# In[8]:


s[2:8]


# In[9]:


s[:8]


# In[10]:


s[8:]


# In[11]:


s[2:8:2]


# In[12]:


s[::2]


# In[13]:


s[1::2]


# In[14]:


s[-1]


# In[15]:


s[-5:-8]


# In[16]:


s[-8:-5]


# In[17]:


s[-5:-8:-1]


# In[18]:


s[::-1]


# In[20]:


def reverse(s):
    news = ''
    for i in range(len(s)):
        news = s[i] + news
        
    return news

reverse('ali')


# In[22]:


def revw(s):
    l = -len(s)
    i = -1
    news = ''
    while i>=l:
        news = news + s[i]
        i = i-1
    return news

revw('ali')


# In[23]:


for i in 12,13,14,15:
    print(i)


# In[24]:


for i in s:
    print(i)


# In[25]:


s[123123:3412351435]


# In[26]:


s 


# In[27]:


s[0]='H'


# In[29]:


s = 'H'+s[1:]
s


# In[31]:


s = s[:6] + 'W' + s[7:]
s


# In[33]:


s = s[:5] + "*****" + s[6:]
s


# In[35]:


s = s[:6]
s


# In[37]:


def find(string, char):
    for i in string:
        if i==char:
            return True
    return False

# find('ali', 'i')
find('ali', 'z')


# In[41]:


def find(string, char):
    i = 0
    while i<len(string):
        if string[i]==char:
            return i
        i = i + 1
    return -1

# find('hello', 'e')
find('hello', 'z')


# In[43]:


def count(string, char):
    counter = 0
    for i in string:
        if i==char:
            counter = counter + 1
    return counter

count('hello worlds!', 'l')


# In[44]:


'ali' == 'Ali'


# In[54]:


def find(string, substr):
    i = 0
    sl = len(substr)
    while i<=len(string)-sl:
        if string[i:i+sl]==substr:
            return True
        i = i+1
    return False

# find('hello worlds', 'rld')
# find('hello worlds', 'lds')
find('hello worlds', 'l')


# In[53]:


s[1:2]


# In[56]:


def find(string, substr):
    i = 0
    sl = len(substr)
    while i<=len(string)-sl:
        if string[i:i+sl]==substr:
            return i
        i = i+1
    return -1

find('hello worlds', 'rld')
# find('hello worlds', 'lds')
# find('hello worlds', 'l')


# In[57]:


'll' in 'hello worlds'


# In[60]:


'hello worlds!'.count('ll')


# In[59]:


'hello worlds!'.find('ll')


# In[61]:


'hello worlds!'.find('zz')


# In[62]:


'hello worlds'.index('z')


# In[64]:


'     hello worlds   \t   '.strip()


# In[65]:


'     hello worlds      '.lstrip()


# In[66]:


'     hello worlds      '.replace('ll', 'zzzz')


# In[67]:


'     hello worlds      '.replace('l', '*')


# In[69]:


str.replace('hello worlds', 'l', '*')


# In[70]:


help(str.find)

