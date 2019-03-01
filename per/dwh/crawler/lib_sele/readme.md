# selenium

> 获取ajax方式有两种方式:
> 1. 分析接口并访问\:比较难分析，可能有加密
>    1. 使用`selenium` + `Driver`访问


## 操作

`driver.close()`\:关闭当前页面;`driver.quit()`\:退出

### 定位元素

1. id定位\: `find_element_by_id()`
2. name定位\: `find_element_by_name()`
3. class定位\: `find_element_by_class_name()`
4. tag定位\: `find_element_by_tag_name()`
5. link定位\: `find_element_by_link_text()`
6. partial_link定位\: `find_element_by_partial_link_text()`
7. xpath定位\: `find_element_by_xpath()`
8. CSS定位\: `find_element_by_css_selector()`
9. 上述方法均可换为`find_element(By.XXX)`, `from
   selenium.webdriver.common.by import By`

### 操作标签

1. `input`
   1. `inputs.send_keys("key")`\:输入
   2. `inputs.clear()`\:清除
2. 复选框\:`box.click()`
3. 下拉框\:`from selenium.webdriver.support.select import Select`
   1. select_by_index\:通过索引定位
   2. select_by_value \:通过value(标签的一个属性值)值定位
   3. select_by_visible_text\:通过文本值(下拉框的值)定位
4. 按钮\:`button.click()`

### 行为链

`from selenium.webdriver.common.action_chains import ActionChains`

```python
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
action = ActionChains(driver)
inputs = driver.find_element_by_css_selector("kw")
action.move_to_element(inputs)
action.click()
action.perform()
driver.quit()
```

> 1. click(on_element=None) ——单击鼠标左键
> 2. click_and_hold(on_element=None) ——点击鼠标左键，不松开
> 3. context_click(on_element=None) ——点击鼠标右键
> 4. double_click(on_element=None) ——双击鼠标左键
> 5. drag_and_drop(source, target) ——拖拽到某个元素然后松开
> 6. drag_and_drop_by_offset(source, xoffset, yoffset)
>    ——拖拽到某个坐标然后松开
> 7. key_down(value, element=None) ——按下某个键盘上的键
> 8. key_up(value, element=None) ——松开某个键
> 9. move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
> 10. move_to_element(to_element) ——鼠标移动到某个元素>
> 11. move_to_element_with_offset(to_element, xoffset, yoffset)
>     ——移动到距某个元素（左上角坐标）多少距离的位置
> 12. perform() ——执行链中的所有动作
> 13. release(on_element=None) ——在某个元素位置松开鼠标左键
> 14. send_keys(*keys_to_send) ——发送某个键到当前焦点的元素
> 15. send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素

### cookie

1. `driver.get_cookies()`\:获取所有cookie
2. `driver.get_cookie(key)`\:由值获取某一个cookie
3. `driver.delete_all_cookies()`\删除所有cookie
4. `driver.delete_cookie(key)`\:删除key对应的cookie
5. 存取cookie使用`json.dump(cookies, file_pointer)` \&
   `json.load(cookies, file_pointer)`\&\&`driver.add_cookie(cookie)`

## 等待

1. 强制等待:`sleep(time)`
2. 隐性等待:`driver.implicitly_wait(time)`
3. 显性等待:`WebDriverWait()`

## 多页面

1. 使用执行脚本方式实现:`driver.execute_script("window.open('https://baidu.com')")`
2. 切换页面:`driver.switch_to.window(driver.window_handles[0])`


## 代理

```python
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
# =两边不能有空格
chromeOptions.add_argument("--proxy-server=http://ip:port")

browser = webdriver.Chrome(chrome_options = chromeOptions)
browser.get("http://httpbin.org/ip")
print(browser.page_source)

browser.quit()
```

