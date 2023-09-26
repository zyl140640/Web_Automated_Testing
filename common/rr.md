## 自动化测试工具调研

### 什么是 UI 自动化测试？

模拟用户在页面上进行操作(点击、输入、滑动)

### 自动化测试工具比较

市面上主流的自动化测试框架：
Playwright Selenium Puppeteer Cypress

## 关键对比

通过各个维度方向去进行比较

### 支持语言

- Playwright 支持主流语言：javaScript&TypeScript\Python\C#\GO\Java
- Selenium 支持主流语言：Java\Python\Ruby\C#\C++\JavaScript
- Cypress 只支持 JavaScript & Typescript
- Puppeteer 只支持 JavaScript & Typescript

<h4>浏览器覆盖(支持)</h4>

- Playwright 支持 Chromium/Webkit/Firefox
- Selenium 支持运行在目前所有主流浏览器上 (不包括国内套皮的浏览器)
- Cypress 只支持 Chromium/Firefox
- Puppeteer 只支持 Chromium/Firefox

<h4>支持多标签+表单</h4>

- Playwright 支持，并且代码简洁易用
- Selenium 只能通过 swith_to 切换，但是特别难用
- Cypress 没有真正支持
- Puppeteer 支持，并且代码简洁易用

<h4>脚本调试</h4>

- Playwright 支持，有界面，可单步执行进行调试
- Selenium 不支持，只能通过代码编写软件进行排查
- Cypress 不支持
- Puppeteer 不支持

<h4>远程执行</h4>

- Playwright 只能自己构建
- Selenium 自己构建或者托管
- Cypress 自己构建或者付费
- Puppeteer 只能自己构建

<h4>稳定性</h4>

- Playwright 自带自动等待机制，特定元素需要手动加等待时间
- Selenium 复杂的自动等待机制，需要自己封装，而且不太稳定
- Cypress 复杂的机制，并且不能与测试框架一起工作
- Puppeteer 只能手动等待其他元素（设置时间，等待页面元素全部加载）

<h4>智能定位(定位页面元素)</h4>

- Playwright 支持自定义选择器引擎，支持多种定位方式选择元素
- Selenium 不支持以多种方式选择元素
- Cypress 不支持以多种方式选择元素
- Puppeteer 不支持以多种方式选择元素

<h4>文档和资源</h4>

- Playwright 工具比较新，是微软公司在 2020 年初发布的，API 在变化，文档教程可能会导致跟不上
- Selenium 官方文档写的很差，到那时第三方资料很丰富，也有相关书籍可查阅
- Cypress 社区很小，官方文档清晰
- Puppeteer 社区很小，教程也很多

综合评分：范围 1-5 分值越高说明越优秀

| 类别       | Playwright | Selenium | Cypress | Puppeteer |
|----------|:----------:|:--------:|:-------:|:---------:|
| 支持语言     |     4      |    5     |    1    |     1     |
| 浏览器覆盖    |     3      |    5     |    2    |     2     |
| 支持多标签&表单 |     5      |    3     |    0    |     5     |
| 远程执行     |     0      |    4     |    2    |     0     |
| 稳定性      |     4      |    3     |    3    |     3     |
| 智能定位     |     3      |    2     |    2    |     2     |
| 脚本调试     |     3      |    2     |    3    |     2     |
| 文档和资源    |     3      |    4     |    4    |     3     |

### 目前搭建的 Web 自动化测试框架结构: Python+Pytest+Playwright+Yaml+Allure

| 工具         | 说明      |
|------------|---------|
| Python     | 编写语言    |
| Pytest     | 单元测试框架  |
| Playwright | UI 自动化库 |
| Yaml       | 存储测试数据  |
| Allure     | 测试报告    |

### 为什么选择 Playwright

1. 其他需要通过 WebDriver(浏览器驱动)操作浏览器；Playwright 内置浏览器驱动，不需要再次配置
2. Playwright 几乎支持所有语言，且不依赖于各种 Driver，通过调用内置浏览器所以启动速度更快。
3. Playwright 基于 Websocket（双向通讯）可自动获取浏览器实际情况。
4. Playwright 定位页面元素时会自动等待,能增加脚本的稳定性 。
5. Playwright 可以在测试执行中时，拦截网络活动(接口)
6. Playwright 带有用于选定移动设备的设备参数注册表，可用于模拟移动设备上的浏览器行为
7. Playwright 自带调试工具，可进行逐步执行进行查看和排查问题
8. Playwright 拥有捕获功能，在执行测试用例时可捕获所有信息以调查测试失败。（截屏、录屏、DOM、测试源等）

- 注： Pytest+Allure 都是目前自动化测试使用率最高的插件库 所以只讲为什么选择 Playwright

###环境资源：

- Docker、Jenkins、github、allure
- 注: 要使用Ubuntu 22.04 LTS 为何要用? 用于拉取Docker镜像
- 原: Firefox 和 WebKit 的浏览器构建是为 glibc 库构建的。不支持 Alpine Linux 和其他基于 musl 标准库的发行版。

### 接口自动化

- Pyhon+Request+Pytest+Yaml+allure

### 持续集成

- [Docker+Jenkins持续集成](https://zhuanlan.zhihu.com/p/615302968 "Docker+Jenkins持续集成")
- [Jenkins部署](https://blog.csdn.net/Faith_Lzt/article/details/126897268?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-126897268-blog-124362259.235^v38^pc_relevant_sort_base2&spm=1001.2101.3001.4242.2&utm_relevant_index=2 "Jenkins部署")
- [Playwright官网-GitLab持续集成](https://playwright.dev/python/docs/docker "Playwright官网-GitLab持续集成")
- [教程](https://www.bilibili.com/video/BV1jm4y1J7YY/?spm_id_from=333.788&vd_source=5f7b140343bf40195148b657c47941e4 "教程")

###禅道

1. 与禅道的兼容性是指？
   1.1. web自动化也好，接口自动化也好，跟禅道无任何关联项
   1.2. 如果需要与禅道进行关联，比如：自动化测试时测出问题，然后自动提交到禅道这个功能
   需要去查看禅道提交BugApi去封装、去实现。 但目前禅道官方API只维护到了禅道12版本（禅道开源版12.5.3、禅道企业版
   4.1.3及以下版本适用）。
