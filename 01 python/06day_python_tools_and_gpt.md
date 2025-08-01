# 第六天：Python工具与GPT实战

## 一、第三方库使用

### 1. requests —— 网络请求（抓数据/调用API）

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
```
**用法：**
- get/post/put/delete
- 搭配 API 调用（例如 OpenAI）

---

### 2. pillow —— 图像处理

```python
from PIL import Image

img = Image.open('example.jpg')
img = img.resize((100, 100))
img.save('resized.jpg')
```
**用法：**
- 图像裁剪、旋转、加水印、批量处理等

---

### 3. rich —— 命令行美化神器

```python
from rich.console import Console
console = Console()
console.print("Hello [bold magenta]World[/bold magenta]!", style="bold green")
```
**用法：**
- 打印彩色日志、表格、进度条、树形结构等

---

## 二、Python 打包为可执行脚本

**使用 pyinstaller**

安装：

```bash
pip install pyinstaller
```

打包：

```bash
pyinstaller your_script.py --onefile
```

输出：

- dist/your_script.exe（Windows）

可部署给没有 Python 环境的用户

**进阶技巧：**
- 加 logo 图标：`--icon=icon.ico`
- 隐藏控制台窗口：`--windowed`

---

## 三、结合 GPT API 构建智能应用

1. 安装 OpenAI 库

```bash
pip install openai
```

2. 使用 GPT 生成回答

```python
import openai

openai.api_key = "你的API Key"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "写一个关于AI的故事"}
    ]
)

print(response['choices'][0]['message']['content'])
```

**推荐用法：**
- 搭配 requests 实现通用调用
- 加入异常处理、缓存机制
- 用 tkinter、streamlit 做图形界面（GUI）

---

## 📚 今日任务建议

| 模块      | 目标                         | 推荐时长 |
| --------- | ---------------------------- | -------- |
| requests  | 熟练调用 API，如 GitHub 或天气接口 | 30min    |
| pillow    | 把一张图片批量处理并保存           | 30min    |
| rich      | 美化终端输出结果                   | 15min    |
| 打包      | 学会使用 pyinstaller              | 20min    |
| GPT API   | 成功调用并获取结果                 | 30min    |