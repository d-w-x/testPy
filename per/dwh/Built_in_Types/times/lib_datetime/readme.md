# pkg \: datetime

## date

构成为(年,月,日)，日期不对应月份会报错`ValueError`.

### 方法

- 类方法
  - `date(year, month, day)` \: 需要给出所有参数
  - `today()` \: 等价于`date.fromtimestamp(time.time())`
  - `fromtimestamp(timestamp)` \: 从系统零点的秒数
  - `fromordinal()` \: 从公元1年到现在的天数
  - `fromisoformat()` \: 将YYYY-MM-DD变成date类

- 实例方法
  - `replace(year=self.year, month=self.month, day=self.day)` \: 替换指定属性
  - `timetuple()` \: 返回时间元组
  - `toordinal()` \: 从公元0年到现在的天数
  - `weekday()` \: 星期数，星期一是0
  - `isoweekday()` \: 星期数，星期一是1
  - `isocalendar()` \: 返回三元组 \: (ISO year, ISO week number, ISO weekday)
  - `isoformat()` \: ‘YYYY-MM-DD’
  - `str(d)` \: 等价于 `d.isoformat()`
  - `strftime(format)` \:
    按给定格式输出字符串,具体参数参加[date](../lib_time/readme.md#方法)中的format
  - `__format__(format)` \: 等价上述

## datetime

- 构造方法
  - `datetime(year, month, day, hour=0, minute=0, second=0,
    microsecond=0, tzinfo=None, *, fold=0)`
    - MINYEAR <= year <= MAXYEAR,
    - 1 <= month <= 12,
    - 1 <= day <= number of days in the given month and year,
    - 0 <= hour < 24,
    - 0 <= minute < 60,
    - 0 <= second < 60,
    - 0 <= microsecond < 1000000,
    - fold in \[0, 1\].

- 类方法
  - `today()`
  - `now(tz=None)`
  - `utcnow()`
  - `fromtimestamp(timestamp, tz=None)`
  - `utcfromtimestamp(timestamp)`
  - `fromordinal(ordinal)`
  - `combine(date, time, tzinfo=self.tzinfo)` \:
    将`date`和`time`两个类合并成`datetime`
  - `fromisoformat(date_string)` \: `YYYY-MM-DD[*HH[ \: MM[ \:
    SS[.fff[fff]]]][+HH \: MM[ \: SS[.ffffff]]]]`
  - `strptime(date_string, format)`

- 实例方法
  - `date()` \: 'datetime.date'
  - `time()` \: 'datetime.time'
  - `timetz()`
  - `replace(year=self.year, month=self.month, day=self.day,
    hour=self.hour, minute=self.minute, second=self.second,
    microsecond=self.microsecond, tzinfo=self.tzinfo, * fold=0)`
  - `timetuple()`
  - `utctimetuple()`
  - `weekday()`
  - `isoweekday()`
  - `isocalendar()`
  - `isoformat(sep='t', timespec='auto')` \: `YYYY-MM-DDtHH \: MM \: SS`
    - t \: 对应日期和时间的空格
    - timespec \:
      - 'auto' \: Same as 'seconds' if microsecond is 0, same as
        'microseconds' otherwise.
      - 'hours' \: Include the hour in HH format.
      - 'minutes' \: Include hour and minute in HH\:MM format.
      - 'seconds' \: Include hour, minute, and second in HH\:MM\:SS
        format.
      - 'milliseconds' \: Include full time, but truncate fractional
        second part to milliseconds. HH\:MM\:SS.sss format.
      - 'microseconds' \: Include full time in HH\:MM\:SS.ffffff format.

## time

- 构造方法
  - `time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *,
    fold=0)`

- 类方法
  - `fromisoformat(time_string)`

- 实例方法
  - `replace(hour=self.hour, minute=self.minute, second=self.second,
    microsecond=self.microsecond, tzinfo=self.tzinfo, * fold=0)`
  - `isoformat(timespec='auto')`
