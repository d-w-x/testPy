# scrapy

## 创建项目

1. `scrapy startproject [name]`
2. `cd [name]`
3. `scrapy genspider spider_name "URL"`


## 结构

1. items\:爬虫得到的数据模型
2. middlewares\:中间件,用于处理代理，更换请求头等
3. pipelines\:模型本地化
4. settings\:爬虫配置信息
5. scrapy\:配置文件
6. spiders\:实际爬虫


## 使用

1. response\:`scrapy.http.HtmlResponse`可以执行`xpath()`和`css()`方法
2. 不规范时使用`beautifulsoup`
3. 数据是`scrapy.selector.unified.Selector`或者`SelectorList`类型
   1. getAll()返回所有文本的列表
   2. get()返回单个文本
4. 数据在`items`中建立bean，使用`[name] = scrapy.Field()`的固定格式
5. 在Spider中yield数据，由pipelines的`process_item`函数接受
   1. `open_spider(self, spider)`\开启爬虫时调用
   2. `close_spider(self, spider)`\:关闭爬虫时调用
6. 在settings中配置`ITEM_PIPELINES`声明pipelines和优先级
7. `scrapy.exporters`有相应的导入器\:
   1. `__init__`方法:`self.exporter = CsvItemExporter(file=self.fp,
      include_headers_line=False)` & `self.exporter.start_exporting()`
   2. `process_item`方法:`self.exporter.export_item(item)`
   3. `close_spider`方法:`self.exporter.finish_exporting()`

## crawl spider

1. 使用\:`scrapy genspider -t crawl spider_name "URL"`
2. LinkExtractors\:提取链接，调用的是extract_links(),其提供了过滤器(filter),以便于提取包括符合正则表达式的链接。

   | 属性                                     | 作用                                                                             |
   |:----------------------------------------|:--------------------------------------------------------------------------------|
   | `allow(a (list of) regular expression)` | 匹配正则表达式的URL被提取｡如果没有给出,匹配所有的链接｡                                  |
   | `deny(a (list of) regular expression)`  | 排除正则表达式的URL,优先级高于 allow 的参数｡如果没有给出, 将不排除任何链接｡               |
   | `allow_domains(str or list)`            | 被提取的domains｡                                                                 |
   | `deny_domains(str or list)`             | 不被提取的domains｡                                                                |
   | `deny_extensions(list)`                 | 可以忽略扩展名的列表｡默认为 scrapy.linkextractor 模块中定义的 IGNORED_EXTENSIONS 列表｡ |
   | `restrict_xpaths(str or list)`          | XPath的选择的文本将被扫描的链接｡                                                    |
   | `tags(str or list)`                     | 提取链接时要考虑的标记｡默认为( 'a' , 'area') ｡                                       |
   | `attrs(list)`                           | 提取链接时应该寻找的attrbitues列表(仅在 tag 参数中指定的标签)｡默认为 ('href')｡           |
   | `canonicalize(boolean)`                 | 规范化每次提取的URL(使用scrapy.utils.url.canonicalize_url )｡默认为 True ｡            |
   | `unique(boolean)`                       | 重复过滤是否应适用于提取的链接｡                                                      |
   | `process_value(callable)`               |                                                                                 |

3. Rules:在rules中包含一个或多个Rule对象，每个Rule对爬取网站的动作定义了特定操作。如果多个rule匹配了相同的链接，则使用第一个。
   1. callback\:从link_extractor中每获取到链接时，参数所指定的值作为回调函数，该回调函数接受一个response作为其第一个参数。
      1. 注意\:当编写爬虫规则时，避免使用parse作为回调函数。CrawlSpider使用parse方法来实现其逻辑，如果覆盖了parse方法，crawl
         spider将会运行失败。
   2. follow\:指定根据规则从response提取的链接是否需要跟进。如果callback为None，follow
      默认设置为True ，否则默认为False。
   3. process_links\:指定该spider中哪个的函数将会被调用，从link_extractor中获取到链接列表时将会调用该函数。该方法主要用来过滤。
   4. process_request\:指定该spider中哪个的函数将会被调用，该规则提取到每个request时都会调用该函数。
      (用来过滤request)
4. 数据写入在回调函数中yield.

## Scrapy Shell

在目录下使用`scrapy shell URL`启动终端，可以执行一些简单的命令.

如果是在项目中打开的，那么项目的配置文件会自动被读取。


## 补充

1. 如果起始需要发送表单\:在spiders类中重写`start_requests`方法

```python
import scrapy


def start_requests(self):
    URL = "https://baidu.com"
    data = {
        "username": "um",
        "password": "pd"
    }
    request = scrapy.FormRequest(url=URL, formdata=data, callback="parse_page")
    yield request

def parse_page():
    pass
```

2. 文件下载
   1. Item中设置两个属性\:`file_urls`,定义文件的来源;`files`,存储下载后的信息如文件路径，校验码等.
   2. `settings.py`:配置`FILES_STORE`设置路径.
   3. `settings.py`配置`ITEM_PIPELINES`中注册`"scrapy.pipelines.files.FliesPipeline":1`
   4. 使用spider，注意`file_urls`的值必须是列表.

3. 图片下载:
   1. 将上述的file全部替换为image
   2. 提供了更多的功能

4. 自定义下载管道
   1. 在pipelines中新建`MyFilePipeline(FilesPipeline)`类，重写`file_path()`方法
   2. `settings.py`配置`ITEM_PIPELINES`中注册自己的`MyFilePipeline`

## 使用中间件

1. `process_request(self,request,spider)`:在请求前调用
2. ·
3. 在`settings.py`中打开`DOWNLOADER_MIDDLEWARES = {
   'test_scr.middlewares.XXXDownloaderMiddleware': 1, }`
