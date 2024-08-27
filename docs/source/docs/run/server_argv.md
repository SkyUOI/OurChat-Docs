# 服务器参数

| name                           |                                  usage |   default |
| :----------------------------- | -------------------------------------: | --------: |
| `--cfg config file path`       |  选择配置文件.[example](#配置文件示例) |    不适用 |
| `--test-mode`                  | 以测试模式启动服务器，仅供开发调试使用 |     false |
| `--clear`                      |           在启动时清除服务器缓存和日志 |     false |
| `--port=server listening port` |                       服务器监听的端口 |      7777 |
| `--ip=server listening ip`     |                        服务器监听的 ip | 127.0.0.1 |
| `--db-type`                    |                         选择数据库类型 |     mysql |
| `--maintaining`                |         启动维护模式，不断发送维护信息 |     false |

## 配置文件示例

```toml
dbcfg = "config/database.json"
rediscfg = "config/redis_connect.json"
port = 7777
db_type = "mysql"
http_port = 7778
```

注意，当配置文件和命令行参数冲突时，以命令行参数覆盖配置文件参数

mysql 数据库配置文件示例:

```json
{
  "host": "db",
  "user": "root",
  "passwd": "123456",
  "db": "OurChat",
  "port": 3306
}
```

sqlite 数据库配置文件示例:

```json
{
  "path": "ourchat.db"
}
```

Redis 示例:

```json
{
  "host": "127.0.0.1",
  "port": 6379,
  "passwd": "123456",
  "user": "root"
}
```

所有的配置文件示例[请见](https://github.com/SkyUOI/OurChat/tree/main/config)
