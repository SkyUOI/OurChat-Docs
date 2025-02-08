# 服务器参数

| name                                     |                     usage |   default |
|:-----------------------------------------|--------------------------:|----------:|
| `--config config file path`              | 选择配置文件.[example](#配置文件示例) |       不适用 |
| `--test-mode`                            |       以测试模式启动服务器，仅供开发调试使用 |     false |
| `--clear`                                |            在启动时清除服务器缓存和日志 |     false |
| `--port=server listening port`           |                  服务器监听的端口 |      7777 |
| `--http-port=http server listening port` |             http 服务器监听的端口 |      7778 |
| `--ip=server listening ip`               |                 服务器监听的 ip | 127.0.0.1 |
| `--db-type`                              |                   选择数据库类型 |     mysql |
| `--maintaining`                          |           启动维护模式，不断发送维护信息 |     false |
| `--enable-cmd`                           |                  是否启用 cmd |      true |

## 配置文件示例

注意，当配置文件和命令行参数冲突时，以命令行参数覆盖配置文件参数

注意，配置文件格式支持多样，包括`toml`,`json`,`json5`,`yaml`,`ini`等，请自行选择熟悉的配置文件格式

- [配置文件示例](https://github.com/SkyUOI/OurChat/tree/main/config)

## 日志

默认日志等级为`info`，可以通过`OURCHAT_LOG`环境变量配置，支持的等级为`trace`,`debug`,`info`,`warn`,`error`，日志储存路径在`log`文件夹下，以时间命名日志文件

日志会定时清理，清理时间设定在`auto_clean_duration`中，也可以通过控制台指令更改

### 测试日志

`test_mode`启用时，日志不会被输出到文件中，并且测试等级会被默认调整到`trace`
