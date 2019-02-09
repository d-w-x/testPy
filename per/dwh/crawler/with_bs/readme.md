# 使用BeautifulSoup4库

## 解析器

| 解析器           | 使用方法                                                                 | 优势                                             | 劣势                                          |
|:----------------|:------------------------------------------------------------------------|:------------------------------------------------|:---------------------------------------------|
| Python标准库     | `BeautifulSoup(markup, "html.parser")`                                  | Python的内置标准库,执行速度适中,文档容错能力强        | Python 2.7.3 (or 3.2.2)前 的版本中文档容错能力差 |
| lxml HTML 解析器 | `BeautifulSoup(markup, "lxml")`                                         | 速度快,文档容错能力强                              | 需要安装C语言库                                |
| lxml XML 解析器  | `BeautifulSoup(markup, ["lxml", "xml"])`,`BeautifulSoup(markup, "xml")` | 速度快,唯一支持XML的解析器                          | 需要安装C语言库                                |
| html5lib        | `BeautifulSoup(markup, "html5lib")`                                     | 最好的容错性,以浏览器的方式解析文档,生成HTML5格式的文档 | 速度慢,不依赖外部扩展                           |

## 对象内容

1. `Tag`\: 标签.
   - `name`\:标签的名字，如果改变则影响所有通过当前Beautiful Soup对象生成的HTML文档.
   - `Attributes`\:标签的属性，操作与字典相同\:`tag['class']`，也可以点属性\:`tag.attrs`;tag的属性可以被添加,删除或修改,方式和字典相同.
   - 多值属性\:多值属性的返回类型是list;但如果HTML标准中从未定义一标签为多值标签，则将值一字符串返回.
2. `NavigableString`\:标签中的字符串.
   - `NavigableString`字符串与Python中的Unicode字符串相同,通过`unicode()`方法可以直接转换
   - Tag中包含的字符串不能编辑,用`replace_with()`方法可以被替换成其它的字符串.
3. `BeautifulSoup`\:表示的是一个文档的全部内容.大部分时候,可以把它当作`Tag`对象.
   - 没有name和attribute属性.
4. `Comment`\:注释.

## 遍历节点

必须是字符串.

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup("<html><head>123</head>data</html>")
head = soup.head
tag_contents = soup.contents
```

说明\:

1. 通过点取属性的方式只能获得当前名字的第一个tag.
2. `.contents`属性可以将tag的子节点以列表的方式输出.
3. 使用`.children`直接获取子节点;`.descendants`获取所有子节点.
4. `.string`可以用来获取`NavigableString`节点\:
   1. 如果tag只有一个`NavigableString`类型子节点,那么这个tag可以使用`.string`得到子节点.
   2. 如果一个tag仅有一个子节点,那么这个tag也可以使用`.string`方法,输出结果与当前唯一子节点的`.string`结果相同.
   3. 如果tag包含了多个子节点,tag就无法确定`.string`方法应该调用哪个子节点的内容,`.string`的输出结果是`None`.
   4. 如果tag包含了多个字符串，可以使用`.strings`获取列表;使用`.stripped_strings`可以去除多余空白内容.
5. `.parent`获取父节点;`.parents`自上递归父节点到根.
6. `.next_sibling`和`.previous_sibling`获取兄弟节点;`.next_siblings`和`.previous_siblings`属性可以对当前节点的兄弟节点迭代输出.
   1. 实际文档中的tag的`.next_sibling`和`.previous_sibling`属性通常是字符串或空白.
7. 按浏览器方式解析:`.next_element`和`.previous_element`;结果可能与`.*_sibling`相同,但通常是不一样的,一般会进入标签内部.

## 搜索节点

- 过滤器\:
  - 字符串,查找与字符串完整匹配的内容.
  - 正则表达式,使用`match()`来匹配内容.
  - 列表,与列表中任一元素匹配的内容返回.
  - True,可以匹配任何值.
  - 可以使用lambda表达式\:`lambda x: x.has_attr('class')`

- `find_all(name, attrs, recursive, text, **kwargs)`方法\:
  - name:查找所有名字为name的tag,[字符串对象](#对象内容)会被自动忽略掉.
  - attrs:
    - 按照css搜索:类`class`用`class_`代替;参数也可以是过滤器.单值时依次和多值比较;多值时匹配包括顺序
    - 给出`id`、`href`等未在参数列表的参数都被认为是tag的属性来搜索.
  - recursive:默认调用find_all()方法时,Beautiful
    Soup会检索当前tag的所有子孙节点;`recursive=False`关闭对子孙节点查询.
  - text:搜索字符串内容.
  - limit:使用`limit`参数限制返回结果的数量.
  - Beautiful Soup类实现了`__call__`方法，底层机制就是`find_all()`.

- `find(name, attrs, recursive, text, **kwargs)`方法\:
  - 结果而言，`find(*)`与`find_all(*,limit=1)`等价，性能比较高.
  - `find_all()`方法没有找到目标是返回空列表,`find()`方法找不到目标时,返回`None`.

- 其他find_all系列:
  - `find_parents()`&`find_parent()`:搜索当前节点的父辈节点.
  - `find_next_siblings()`&`find_next_sibling()`:符合条件的后面的兄弟节点.
  - `find_previous_siblings()`&`find_previous_sibling()`:符合条件的前面的兄弟节点.
  - `find_all_next()`和`find_next()`:下一节点.
  - `find_all_previous()`&`find_previous()`:前一节点.

- CSS选择器:`.select()`方法中传入字符串参数,即可使用CSS选择器的语法找到tag.

## 修改文档树

- 修改tag的名称和属性:字典形式.
- 修改.string:给.string赋值.
- `append()`:向tag中添加内容.
- `BeautifulSoup.new_string()`和`BeautifulSoup.new_tag()`:要创建一段注释,或`NavigableString`的任何子类,将子类作为`new_string()`方法的第二个参数传入;tag最好的方法是调用工厂方法`BeautifulSoup.new_tag()`.
- `insert()`:插入.
- `insert_before()`和`insert_after()`:分别在前和后插入.
- `clear()`:移除tag的内容.
- `extract()`:将当前tag移除文档树,并作为方法结果返回.
- `decompose()`:将当前节点移除文档树并完全销毁.
- `replace_with()`:移除文档树中的某段内容,并用新tag或文本节点替代它.
- `wrap()`:对指定的tag元素进行包装,并返回包装后的结果.
- `unwrap()`.

## 输出

- `prettify()`方法将Beautiful
  Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行.
- 如果只想得到结果字符串,不重视格式,那么可以对一个BeautifulSoup对象或Tag对象使用Python的`unicode()`或`str()`
- 将HTML中的特殊字符转换成Unicode,比如“&lquot;”.
- `get_text()`:获取到tag中包含的所有文本内容包括子孙tag中的内容,并将结果作为Unicode字符串返回;通过参数指定tag的文本内容的分隔符.
