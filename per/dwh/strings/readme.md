Strings

- constants:常量
    >|常量名|含义|值
    >|---|---|---
    >|ascii_letters|字母|下两项之和
    >|ascii_lowercase|小写字母|abcdefghijklmnopqrstuvwxyz
    >|ascii_uppercase|大写字母|ABCDEFGHIJKLMNOPQRSTUVWXYZ
    >|digits|数字|0123456789
    >|hexdigits|16进制数字|digits + abcdef + ABCDEF
    >|octdigits|8进制数字|01234567
    >|punctuation|标点|!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    >|whitespace|空格|' \t\n\r\v\f'
    >|printable|可打印内容|上述全部
    
- String Formatting:字符串格式化
        >参见[PEP 3101](https://www.python.org/dev/peps/pep-3101/ "官方文档")
    
    - 格式化方法
    
        1. 默认排序：按照顺序一一对应       
            ```python
           strings = "{} is good day, {}"
           print(strings.format("1.12", "hello"))  #1.12 is good day, hello
            ```
        
        2. 指定位置
            ```python
           strings = "{1} is good day, {0}"
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
            > |数字|格式|输出|描述
            > |---|---|---|---
            > |3.1415926|{:.2f}|3.14|保留小数点后两位
            > |3.1415926|{:+.2f}|+3.14|带符号保留小数点后两位
            > |-1	|{:+.2f}|-1.00|带符号保留小数点后两位
            > |2.71828|{:.0f}|3|不带小数
            > |5|{:0>2d}|05|数字补零 (填充左边, 宽度为2)
            > |5|{:x<4d}|5xxx|数字补x (填充右边, 宽度为4)
            > |10|{:x<4d}|10xx|数字补x (填充右边, 宽度为4)
            > |0x123a|{:x<8}|4666xxxx|先进制转化然后填充
            > |1000000|{:,}|1,000,000|以逗号分隔的数字格式
            > |1234.56789|{:,}|1,234.56789|以逗号分隔的数字格式
            > |0.25|{:.2%}|25.00%|百分比格式
            > |1000000000|{:.2e}|1.00e+09|指数记法
      
        7. format内容只能多，不能少
            > IndexError: tuple index out of range
      
        8. 用{}转义{}:`print("{{0}}的转义.{}".format("111","222"))   # :{0}的转义.111`
    
    
- f-string:格式化字符串常量（formatted string literals）
    >参见[PEP 498](https://www.python.org/dev/peps/pep-0498/ "官方文档")
    