# -*- coding:utf8 -*
__author__ = 'DW '
__date__ = '2019/1/16'

a = " 12a4sDf\t1d马 "
s = iter(a)
for i in range(0, a.__len__()):
    print(s.__next__())
print("============================")
for i in a:
    print(i)


# =====================================
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(15)
for i in f:
    print(i)
