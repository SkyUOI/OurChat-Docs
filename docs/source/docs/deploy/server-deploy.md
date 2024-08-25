# 服务端部署指南

- [Docker 部署](#docker推荐)
- [手动部署](#手动部署)
- [Sqlite 便携部署](#sqlite-便携部署)

## Docker(推荐)

对于该项目，我们提供了一个生产环境中使用的 dockerfile，可以直接构建并运行项目。

以下是具体操作步骤：

```bash
docker compose -f compose.prod.yml up -d
```

这一步完成只是创建了一个最基本的环境，但是安全性还远远没有达到，为了保证安全性，你需要修改 MySQL 和 Redis 的密码。

具体有以下几步:

- 修改`compose.prod.yml`中的两个`password`的`123456`为你自己的强密码
- 修改`config/database.json`为改后的 MySQL 密码，`config/redis_connection.json`为改后的 Redis 密码
- 再次运行`docker compose -f compose.prod.yml up -d`

完成这几步之后，你就成功部署了该项目。

对于容器中的数据，我们将其映射在了`mysql-data`和`redis-data`中，你可以随时保存数据

## 手动部署

对于性能不高和未安装 docker 的计算机，我们也提供了手动部署的文档，关于这一点，建议部署在 linux 环境，其他环境未经过严格的测试。

### 安装 mysql

mysql 版本为 9.0.1（如果该文档未及时更新可以查看`[compose.yml](https://github.com/SkyUOI/OurChat/blob/main/compose.yml)中的 mysql 版本）

### 安装 redis

可以直接安装最新版的 redis

### 安装 ourchat server

此处存在两种备选的方案:

1.(推荐)从 github release 下载最新的 linux 编译结果，此版本经过官方的 pgo 优化，性能会更高，如果遇到 CPU 架构和其他兼容性问题，可能需要手动编译，参见下一节

2.手动编译

- 拉取源代码:

```sh
git clone https://github.com/SkyUOI/OurChat --depth=1 && cd OurChat
```

- 安装 rust 工具链

- 编译项目

```sh
cd server && cargo build --release
```

- (可选)pgo 优化

该步骤会消耗大量时间，收集运行时信息来进行程序的优化，如果对于性能没有苛刻的要求不建议这么做

```sh
cargo install cargo-pgo
```

- 运行项目

这一步请参考[服务器参数](../run/server_argv.md)进行运行，可执行文件位于``target/server`

## Sqlite 便携部署

其余部分都可以参考上一章，但是 mysql 可以无需安装，具体配置方法参考[服务器参数](../run/server_argv.md)或直接参考`config/sqlite`文件夹中的`ourchat.toml`

注意，sqlite 运行仅限于性能需求不高，需要快速搭建的小型场景，如对性能有要求请使用 Mysql 方式。
