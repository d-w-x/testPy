# Sequence Types

- 常见操作：下表中s和t是两个同类序列；n，i，j，k是数字；x是元素

  | 操作符                    | 作用                                                      | 说明                              |
  |:-------------------------|:---------------------------------------------------------|:---------------------------------|
  | x in s                   | s中某一个等于x                                             | 同时支持string等                   |
  | x not in s               |                                                          |                                  |
  | s + t                    | 并集                                                      | `range`不支持                     |
  | s \* n or n \* s         |                                                          | 空集合也可以乘,`range`不支持         |
  | s\[i\]                   |                                                          |                                  |
  | s\[i\:j\]                |                                                          | 如果是负数，那么是相对于尾偏移值；-0=0 |
  | s\[i\:j\:k\]             | 步长为k                                                   |                                  |
  | len(s)                   |                                                          |                                  |
  | min(s)                   |                                                          |                                  |
  | max(s)                   |                                                          |                                  |
  | s.index(x\[, i\[, j\]\]) | 在i之后j之前出现第一个x的位置,`ValueError: 1 is not in List` |                                  |
  | s.count(x)               |                                                          |                                  |

- 相同类型的序列也支持比较。
  - 字典序比较
  - 如果相等，必须长度，类型，元素内容完全相等

- 连接不可变序列导致新对象的产生。
  - str:构建列表并使用[str.join()](../../iterable_types/strings/readme.md#string的其他方法 )
  - bytes:bytes.join()，或者使用`bytearray`
  - tuple:替换为List

## 不可变序列

含有对`hash()`的支持，因此允许作为dict的key。

## 可变序列

s是可变序列，t是序列，x是任意对象，则有以下操作：

| 操作                       | 结果                                   | 说明                         |
|:--------------------------|:--------------------------------------|:-----------------------------|
| `s[i] = x`                | 替换                                   |                              |
| `s[i:j] = t`              | 序列替换                               |                              |
| `del s[i:j]`              | 等价于`s[i:j] = []`                    |                              |
| `s[i:j:k] = t`            | `s[i:j:k]` 的元素被t中元素依次替换        | t长度必须相同                  |
| `del s[i:j:k]`            |                                       |                              |
| `s.append(x)`             | 末尾追加，等价于`s[len(s):len(s)] = [x]` |                              |
| `s.clear()`               | 删除全部                               |                              |
| `s.copy()`                | 浅拷贝，等价于`s[:]`                    |                              |
| `s.extend(t)` or `s += t` | 末尾追加t，等价于`s[len(s):len(s)] = t`  |                              |
| `s *= n`                  |                                       |                              |
| `s.insert(i, x)`          | `s[i:i] = [x]`)                       |                              |
| `s.pop([i])`              | 出栈                                   | i默认-1，即移除栈顶            |
| `s.remove(x)`             |                                       | 当未检索到x时，产生`ValueError` |
| `s.reverse()`             |                                       | 将自身逆转而不返回值            |

## List

是[可变序列](#可变序列)

- 构造List：
  - 用`[]`表示空项目
  - 用`[,]`表示和分割
  - 用列表构造：`[x for x in iterable]`
  - 构造函数：`List()` or `List(iterable)`

- List额外方法:
  - `sort(*, key=None, reverse=False)`:只使用`<`比较；`keyword-only
    arguments`:
    - key -- 进行比较的元素，只有一个参数，是lambda表达式。
    - reverse -- 排序规则，`reverse = True`降序，`reverse =
      False`升序（默认）。

## tuple

是[不可变序列](#不可变序列)

- 构造tuple：
  - 空元组：`()`
  - 单元组：`a,` or `(a,)`
  - 用逗号分隔元素：`a, b, c` or `(a, b, c)`
  - 构造方法：`tuple()` or `tuple(iterable)`

- 注意：
  - 实际上是逗号构成了一个元组，而不是括号。
  - 括号是避免误解：`f(a, b, c)`三参函数，`f((a, b, c))`一元组参函数。

## range

是[不可变序列](#不可变序列)

- 构造
  - `range(stop)`:从0开始。
  - `class range(start, stop)`：步长是1。
  - `class range(start, stop, step)`

- 注意
  - 只保存start, stop 和 step 三个值，占用内存很低。
  - `==`比较的是实际内容：`range(0) == range(2, 1, 3)`
