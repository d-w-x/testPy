# Iterator Types

- 方法：
    1. __ iter __:返回自身，允许迭代器和容器进行for和in操作
    2. __ next __:返回下一个元素，或者抛出StopIteration异常

# Iterable

支持for...in...迭代<br/>
通过iter(obj)得到对应的迭代器

# Generator ——生成器

惰性计算

1. 生成：
    1. 把一个列表生成式的[]改成()：`g = (x * x for x in range(10))`
    2. 含有yield语句的函数
        1. 每次检测到yield语句返回
        2. 函数返回值包含在StopIteration的value

2. 调用:
    1. 使用next(Generator)，如果越界产生StopIteration异常
    2. 使用for...in...
