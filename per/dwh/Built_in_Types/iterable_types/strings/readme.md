
# Strings

## constants:常量
  >| 常量名           | 含义       | 值                                    |
  >|:----------------|:----------|:-------------------------------------|
  >| ascii_letters   | 字母       | 下两项之和                             |
  >| ascii_lowercase | 小写字母   | abcdefghijklmnopqrstuvwxyz           |
  >| ascii_uppercase | 大写字母   | ABCDEFGHIJKLMNOPQRSTUVWXYZ           |
  >| digits          | 数字       | 0123456789                           |
  >| hexdigits       | 16进制数字 | digits + abcdef + ABCDEF             |
  >| octdigits       | 8进制数字  | 01234567                             |
  >| punctuation     | 标点       | !"#$%&'()*+,-./:;<=>?@\[\]^_`{ \| }~ |
  >| whitespace      | 空格       | ' \t\n\r\v\f'                        |
  >| printable       | 可打印内容  | 上述全部                               |

## 字符串前置

1. u/U:表示unicode字符串
2. r/R:非转义的原始字符串：后者所有内容不进行转义。常用于正则表达式，对应着re模块。
3. b:bytes，字节码，需要decode

## String Formatting:字符串格式化

>参见[PEP 3101](https://www.python.org/dev/peps/pep-3101/ "官方文档")

1. 默认排序：按照顺序一一对应

    ```python
    strings = "{} is good day, {}"
    print(strings.format("1.12", "hello"))  #1.12 is good day, hello
    ```

2. 指定位置

    ```python
    strings = "{1} is good day, {0}"
    print(str)
    print(strings.format("hello", "1.12"))  #1.12 is good day, hello
    ```

    - 变形：通过列表索引

        ```python
        strings = "{0[0]} is good day, {0[1]}"
        args = ["1.12", "hello"]
        print(strings.format(args))
        ```

3. 键值对

    ```python
    strings = "{}: {date} is good day, {greeting}"
    print(strings.format(3, greeting="hello", date="1.12"))  #3: 1.12 is good day, hello
    ```

    - 变形：使用字典

        ```python
        strings = "{}: {date} is good day, {greeting}"
        keys = {"greeting": "hello", "date": "1/12"}
        print(strings.format(3, **keys))  # 3: 1/12 is good day, hello
         ```

4. 对齐
    - “<”表示居左对齐:`print('{:<10}'.format('ABC12abc') + "1")  # :ABC12abc  1`
    - ">"表示居右对齐:`print('{:>10}'.format('ABC12abc') + "1")  # :  ABC12abc1`
    - "^"表示居中对齐:`print('{:^10}'.format('ABC12abc') + "1")  # : ABC12abc 1`
    - 上述均可换成用指定字符填充:`print('{:*^10}'.format('ABC12abc') + "1")  # :*ABC12abc*1`

5. 进制表示
    - “b”表示二进制:`print("{:b}".format(-200)) # -11001000`
    - "o"表示八进制:`print("{:o}".format(-200)) # -310`
    - "d"表示十进制:`print("{:d}".format(-0b1100)) # -12`
    - "x"表示十六进制:`print("{:x}".format(-0b1100)) # -c`

6. 精度转化

    > |数字|格式|输出|描述|
    > |---|---|---|---|
    > |3.1415926|\{:.2f\}|3.14|保留小数点后两位|
    > |3.1415926|\{:+.2f\}|+3.14|带符号保留小数点后两位|
    > |-1	|\{:+.2f\}|-1.00|带符号保留小数点后两位|
    > |2.71828|\{:.0f\}|3|不带小数|
    > |5|\{:0>2d\}|05|数字补零 (填充左边, 宽度为2)|
    > |5|\{:x<4d\}|5xxx|数字补x (填充右边, 宽度为4)|
    > |10|\{:x<4d\}|10xx|数字补x (填充右边, 宽度为4)|
    > |0x123a|\{:x<8\}|4666xxxx|先进制转化然后填充|
    > |1000000|\{:,\}|1,000,000|以逗号分隔的数字格式|
    > |1234.56789|\{:,\}|1,234.56789|以逗号分隔的数字格式|
    > |0.25|\{:.2%\}|25.00%|百分比格式|
    > |1000000000|\{:.2e\}|1.00e+09|指数记法|

7. format内容只能多，不能少
    > IndexError: tuple index out of range

8. 用{}转义{}:`print("{{0}}的转义.{}".format("111","222"))   # :{0}的转义.111`


## f-string:格式化字符串常量（formatted string literals）

>参见[PEP 498](https://www.python.org/dev/peps/pep-0498/ "官方文档")

*尽管format易读，但是当处理多个参数和更长的字符串时它可能过于冗长*

**f-string类似于kotlin的字符串，也类似于El表达式等，f不区分大小写**

1. 示例:
    ```python
    #Hello,today is 1/12
    date = "1/12"
    greeting = "hello"
    print(f"{greeting.capitalize()},today is {date}")
    ```

2. 补充说明:
    1. 可以计算:`print("{3*4}")`
    2. 可以调用函数
    3. 多行字符串时没必要将f放在多行字符串的每一行的前面，只在需要的行出现
    4. 可以在表达式中使用各种类型的引号，只要确保在表达式中使用的f-字符串外部没有使用相同类型的引号即可。
    5. 大括号用大括号转义
    6. 表达式部分不能使用反斜杠\转义
    7. 可以将内容同format一样进行格式化，形式为`{expression : format}`
    8. lambda表达式建议写在括号里`strings = f"{(lambda x: x * 37) (2)}"`


## string的其他方法:{#string的其他方法}

|     方法      |              参数              |                                   效果                                   |                                                              说明                                                              |    |
|:-------------|:------------------------------|:------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|:---|
| capitalize   |                               | 首字母大写                                                                |                                                                                                                               |    |
| center       | width                         | 将字符串扩展到指定宽度并居中                                                 |                                                                                                                               |    |
| count        | sub\[, start\[, end\]\]           | 从指定位置计算给定字符在原始字符出现次数                                       |                                                                                                                               |    |
| decode       | encoding\[, errors\]            | 将其从指定字符集解码                                                       | 1.strict，默认,遇到非法字符时抛出异常<br/>2.ignore，忽略非法字符<br/>3.replace，用?取代非法字符<br/>4.xmlcharrefreplace，使用XML的字符引用 |    |
| encode       | encoding\[, errors\]            | 将其编码为指定字符集的字符流                                                 |                                                                                                                               |    |
| endswith     | suffix\[, start\[, end\]\]        | 检查字符串是否以指定结尾                                                    | suffix可以是一组待测值：("1","2","3")                                                                                            |    |
| expandtabs   | tabsize                       | 将\t展开成指定长度                                                         | \t指从该行首算的长度，默认8                                                                                                       |    |
| find         | sub\[,start\[, end\]\]            | 在给定范围查找指定字符串                                                    | 未找到返回-1                                                                                                                    |    |
| format       |                               |                                                                         |                                                                                                                               |    |
| index        | sub\[, start\[, end\]\]           | 基本同find                                                               | 不存在产生异常：ValueError: substring not found                                                                                  |    |
| isalnum      |                               | 至少有一个字符，是字母和数字组合                                             |                                                                                                                               |    |
| isalpha      |                               | 至少有一个字符，是纯字母                                                    |                                                                                                                               |    |
| isdecimal    |                               | Unicode数字，全角数字（双字节）                                             | 罗马数字，汉字数字False，byte数字（单字节）无此方法。                                                                                 |    |
| isdigit      |                               | Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字                   | 汉字False                                                                                                                      |    |
| isnumeric    |                               | Unicode数字、全角数字（双字节）、罗马数字和汉字数字会返回True                   | byte数字（单字节）无此方法。                                                                                                      |    |
| isascii      |                               | 都是ASCII字符。【空字符也是ASCII字符】                                       |                                                                                                                               |    |
| islower      |                               | 包含至少一个区分大小写的字符，这些(区分大小写的)字符都是小写                      |                                                                                                                               |    |
| isidentifier |                               | 是python保留字符                                                          |                                                                                                                               |    |
| isprintable  |                               |                                                                         |                                                                                                                               |    |
| isspace      |                               |                                                                         |                                                                                                                               |    |
| istitle      |                               |                                                                         | title格式：所有的单词拼写首字母为大写，且其他字母为小写                                                                                |    |
| isupper      |                               |                                                                         |                                                                                                                               |    |
| join         | iterable                      | 过指定字符连接序列中元素后生成的新字符串<br/>如："-".join("32423") ->3-2-4-2-3 | 字典只对key进行join                                                                                                             |    |
| __ len __    |                               |                                                                         | 调用len(str)时自动调用                                                                                                           |    |
| ljust        | width\[, fillchar\]             | 左对齐，用指定字符填充至长度width                                            |                                                                                                                               |    |
| lower        |                               |                                                                         |                                                                                                                               |    |
| lstrip       | chars                         | 删除左空格                                                                | 如果给定char，则删去开头的char                                                                                                    |    |
| maketrans    | src_str,dis_str\[, ignore_str\] | 生成转换表，将src字符串内容按字节变成dis对应内容，ignore中内容变成空             | 通过str.maketrans直接调用，生成Dict\[int, _T\]                                                                                     |    |
| translate    | table\[, deleted\]              | 使用转换表进行转换                                                         |                                                                                                                               |    |
| max          | str                           | 返回字符串中的最大值                                                       | <span style="color: #ffb6c1; ">调用方法：max(str)</span>                                                                        |    |
| min          | str                           | 返回字符串中的最小值                                                       |                                                                                                                               |    |
| replace      | old, new\[, count\]             | 将字符串中的str1替换成str2， max指定，则替换不超过max次。                      |                                                                                                                               |    |
| rfind        | sub\[, start\[, end\]\]           | 从右边开始查找.                                                           |                                                                                                                               |    |
| rindex       | sub\[, start\[, end\]\]           | 从右边开始.                                                               |                                                                                                                               |    |
| rjust        | width\[, fillchar\]             | 右对齐                                                                   |                                                                                                                               |    |
| rstrip       |                               | 删除末尾空格                                                              |                                                                                                                               |    |
| split        | \[sep\[, maxsplit\]\]             | 切分字符，返回列表                                                         | sep默认空格，maxsplit指切分次数，默认-1不限制                                                                                       |    |
| splitlines   | keepends                      | 按行切分                                                                 | keepends为True，则保留换行符。                                                                                                   |    |
| startswith   | suffix\[, start\[, end\]\]        | 检查字符串是否以指定结尾                                                    | suffix可以是一组待测值：("1","2","3")                                                                                            |    |
| strip        | chars                         | 删除空格                                                                 | 如果给定char，则删去开头的char                                                                                                    |    |
| swapcase     |                               | 大小写互换                                                                |                                                                                                                               |    |
| title        |                               | 标题化                                                                   |                                                                                                                               |    |
| upper        |                               |                                                                         |                                                                                                                               |    |
| zfill        | width                         | 右对齐，左加0                                                             |                                                                                                                               |    |

- String 是 [Iterator](../readme.md#iterator-types  "说明")