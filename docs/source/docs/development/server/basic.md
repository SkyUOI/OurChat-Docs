# 开发基本注意事项

## 脚本

我们提供了一系列脚本，帮助您处理日常简单事物，参考[脚本说明](https://github.com/SkyUOI/OurChat/blob/main/script/README.md)。

### 运行集成测试

首先要设置环境变量，为了方便起见，我们支持`.env`的方式来设置环境变量，提供了一个[简单模板](https://github.com/SkyUOI/OurChat/blob/main/.env.template)，或者可以通过设置`OURCHAT_CONFIG_FILE`变量指向存有配置文件的目录。然后如正常 rust 项目运行`cargo test`即可运行测试

## 文档

请善用`cargo doc`，我们为你提供了详尽的文档参考！调用`cargo doc --document-private-items`来生成私有的文档

## 前置依赖

- [Rust Compiler](https://rust-lang.org)
- [buf](https://buf.build/) (为了格式化和检测.proto 文件，可选)
- [protobuf compiler](https://github.com/protocolbuffers/protobuf)

## 优化开发体验

由于全部分析索引 workspace 中的所有 crate 对您的计算机是一种很大的负担，尤其是您很可能只会在其中几个 crate 上工作的情况下，我们强烈建议您使用如下配置，在 vscode 中:

```json5
{
  "rust-analyzer.files.exclude": [
    "server/migration", // example
  ],
}
```
