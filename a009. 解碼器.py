'''method 1
K = -7

s = list(input())

i = 0

while i < len(s):
    s[i] = ord(s[i])
    s[i] = s[i] + K
    print(chr(s[i]),end='')
    i=i+1
'''
''' method 2
K = -7

s = list(input())

i = 0

for i in s:
    i = ord(i)
    i += K
    print(chr(i),end = '')
'''
''' method 3 '''

K = -7

#list
s = list(input())

#list
decode = [ord(i) + K for i in s]

for d in decode:
    print(chr(d), end = '')
