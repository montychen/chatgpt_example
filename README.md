OpenAI的python接口版本要求： `python >= 3.9`, `openai的版本至少是0.27`

# 一、 创建虚拟环境 
venv 和 [anaconda](https://anaconda.org) 二选一，推荐**anaconda**
### 1、通过 venv 操作虚拟环境
 **venv** 是python3.3标准库自带的虚拟环境库
#### 创建虚拟环境
 ```bash
 python -m venv your_env_name  # -m 把模块当作脚本运行
 ```
#### 激活虚拟环境
```bash
source <环境名称>/bin/activate
````
```bash
deactivate
```

### 2、通过anaconda 创建虚拟环境
需要先安装 [anaconda](https://anaconda.org)
#### 创建虚拟环境，同时指定python使用3.8版本
```bash
conda create -n my_python3.10_env python=3.10
```
#### 激活 anaconda 虚拟环境
```bash
source activate my_python3.10_env 
# 或者
conda activate my_python3.10_env 
```
#### 关闭虚拟环境
```bash
conda deactivate
```
#### 列出有那些环境
```bash
conda env list
```

#### 删除虚拟环境
```bash
conda env remove -n env_name -all
```

#### 更新 conda
```bash
conda update -n base conda
```

#### 彻底删除 anaconda
1. 运行 `anaconda-clean`
    ```bash
    conda install anaconda-clean
    anaconda-clean
    ```
2. 删除Anaconda目录，Anaconda的安装文件都包含在一个目录中，所以直接将该目录删除即可。 `conda info` 可以查看到当初 anaconda 安装所在目录
3. 删除 `~/.bash_profile`中anaconda的环境变量，使用vim打开删除；Anaconda在安装的时候，会**自动**在`~/.bash_profile` 加入一些环境变量。


[参考这篇文章](https://blog.csdn.net/weixin_45277161/article/details/127817700)


# 二、安装openai
```bash
pip install openai
```

# 三、运行例子
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