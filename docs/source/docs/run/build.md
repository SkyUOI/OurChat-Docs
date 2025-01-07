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

接下来进入客户端目录安装依赖包

```bash
cd ./client/pc/ourchat # 进入目录
flutter pub get # 安装依赖
```

### 运行项目

进入客户端目录并运行项目

```bash
cd ./client/pc/ourchat # 进入目录
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

进入客户端目录并运行项目

```bash
cd ./client/pc/ourchat # 进入目录
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
