创建虚拟环境 venv 和 anaconda 二选一，推荐**anaconda**
## 一、通过 venv 操作虚拟环境
 **venv** 是python3.3标准库自带的虚拟环境库
 
#### 创建虚拟环境
 ```bash
 python -m venv your_env_name  # -m 把模块当作脚本运行
 ```
#### 激活虚拟环境
```bash
source <环境名称>/bin/activate
```
#### 关闭虚拟环境
```bash
deactivate
```

## 二、通过anaconda 创建虚拟环境
需要先安装 anaconda
#### 创建虚拟环境，同时指定python使用3.8版本
```bash
conda create -n my_python3.8_env python=3.8
```
#### 激活 anaconda 虚拟环境
```bash
source activate my_python3.8_env 
# 或者
conda activate my_python3.8_env 
```
#### 关闭虚拟环境
```bash
conda deactivate
```
#### 其它conda常用命令
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


# faq

#### error: metadata-generation-failed
````
error: subprocess-exited-with-error

  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [1 lines of output]
      ERROR: Can not execute `setup.py` since setuptools is not available in the build environment.
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.
````
By running `pip install setuptools --upgrade` fixed the version with Successfully installed setuptools-67.2.0