# 如何构建该项目

## Server

开发构建，请见[服务端开发](../development/server/server-develop.md)

对于真正部署到生产环境，参见[部署指南](../deploy/server-deploy.md)

## client-pc

**_考虑到性能和人力成本问题，我们决定终止py客户端的开发，改用Flutter开发客户端_**

client-pc 部分由 python 编写，要求是 python3 以上以及[rust环境](https://www.rust-lang.org/tools/install)(编译rmodule库),通过以下命令进行安装和运行

### 运行

```bash
python -m pip install -r client/pc/requirement.txt # 安装依赖库
python script/export_themes.py # 导出主题到client/pc/src/theme中
cd ./client/pc/src/rmodule
maturin develop # 编译rmodule库
cd ..
python main.py # 运行
```

### 打包为可执行文件

```bash
cd ./client/pc/src/rmodule
maturin build --release # 编译rmodule库
python script/build_pc.py
```

等待脚本运行完毕后，`client/pc/src/out/main.dist`目录中即为可执行文件及其依赖文件
