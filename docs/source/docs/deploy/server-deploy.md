# 服务端部署指南

- [Docker 部署](#docker推荐)
- [手动部署](#手动部署)

## Docker(推荐)

对于该项目，我们提供了两种在生产环境中使用的 docker 镜像，一种基于 debian，另一种基于 alpine, alpine 系列镜像适合硬盘空间比较宝贵的场景。

除去操作系统的区别外，还有几种不同的 tag 供选择：

- nightly: 在 main 分支上构建的最新版本，每天构建一次，可能不稳定，但具有最新的更改
- latest: 最新的稳定版本
- 其余各个版本的镜像，例如 v0.1.0.beta 之类，代表特定版本的镜像

以下是具体操作步骤：

- alpine

```bash
cd docker && docker compose up -d
```

- debian

```bash
cd docker && docker compose -f compose.debian.yml up -d
```

这一步完成只是创建了一个最基本的环境，但是安全性还远远没有达到，为了保证安全性，你需要修改 PostgreSQL 和 Redis 的密码。

具体有以下几步:

(如果你是用的 debian 系列镜像，下文的`compose.yml`全都指的是`compose.debian.yml`)

- 修改`compose.yml`中的`PORTGRES_PASSWORD`的`123456`为你自己的强密码
- 修改`docker/config/redis.conf`中的`123456`为你自己的强密码
- 修改`compose.yml`中的`RABBITMQ_DEFAULT_PASS`的`123456`为你自己的强密码
- 修改`docker/config/database.toml`中的密码为改后的 PostgreSQL 密码
- 修改`docker/config/redis.toml`中的密码为改后的 Redis 密码
- 修改`docker/config/rabbitmq.toml`中的密码为改后的 Rabbitmq 密码
- 再次运行你用于启动 docker 的环境的命令

完成这几步之后，你就成功部署了该项目。

对于容器中的数据，我们将其映射在了`data`中，你可以随时保存数据

## 手动部署

对于性能不高和未安装 docker 的计算机，我们也提供了手动部署的文档，关于这一点，建议部署在 linux 环境，其他环境未经过严格的测试。

### 安装 PostgreSQL

postgres 版本为 17（如果该文档未及时更新可以查看 [compose.yml](https://github.com/SkyUOI/OurChat/blob/main/docker/compose.yml)中的 postgres 版本）

### 安装 redis

Redis 版本为 7（如果该文档未及时更新可以查看 [compose.yml](https://github.com/SkyUOI/OurChat/blob/main/docker/compose.yml)中的 redis 版本）

### 安装 ourchat server

此处存在两种备选的方案:

1.(推荐)从 github release 下载最新的 linux 编译结果，如果遇到 CPU 架构和其他兼容性问题，可能需要手动编译，参见下一节

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

- 运行项目

这一步请参考[服务器参数](../run/server_argv.md)进行运行，可执行文件位于`target/release/server`

请注意服务器密码等依然需要修改!

- SSL/TLS 加密

见[SSL/TLS](../deploy/ssl-tls.md)
