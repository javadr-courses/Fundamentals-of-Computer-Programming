#!/usr/bin/env python
# coding: utf-8

# # Introduction to Progamming Languages with Python 
# ### University of Qom
# ##### Sat. 1401/09/12

# ### Chapter 9: Case Study [Word Play]

# In[7]:


fin = open('words.txt')


# In[8]:


fin


# In[9]:


lines = fin.readlines()


# In[13]:


lines[0][:-1], lines[0].strip()


# In[19]:


for line in lines:
     print(line.strip())
#     print(line, end='')


# In[20]:


for line in lines:
    line = line.strip()
    if len(line)>20:
        print(line)


# In[22]:


for line in lines:
    if 'e' not in line:
        print(line.strip())


# In[23]:


for line in lines:
    if line.count('e')==0:
        print(line.strip())


# In[26]:


count = 0
for line in lines:
    if 'e' in line:
        count = count + 1
count / len(lines) * 100


# In[29]:


def avoids(word, letters):
    for char in letters:
        print(char)
        if char in word:
            return True
    return False

avoids('hello', 'adfodsb')


# In[37]:


def avoids2(word, letters):
    count = 0 
    for char in letters:
        if char in word:
            count = count + 1 
    if count >= 2: 
        return True
    else: 
        return False

avoids2('hello', 'ladfdsb')


# In[38]:


def avoids2(word, letters):
    count = 0 
    for char in letters:
        if char in word:
            count = count + word.count(char)
    if count >= 2: 
        return True
    else: 
        return False

avoids2('hello', 'ladfdsb')


# In[44]:


def uses_only(word, letters):
    for char in word:
        if char not in letters:
            return False
    for char in letters:
            if char not in word:
                return False
        
    return True

uses_only('hello', 'helo')


# In[50]:


for line in lines:
    if uses_only(line.strip(), 'apec'):
        print(line.strip())


# In[59]:


def uses_all(word, letters):
    for char in letters:
            if char not in word:
                return False
        
    return True

uses_all('hello', 'helo')


# In[62]:


for line in lines:
    if uses_all(line.strip(), 'apecyx'):
        print(line.strip())


# In[63]:


def is_abecedarian(word):
    for i in range(len(word)-1):
        if ord(word[i]) > ord(word[i+1]):
            return False
    return True

is_abecedarian('ily')
            


# In[66]:


def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True

is_abecedarian('ily')


# In[67]:


for line in lines:
    if is_abecedarian(line.strip()):
        print(line.strip())


# In[69]:


def is_reverse_abecedarian(word):
    for i in range(len(word)-1):
        if ord(word[i]) <= ord(word[i+1]):
            return False
    return True

for line in lines:
    if is_reverse_abecedarian(line.strip()):
        print(line.strip())


# In[79]:


def is_abecedarian_rec(word):
    if len(word)<=1:
        return True
    if word[0]<=word[1]:
        return is_abecedarian_rec(word[1:])
    else:
        return False
    
is_abecedarian_rec('abcdeffg')


# In[ ]:


def is_abecedarian_rec(word):
    a = 0
    if len(word)<=1:
        return True
    if word[a]<=word[a+1]:
        return is_abecedarian_rec(word[a+1:])
    else:
        return False
    
is_abecedarian_rec('abcdeffg')


# # Chapter 10 : Lists

# In[84]:


l = [1, 2.3, True, 'hello', 2+4j]
l, type(l)


# In[82]:


type(2+3j)


# In[83]:


type(2+3i)


# In[85]:


w = 'hullo'
w[1]='e'


# In[86]:


l = ['h', 'u', 'l', 'l', 'o']
l[1] = 'e'
l


# In[87]:


l[::-1]


# In[88]:


help(str.join)


# In[92]:


'*#*'.join(l)


# In[93]:


list('hello')


# In[94]:


'hello ali and hosein and hasan'.split()


# In[99]:


'&'.join('hello ali and hosein and hasan'.split('and'))


# In[100]:


names = 'ali hasan hosein zahra'.split()

for name in names:
    print('Hello', name)


# In[103]:


names = 'ali hasan hosein zahra'.split()

i = 0
while i<len(names):
    print('Hello', names[i], sep='*')
    i = i+1


# In[104]:


n = input().split()
print(n)


# In[106]:


n = list(input())
print(n)


# In[108]:


a = [1,2, 3]
b = [3,4]
a+b


# In[109]:


a = [1,2]
a * 2


# In[110]:


a = [1,2, 3]
b = [3,4]
a*b


# In[113]:


l = [0]* 10
l[3]=12
l


# In[114]:


l = [1,4,6,7,8,94,2,6,7]
l[3:7]


# In[115]:


l[:]


# In[116]:


l = []
l.append(12)
l.append(7)
l.append(5)
l


# In[118]:


n = int(input("Please enter your desired numebr: "))
l = []
for i in range(n):
    l.append(int(input()))
print(l)


# In[119]:


l = [1, 4, 6, 7, 8, 94, 2, 6, 7]
print(l)
l.sort()
print(l)


# In[120]:


l = [1, 4, 6, 7, 8, 94, 2, 6, 7]
print(l)
l2 = l
l2.sort()
print(l)


# In[121]:


n = 2
m = n
m = 4
print(n)


# In[123]:


l = [1, 4, 6, 7, 8, 94, 2, 6, 7]
print(l)
l2 = l[:]
l2.sort()
print(l)
print(l2)


# In[124]:


l = [1, 4, 6, 7, 8, 94, 2, 6, 7]
print(l)
l2 = l.copy()
l2.sort()
print(l)
print(l2)


# In[128]:


def test(mylist):
    mylist[0]= 'boooq'
    
l = [1,3,5,67,0]
test(l)
l


# In[131]:


a = [1,3]
b = [3,4]
a.extend(b)
print(a,b)

