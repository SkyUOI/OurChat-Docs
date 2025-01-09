# 开发基本注意事项

## 脚本

我们提供了一系列脚本，帮助您处理日常简单事物，参考[脚本说明](https://github.com/SkyUOI/OurChat/blob/main/script/README.md)。

### 运行集成测试

首先要设置环境变量，为了方便起见，我们支持`.env`的方式来设置环境变量，提供了一个[简单模板](https://github.com/SkyUOI/OurChat/blob/main/.env.template)，或者可以通过设置`OURCHAT_TEST_CONFIG_DIR`变量指向存有配置文件的目录。然后如正常 rust 项目运行`cargo test`即可运行测试

## 文档

请善用`cargo doc`，我们为你提供了详尽的文档参考！调用`cargo doc --document-private-items`来生成私有的文档

## 前置依赖

- [Rust Compiler](https://rust-lang.org)
- [buf](https://buf.build/)
- [protobuf compiler](https://github.com/protocolbuffers/protobuf)
