## 运行环境配置
### 配置conda
在命令行中执行
```
conda config --add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/'
conda config --set show_channel_urls yes
```


### 配置pip
将以下字段放在 ~/.pip/pip.conf 里面
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

[list]
format=columns
```

### Python 3 环境构建
`conda create --name py3dev python=3`

### 切换环境
`source activate py3dev`

### 安装必要软件包
`pip install -r requirements.txt`

### 命令行环境下
`python server.py`


## Pycharm 配置
### 新环境的 python 命令位置在
`$anaconda_home$/envs/py3dev/bin/python`

### 设置
设置->Project:Interpreter，选择上面的新命令即可

