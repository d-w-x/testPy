# -*- coding:utf8 -*
__author__ = 'DW '
__date__ = '2019/1/18'

s = [1, 2, 3, 9]
t = [[]]
q = range(1, 10)
print(s)
print(t)
print(q)
print(s + t)
print(s * 3)
print(t * 3)
# print(q * 3) TypeError: unsupported operand type(s) for *: 'range' and 'int'
print(s.index(1))
t = [3, 4]
print("=================")
print(s > t)
print(s[1:-1])
s[1] = 100
print(s)
s[2:3] = [3, 1, 1, 5, 1]
print(s)
s.reverse()
print(s)
print(s.reverse())
q = s.copy()
q.append("caddr")
print(s)
print(q)
strs = "dzxcvtqw"
print([x for x in strs])
print("=================")
s.sort()
print(s)
print(range(0) == range(2, 1, 3))
