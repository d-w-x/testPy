#布尔

- python中的布尔值
    1. 值不仅是True和False，任何值在满足条件的时候都可以做布尔值
    2. 1是错的，实质是调用对应值的`__bool__()`方法或者`__len__() != 0`
    3. True = 1,False = 0
    4. 常见的false：
        - 常量：None，False
        - 任何为0的数值：0, 0.0, 0j, Decimal(0), Fraction(0, 1)
        - 空集合或序列：'', (), [], {}, set(), range(0)
    5. In addition, Booleans are a subtype of integers.

- 布尔运算
    1. and , or , not
    2. 上述优先级在提高
    3. 布尔运算是最低优先级，因此 `a == not b`是syntax err；`not a == b`等价于` not (a == b)`
    
- 比较
    1. 优先级高于布尔运算
    2. 可以线性比较:`x < y <= z`就是`x < y and y<= z`
    3. 2中的任何一种情况z都是短路的
    4. 比较符：<, <=, >, >=, ==, !=, is, is not
    5. 除了数字之外，任何两个类都不会相等；部分类只能比相等，不可比大小
    6. ==实质的__eq__()方法的重载【那么python支持重载运算符】;is判断引用是否相等，不可重载
    7. in 和 not in 对iterable或者实现__contains__()方法的类使用
    8. 重载运算符：
        - __ lt __:小于
        - __ gt __:大于
        - __ le __:小于等于
        - __ ge __:大于等于
        - __ eq __:等于
        - __ ne __:不等于
    