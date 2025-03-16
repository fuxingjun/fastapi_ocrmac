# fastapi 调用 ocrmac
将苹果的本地ocr变成一个http服务

### 运行
```bash

# 安装依赖(推荐使用venv)
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 启动
python main.py

```

### 关于虚拟环境
使用pycharm可以很方便的创建, 没有pycharm的话使用以下命令

```bash
# 创建一个名为venv的虚拟环境, 注意python可以使用默认的全局版本, 也可以改为目标版本的绝对路径(例如 C:\Python310\python.exe)
python -m venv venv

# 激活虚拟环境
# windows
.\venv\Scripts\activate
# mac
source venv/bin/activate 
# 退出虚拟环境
deactivate

```


### todo
