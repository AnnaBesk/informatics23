#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)


# In[ ]:


x = int(input())
print(x%10)


# In[ ]:


A = list(map(int, input().split()))
x = 1
for i in A:
    x = x * i
print(x ** (1/len(A)))


# In[77]:


f = open('input.txt', 'r')
A = list(map(int, f.readline().split()))
m = f.readline()
s = 0
if m == "+":
    s = sum(A)
elif m == "-":
    s = A[0]
    for i in range(1, len(A)):
        s -= A[i]
elif m == ":":
    s = A[0]
    for i in range(1, len(A)):
        s = s/A[i]
elif m == "*":
    s = A[0]
    for i in range(1, len(A)):
        s = s * A[i]
g = open('output.txt', 'w')
g.write(str(s) + '\n')
f.close()
g.close()


# In[76]:


N = input()
b = int(input())
c = int(input())
N = N[::-1]
chislo = 0
fin = str()
#переведем N в десятичную систему
for i in range(len(N)):
    chislo += int(N[i])*(b**i)

#переведем chislo в новую систему
while chislo > c:
    ost = chislo % c
    fin += str(ost)
    chislo = chislo // c
ost = chislo % c
fin += str(ost)
print(fin[::-1])
    


# In[75]:


f = open('input2.txt', 'r')
A = list(f.readline().split())
B = []
m = f.readline()
type(m)
sys = int(f.readline())
s = 0
ch = str()
#переведем числа в 10ричную систему отсчета
for j in range(len(A)):
    N = A[j][::-1]
    chislo = 0
    for i in range(len(N)):
        chislo += int(N[i])*(sys**i)
    B.append(chislo)
m = m.strip('\n')
# произвожу операцию
if m == "+":
    s = sum(B)
elif m == "-":
    s = B[0]
    for i in range(1, len(B)):
        s -= B[i]
elif m == ":":
    s = B[0]
    for i in range(1, len(B)):
        s = s/B[i]
elif m == "*":
    s = B[0]
    for i in range(1, len(B)):
        s = s * B[i]
#переводим ответ в исходную сс
while s > sys:
    ost = s % sys
    ch += str(ost)
    s = s // sys
ost = s % sys
ch += str(ost)
g = open('output2.txt', 'w')
g.write(str(ch[::-1]) + '\n')
f.close()
g.close()

