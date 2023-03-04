## 通过 venv 操作虚拟环境
 **venv** 是python3.3标准库自带的虚拟环境库
 
### 创建虚拟环境
 ```bash
 python -m venv your_env_name  # -m 把模块当作脚本运行
 ```
### 激活虚拟环境
```bash
source <环境名称>/bin/activate
```
### 关闭虚拟环境
```bash
deactivate
```

## 通过anaconda 创建虚拟环境
需要先安装 anaconda
### 创建虚拟环境，同时指定python使用3.8版本
```bash
conda create -n my_python3.8_env python=3.8
```
### 激活 anaconda 虚拟环境
```bash
source activate my_python3.8_env 
# 或者
conda activate my_python3.8_env 
```
### 关闭虚拟环境
```bash
conda deactivate
```
### 其它conda常用命令
```bash
# 列出有那些环境
conda env list

# 删除虚拟环境
conda env remove -n env_name

#更新 conda
conda update conda


```

# 安装openai
```bash
pip install openai
```

# 运行例子
```python
python test.py
```

