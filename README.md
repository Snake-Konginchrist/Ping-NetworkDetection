# PING自动化探测工具

## 项目简介
PING自动化探测工具是一个基于Flask搭建的网络探测应用，用于自动执行PING命令并记录结果。该工具允许用户选择探测间隔并开始或停止探测任务。探测结果会被记录在一个文本文件中，并且可以通过页面实时查看。

## 功能特点
- 执行PING命令来探测指定目标的网络连通性。
- 支持选择不同的探测间隔，包括30分钟、1小时、6小时、12小时和24小时（可以自行修改）。
- 可以通过页面开始或停止探测任务。
- 实时记录探测结果，并在页面上显示最新的结果。
- 结果记录包括时间戳、PING目标、PING结果和统计信息。

## 使用方法
1. 打开应用后，在页面上输入要探测的目标域名或IP地址。
2. 从下拉菜单中选择探测间隔。
3. 点击“开始探测”按钮开始PING探测任务。
4. 等待探测结果即可在页面上实时显示。
5. 可以随时点击“停止探测”按钮停止探测任务。

## 技术实现
- 后端使用 Python Flask 框架搭建，通过调用系统命令执行PING操作，并记录结果。
- 前端使用 HTML、CSS 和 JavaScript 实现页面交互和结果展示。
- 使用了多线程来异步执行PING任务，保证不阻塞应用主线程。

## 运行环境
- Python 3.x
- Flask
- 前端浏览器

## 项目结构
```
Ping-NetworkDetection/
│
├── app.py                # Flask应用入口文件
├── diagnostics.py        # 控制PING任务的模块
├── logger.py             # 记录和获取PING结果的模块
├── static/               # 存放静态资源文件（如CSS和JavaScript）
│   └── style.css         # 样式文件
│   └── script.js         # JavaScript脚本
└── templates/            # 存放HTML模板文件
    └── index.html        # 应用主页面模板
```

## 启动应用
1. 安装所需的Python依赖库：
   ```
   pip install flask
   ```
2. 在终端中进入项目目录，并运行以下命令：
   ```
   python app.py
   ```
3. 在浏览器中打开 `http://localhost:5000` 即可访问应用（可以在app.py里面改成你喜欢的端口）。

## 注意事项
- 在diagnostics.py文件中，请根据Windows还是Linux系统选择合适的代码
- Windows的`ping -n 4 domain.com`命令运行需要管理员权限，如果嫌麻烦可以自行改成`ping domain.com`
- Linux的`ping -c 4 domain.com`命令不是root也可以运行

---

根据实际情况，你可能需要对其中的内容进行调整或补充。