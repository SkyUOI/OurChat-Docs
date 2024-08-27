# 开发基本注意事项

## 脚本

我们提供了一系列脚本，帮助您处理日常简单事物。

你可以运行`script/test_server.py`脚本来运行测试，默认会选择同目录下下的`server_test.json`作为配置文件，也可以通过`test_server.py xxx`的方式来指定，从而进行服务端测试的自定义。**注意：测试不能直接`cargo test`运行！**

## 测试

由于服务端测试具有特殊性，我们引入了一个`test_lib`模块用于辅助测试，具体可以参考已有的单元测试。

## 文档

请善用`cargo doc`，我们为你提供了详尽的文档参考！调用`cargo doc --document-private-items`来生成私有的文档
