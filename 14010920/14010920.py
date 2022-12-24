#!/usr/bin/env python
# coding: utf-8

# # Introduction to Progamming Languages with Python 
# ### University of Qom
# ##### Sun. 1401/09/20

# # Chapter 12 : Tuples

# In[1]:


t = 1,2,3
type(t)


# In[2]:


t = (1,2,3)
type(t)


# In[3]:


for i in 'ali', 'javad', 'hosein':
    print(f'hi {i}')


# In[15]:


n = 12.988767
'n = {:.2f}'.format(n)


# In[13]:


n = 12.988767
f'n = {n:.2f}'


# In[7]:


n = 12.988767
f'n = {{ {n:.2f} }}'


# In[17]:


n = 12.988767
f'{n = :.2f}'


# In[18]:


t = (1)
type(t)


# In[19]:


t = (1,) # equals t = 1,
type(t)


# In[20]:


t = (1,4,6,8)
t[0] = 12


# In[21]:


t = (1,4,6,8)
t = (12,) + t[1:]
t


# In[22]:


t = (1,4,6,8)
t = t[:2] + (12,) + t[2:]
t


# In[23]:


w = 'hello'
print(list(w), tuple(w), sep='\n')


# In[24]:


(1,2) < (1,5)


# In[30]:


(2,5) < (2,5,3, 342,234,5,)


# In[31]:


(2,5,2435,6,7,7,8,) < (2,5)


# In[35]:


def fib(n):
    f0 = 1
    f1 = 1
    for i in range(n-2):
        f2 = f1+f0
        f0 = f1
        f1 = f2
    return f2

fib(50)


# In[36]:


# swap
a = 3
b = 5
t = a
a = b
b = t
a,b


# In[37]:


# tuple assignment
a = 3
b = 5

a, b = b, a

a,b


# In[39]:


m, n = map(int, input().split())
m,n 


# In[40]:


def fib(n):
    f0 = 1
    f1 = 1
    for i in range(n-2):
        f0, f1 = f1, f0+f1
    return f1

fib(5)


# In[41]:


def test(n):
    return n**2, n**3

test(3)


# In[42]:


print(1,2,3,4,5,)


# In[44]:


def test(m,n,p):
    return m*n*p

# test(1,2,3)
test(1,2,3,4)


# In[46]:


def mysum(*t):
    s = 0
    for item in t:
        s += item
    return s

mysum(1,2,435,7,7,8)
    


# In[47]:


def mysum(n, *t):
    print(n)
    print(t)
mysum(1,2,435,7,7,8)


# In[48]:


# wrong usage
def test(*t, *p):
    print(t,p)
    
    
test(123,5,5,6,7,8,8,)


# In[50]:


def test(t, p):
    print(t,p)
    
    
test((123,5,5),(6,7,8,8,))


# In[51]:


sum(1,2,34,45)


# In[56]:


sum((1,2,34,45), start=100)


# In[55]:


help(sum)


# In[57]:


names = ['ali', 'hasan', 'hosein']
family = ['taqavi', 'alavi', 'hasani']
length = len(names)

for i in range(length):
    print(f"{names[i]} {family[i]}")


# In[59]:


names = ['ali', 'hasan', 'hosein']
family = ['taqavi', 'alavi', 'hasani']
length = len(names)

total = []
for i in range(length):
    total.append([names[i], family[i]])
    
total


# In[62]:


names = ['ali', 'hasan', 'hosein', 'reza']
family = ['taqavi', 'alavi', 'hasani', 'mohammadi']
total = names + family
for i in range(4):
    print(total[i], total[i+4])


# In[64]:


names = ['ali', 'hasan', 'hosein', 'reza']
family = ['taqavi', 'alavi', 'hasani', 'mohammadi']

list(zip(names, family))


# In[66]:


names = ['ali', 'hasan', 'hosein', 'reza']
family = ['taqavi', 'alavi', 'hasani', 'mohammadi']

for item in zip(names, family):
    print(item)
    
for item in zip(names, family):
    print(item[0], item[1])


# In[67]:


names = ['ali', 'hasan', 'hosein', 'reza']
family = ['taqavi', 'alavi', 'hasani', 'mohammadi']
    
for name, family in zip(names, family):
    print(name, family)


# In[70]:


names = ['ali', 'hasan', 'hosein', 'reza']
family = ['taqavi', 'alavi']

list(zip(names, family))


# In[71]:


l = [1,2,35,8,9,10]
c = []
for i in range(len(l)-1):
    c.append(l[i]+l[i+1])
    
c


# In[73]:


l = [1,2,35,8,9,10]
c = []
for i in zip(l, l[1:]):
    c.append(sum(i))
c


# In[74]:


list(zip([1,2,35,8,9,10], [2,35,8,9,10]))


# In[75]:


l = [1,2,35,8,9,10]
c = []
list(map(sum, zip(l, l[1:])))


# In[ ]:


# Matrix
# 1 2 3
# 4 5 6
# 7 8 9

# row-major
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

# column-major
mat = [[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]]


# In[77]:


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
r = len(mat)
c = len(mat[0])
for row in range(r):
    for col in range(c):
        mat[row][col] **= 2

mat


# In[80]:


mat = {(1,1):1, (1,2):2, (1,3):3,
       (2,1):4, (2,2):5, (2,3):6,
       (3,1):7, (3,2):8, (3,3):9}

r = 3
c = 3
for row in range(1,r+1):
    for col in range(1,c+1):
        mat[(row,col)] **= 2
        
mat


# In[86]:


mat = {(1,1):1, (1,2):2, (1,3):3,
       (2,1):4, (2,2):5, (2,3):6,
       (3,1):7, (3,2):8, (3,3):9}

r = 3
c = 3
for row in range(1,r+1):
    for col in range(1,c+1):
        print(mat[(row,col)], end=' ')
    print()


# In[88]:


mat = {(1,1):1, 
       (2,3):6,
       (3,2):8}

r = 3
c = 3
for row in range(1,r+1):
    for col in range(1,c+1):
        if (row,col) in mat:
            print(mat[(row,col)], end=' ')
        else:
            print(0, end=" ")
    print()


# In[89]:


mat = {(1,1):1, 
       (2,3):6,
       (3,2):8}

r = 3
c = 3
for row in range(1,r+1):
    for col in range(1,c+1):
        print(mat.get((row,col), 0), end=' ')
    print()

