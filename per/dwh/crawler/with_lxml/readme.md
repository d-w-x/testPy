# 使用lxml库

## 基本使用:

```python
from lxml import etree

parser = etree.HTMLParser(encoding="UTF-8")
html = etree.parse("tencent.html", parser=parser)
result = html.xpath("xPath_language")
```

上述代码等价于`html = etree.HTML("tencent.html")`，使用不严格的HTML解析。

注意:
- 一般结果是[列表](../../Built_in_Types/iterable_types/list/readme.md#list)
- 一般可以进行多次解析: `result2 = result.xpath(another_path)`
- 少数情况下不可解析: 上次解析到文本内容，属性值等。

## xPath语法:

### 选取节点:

| 表达式    | 描述                                              |
|:---------|:-------------------------------------------------|
| nodename | 选取此节点的所有子节点。                             |
| /        | 从根节点选取。                                     |
| //       | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 |
| .        | 选取当前节点。                                     |
| ..       | 选取当前节点的父节点。                               |
| @        | 选取属性。                                         |

### 谓语:

| 表达式                             | 描述                                   |
|:----------------------------------|:--------------------------------------|
| `fatherPath / path[x]`            | 父节点下第x个`path`                     |
| `fatherPath / path[last()]`       | 父节点下最后一个`path`                   |
| `fatherPath / path[last()-x]`     | 父节点下倒数第x+1个`path`                |
| `fatherPath / path[position()<x]` | 父节点前第x个`path`                     |
| `fatherPath / path[value>x]`      | 父节点下满足 子节点的value值大于x 的`path` |
| `path[@value]`                    | 拥有value属性的`path`                   |
| `path[@value="value"]`            | value属性的值为"value"的`path`          |
| `path / @value`                   | `path`的value值                        |
| `path / text()`                   | `path`的内容                           |

### 通配符:

| 通配符  | 描述               |
|:-------|:------------------|
| \*     | 匹配任何元素节点。   |
| @\*    | 匹配任何属性节点。   |
| node() | 匹配任何类型的节点。 |

### 运算符:

| 运算符 | 功能 |
|:------|:----|
| \|    | 并集 |
| div   | 除法 |
| or    | 或  |
| and   | 和  |
| mod   | 求余 |

### 轴选取:

| 轴名称              | 结果                                             |
|:-------------------|:------------------------------------------------|
| ancestor           | 选取当前节点的所有先辈（父、祖父等）。                |
| ancestor-or-self   | 选取当前节点的所有先辈（父、祖父等）以及当前节点本身。   |
| attribute          | 选取当前节点的所有属性。                            |
| child              | 选取当前节点的所有子元素。                          |
| descendant         | 选取当前节点的所有后代元素（子、孙等）。               |
| descendant-or-self | 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。 |
| following          | 选取文档中当前节点的结束标签之后的所有节点。           |
| namespace          | 选取当前节点的所有命名空间节点。                     |
| parent             | 选取当前节点的父节点。                              |
| preceding          | 选取文档中当前节点的开始标签之前的所有节点。           |
| preceding-sibling  | 选取当前节点之前的所有同级节点。                     |
| self               | 选取当前节点。                                    |

使用轴:`name::range`，如:`child::text()`\:子节点的文本；`attribute::*`\:当前节点属性。