# 开发基本注意事项

## 脚本

我们提供了一系列脚本，帮助您处理日常简单事物。

### 运行集成测试

你可以运行`script/test_server.py`脚本来运行测试，第二个参数为自定义化的测试命令，默认为`cargo test`。**如果不使用该脚本，使用`cargo test`运行前，要先设置好 OURCHAT_CONFIG_PATH 环境变量**

## 文档

请善用`cargo doc`，我们为你提供了详尽的文档参考！调用`cargo doc --document-private-items`来生成私有的文档

## 前置依赖

- [Rust Compiler](https://rust-lang.org)
- [buf](https://buf.build/)
- [protobuf compiler](https://github.com/protocolbuffers/protobuf)
