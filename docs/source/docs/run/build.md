# 如何构建该项目

## Server

开发构建，请见[服务端开发](../development/server/server-develop.md)

对于真正部署到生产环境，参见[部署指南](../deploy/server-deploy.md)

## client-pc

**_考虑到性能和人力成本问题，我们决定终止 py 客户端的开发，改用[Flutter 开发客户端](#flutter-版客户端)_**

## Flutter 版客户端

### 环境配置

在下面选择你的操作系统进入配置教程安装 Flutter

- [Windows](https://docs.flutter.cn/get-started/install/windows/desktop)
- [Linux](https://docs.flutter.cn/get-started/install/linux/desktop)
- [MacOS](https://docs.flutter.cn/get-started/install/macos/desktop)

### 安装protoc

详情参见[官方文档](https://grpc.io/docs/languages/dart/quickstart/)

从[Github](https://github.com/google/protobuf/releases)下载官方编译版本的`Protobuf` 它将用于编译`proto`文件

将下载的文件解压在任意位置**并添加到环境变量**

### 安装dart的protoc编译插件

详情参见[官方文档](https://grpc.io/docs/languages/dart/quickstart/)

```bash
dart pub global activate protoc_plugin
```

将Pub缓存路径添加到环境变量中

若你是Windows用户，则默认路径为`C:/Users/%username%/AppData/Local/Pub/Cache/bin`

若你是Mac/Linux用户，则应添加`~/.pub-cache/bin`至环境变量

### 安装依赖

```bash
cd ./client/pc/ourchat # 进入目录
flutter pub get # 安装依赖
```

### 生成代码

在本项目根目录下运行

```bash
# 生成grpc service相关代码
python ./script/generate.pb.dart.py
# 获取about界面相关信息
python ./script/generate_about_code.py --afdian_userid userid --afdian_token token --version v0.1.0.beta --commit_sha 123456abc
```

| 参数 | 含义 |可选|
|-----|------|---|
|afdian_userid|爱发电平台的userId，用于获取捐献者列表| ● |
|afdian_token|爱发电平台的token，用于获取捐献者列表| ● |
|version|当前版本的版本号|×|
|commit_sha|当前版本的commit_sha|×|

等待完成后进入客户端目录并运行

```bash
cd ./client # 进入客户端目录
# 生成数据库ORM相关代码
dart run build_runner build
```

### 运行项目

```bash
cd ./client # 进入客户端目录
flutter run

# 会出现如下界面，选择你希望运行的平台即可
> Connected devices:
> Windows (desktop) • windows • windows-x64    • Microsoft Windows [版本 xxx]
> Chrome (web)      • chrome  • web-javascript • Google Chrome xxx
> Edge (web)        • edge    • web-javascript • Microsoft Edge xxx
> [1]: Windows (windows)
> [2]: Chrome (chrome)
> [3]: Edge (edge)
> Please choose one (or "q" to quit):
```

### 构建为可执行文件

#### 构建APK并签名

我们强烈建议构建apk时为其签名，若您暂时不打算签名，可直接跳至常规构建

你需要准备：

- 密钥库文件及密钥
- 脑子

将密钥库文件复制到`client/android/app`下，并在同目录下新建`key.properties`文件，内容为：

```
storePassword = <storePassword>
keyPassword = <keyPassword>
keyAlias = key
storeFile = <storeFile>
```

例如

```
storePassword = test123
keyPassword = test123
keyAlias = key
storeFile = key.jks
```

接下来只需在`client`目录下执行

```bash
flutter build apk --release -PuseReleaseSigning=true
```

#### 常规构建

进入客户端目录并运行项目

```bash
cd ./client # 进入目录
flutter build # 查看可供构建的平台

# 会出现可构建的平台列表，如：
> Available subcommands:
>   aar         Build a repository containing an AAR and a POM file.
>   apk         Build an Android APK file from your app.
>   appbundle   Build an Android App Bundle file from your app.
>   bundle      Build the Flutter assets directory from your app.
>   web         Build a web application bundle.
>   windows     Build a Windows desktop application.

# 选择你想要构建的平台即可，这里选择windows为例
flutter build windows

# 构建完成后会显示可执行文件的目录
```
