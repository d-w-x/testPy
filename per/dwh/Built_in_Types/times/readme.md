# time

- [readme](lib_time/readme.md)提供各种操作时间的函数

- datetime模块定义了下面这几个类:
  - datetime.date:表示日期的类。常用的属性有year, month, day；
  - datetime.time:表示时间的类。常用的属性有hour, minute, second, microsecond；
  - datetime.datetime:表示日期时间。
  - datetime.timedelta:表示时间间隔，即两个时间点之间的长度。
  - datetime.tzinfo:与时区有关的相关信息。表示时间的类。常用的属性有hour, minute, second,
    microsecond；

- 表示时间:
  - 时间戳:从零点开始的秒数
  - 时间元组:
    > | 索引 | 属性                 |
    > |:---|:-------------------|
    > | 0  | tm_year(年)         |
    > | 1  | tm_mon(月)          |
    > | 2  | tm_mday(日)         |
    > | 3  | tm_hour(时)         |
    > | 4  | tm_min(分)          |
    > | 5  | tm_sec(秒)          |
    > | 6  | tm_wday(星期几)       |
    > | 7  | tm_yday(一年中的第几天)   |
    > | 8  | tm_isdst(是否为夏令时-1) |

  - 字符串
