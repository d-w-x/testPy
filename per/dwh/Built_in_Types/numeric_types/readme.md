# 数字

- 分类
    1. int:
        1. 精度是无限
        2. 包括二进制，八进制，十进制和十六进制整数
        3. 用整数字面值直接创建
    2. float:
        1. 是C里的double
        2. 用含有小数点形式or指数形式的数字创建
    3. complex:
        1. 实部和虚部都是float数
        2. 用J作为虚数单位


- 数的运算
    1. 支持混合运算，int——>float——>complex
    2. 可以使用构造函数生成对应的数
    3. 运算优先级:
        >|         运算         |                 说明                 |
        >|:--------------------|:------------------------------------|
        >| x + y               |                                     |
        >| x - y               |                                     |
        >| x / y               |                                     |
        >| x // y              | 除法的整数（向负无穷舍入），浮点也可以... |
        >| x % y               | 求余，浮点也可以...                    |
        >| -x                  |                                     |
        >| +x                  |                                     |
        >| abs(x)              |                                     |
        >| int(x)              |                                     |
        >| float(x)            | 包括“nan” 和 “inf”                   |
        >| complex(re, im)     | 构造虚数，字符串必须是"X+YJ"的形式       |
        >| complex.conjugate() | 虚数共轭                             |
        >| divmod(x, y)        | (商,余数)                            |
        >| pow(x, y)           | dif: pow(0, 0) = 1                  |
        >| x ** y              | 同上                                 |
    4. 实数的额外库方法:
        >|      运算      |     说明      |
        >|:--------------|:-------------|
        >| math.trunc(x) | 去尾          |
        >| round(x\[, n\]) | 指定位四舍五入 |
        >| math.floor(x) |              |
        >| math.ceil(x)  |              |
    5. 整数的按位运算(Bitwise Operations):
        >| 运算   | 说明    |           |
        >|:------|:-------|:----------|
        >| x \| y   |        |           |
        >| x ^ y |        |                 |
        >| >     | x & y  |           |
        >| >     | x << n | n必须是整数 |
        >| >     | x >> n |           |
        >| >     | ~x     |           |
    6. 额外操作
        - on Integer Types
            >|方法|参数|说明|
            >|---|---|---|
            >|bit_length| |不算符号位|
            >|to_bytes|length, byteorder, signed|位长度 ，升\[big\]降\[little\]序，是否区分正负数含义<br/>如果是False+负数，产生OverflowError: can't convert negative int to unsigned|
            >|from_bytes|bytes, byteorder, signed| |

        - on Float
            >|方法|参数|说明|
            >|---|---|---|
            >|as_integer_ratio| |分数化，二元组|
            >|is_integer| | |
            >|hex| |十六进制表示|
            >|fromhex|s|`[sign]['0x']integer['.'fraction]['p'exponent]`没有空格|

- 数的Hash
    1. Hash需要保证hash(x) == hash(y)当x == y
    2. 因子 P = 2**61 - 1 
    3. 计算：
        >If x = m / n is a nonnegative rational number and n is not divisible by P, define hash(x) as m * invmod(n, P) % P, where invmod(n, P) gives the inverse of n modulo P. 
        >
        >If x = m / n is a nonnegative rational number and n is divisible by P (but m is not) then n has no inverse modulo P and the rule above doesn’t apply; in this case define hash(x) to be the constant value sys.hash_info.inf.
        >
        >If x = m / n is a negative rational number define hash(x) as -hash(-x). If the resulting hash is -1, replace it with -2.
        >
        >The particular values sys.hash_info.inf, -sys.hash_info.inf and sys.hash_info.nan are used as hash values for positive infinity, negative infinity, or nans (respectively). (All hashable nans have the same hash value.)
        >
        >For a complex number z, the hash values of the real and imaginary parts are combined by computing hash(z.real) + sys.hash_info.imag * hash(z.imag), reduced modulo 2**sys.hash_info.width so that it lies in range(-2**(sys.hash_info.width - 1), 2**(sys.hash_info.width - 1)). Again, if the result is -1, it’s replaced with -2.