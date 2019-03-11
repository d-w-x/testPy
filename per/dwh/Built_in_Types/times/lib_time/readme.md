# time

1. `epoch`:`January 1, 1970, 00:00:00 (UTC)`,可以使用`time.gmtime(0)`获得
2. 一般忽略闰秒
3. 一般是从系统零点到2038年
4. 没有千年问题
5. UTC(Coordinated Universal Time,世界协调时)也叫格林威治天文时间，是世界标准时间．在我国为UTC+8
6. DST(Daylight Saving Time)即夏令时

### 方法

1. time.asctime(\[t\]): 接受时间元组并返回一个可读的形式"Tue May 30 17:17:30
   2017"的24个字符的字符串
2. time.ctime(\[secs\]): 作用相当于asctime(localtime(secs)),未给参数相当于asctime()
3. time.get_clock_info(\[name\]): 获取相关方法的详细信息
   1. 方法参数范围:
      2. 'monotonic': time.monotonic()
      3. 'perf_counter': time.perf_counter()
      4. 'process_time': time.process_time()
      5. 'thread_time': time.thread_time()
      6. 'time': time.time()
   2. 返回值属性:
      1. adjustable: 当该值可以被自动改变的时候返回`True`,如当前时间等;对CPU时间等不可改变值返回`false`
      2. implementation: 实现使用的C函数
      3. monotonic: (单调的)该时间不可以被减少
      4. resolution: 以秒为单位的时钟分辨率(float)
4. time.gmtime(\[secs\]):
   接收时间戳并返回格林威治天文时间下的时间元组(t.tm_isdst始终为０)。如果sec参数未输入，则以当前时间为转换标准
5. time.localtime(\[secs\]): 格式化时间戳为本地的时间。如果sec参数未输入，则以当前时间为转换标准
6. time.mktime(t): `localtime`的反函数，接受时间元组并返回时间戳
7. time.monotonic(): 返回单调时钟的值（以分数秒为单位），即不能倒计时的时钟。时钟不受系统时钟更新的影响。
8. time.perf_counter():
   返回计时器的精准时间(系统的运行时间)，包含整个系统的睡眠时间．由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的
9. time.process_time():
   返回当前进程执行CPU的时间总和，不包含睡眠时间．由于返回值的基准点是未定义的，所以只有连续调用的结果之间的差才是有效的
10. time.sleep(secs): 推迟调用线程的运行，secs的单位是秒
11. time.strftime(format\[,t\]): 接收时间元组，并返回以可读字符串表示的当地时间
    1. format:
       - %y: 两位数的年份表示（00-99）
       - %Y: 四位数的年份表示（000-9999）
       - %m: 月份（01-12）
       - %d: 月内中的一天（0-31）
       - %H: 24小时制小时数（0-23）
       - %M: 分钟数（00-59）
       - %S: 秒（00-59）
       - %I: 12小时制小时数（01-12）
       - %a: 本地简化星期名称
       - %A: 本地完整星期名称
       - %b: 本地简化的月份名称
       - %B: 本地完整的月份名称
       - %c: 本地相应的日期表示和时间表示
       - %j: 年内的一天（001-366）
       - %p: 本地A.M.或P.M.的等价符
       - %U: 一年中的星期数（00-53）星期天为星期的开始
       - %w: 星期（0-6），星期天为星期的开始
       - %W: 一年中的星期数（00-53）星期一为星期的开始
       - %x: 本地相应的日期表示
       - %X: 本地相应的时间表示
       - %Z: 当前时区的名称
       - %%: %号本身
    2. t: 可选的时间元组
12. time.strptime(string\[, format\]): 接收可读字符串表示的当地时间,返回时间元组
13. time.time(): 返回当前时间的时间戳
14. time.thread_time(): 当前线程占用CPU时间
15. time.localtime(\[secs\]):接收时间戳并返回当地时间下的时间元组t
