# 本地文档部署指南

该文档使用 Sphinx 作为文档生成器

## 环境配置

- Python: python3 以上即可
- Python包管理器：uv

首先，请生成虚拟环境并安装相关依赖：

```sh
uv sync
```

然后你需要激活虚拟环境。

## 生成文档

在`docs`目录下运行

```bash
make
```

即可查看所有可用的生成器

```bash
# OUTPUT
html        to make standalone HTML files
#...
```

使用

```bash
make target
```

即可生成指定类型的文档，生成完毕后请检查`build/target`目录

该文档默认语言为 en，如果你想要生成其他语言的文档，请设置环境变量`READTHEDOCS_LANGUAGE`。为了方便，我们提供了`generate.py`脚本。
目前支持语言:

- zh_CN
- en

### Example

例如: 生成`zh_CN`语言的`html`文档
使用`generate.py`脚本:

```bash
python generate.py zh_CN
```

或者，直接运行命令:

```bash
READTHEDOCS_LANGUAGE=zh_CN make html
```

文档将会生成在`build/html`目录中
