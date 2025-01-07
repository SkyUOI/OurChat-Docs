# 服务端开发指南

- [项目构建依赖](#项目构建依赖)
- [容器开发](#容器开发)
- [数据库](#数据库)
- [服务器配置文件](#服务器配置文件)

## 项目构建依赖

Server 部分由 Rust 语言编写.你首先应当安装 Rust.
开发在本地或是在 docker 中都是可行的。
部署在 Docker 中完成，所以你也应当安装 Docker.
docker-buildx 和 docker-compose 同样也需要安装.

## 服务器配置文件

于`config`目录下存放了所有配置文件的示例，在开发阶段请最好不要更改这些配置文件。

## 容器开发

我们提供了一个用于开发环境的 docker-compose 文件模板，你可以根据需要修改

你可以运行:

```bash
docker compose -f compose.dev.yml up -d
```

来配置开发环境

如果 Dockerfile.dev 改变了，你可以运行`script/rebuild_dev_container.py`来重新构建镜像。

我们将数据直接复制到了`/app`文件夹，因此你**_不能随意重置容器_**，但这样可以使您的数据之间不会相互干扰。

推荐的开发方式是在本地使用编辑器编辑，同时使用`docker exec -it OurChatServer bash`进入容器运行并观察结果

首先，切换进`server`目录中，开发都将在这里进行。

启动时使用

```bash
cargo run -- --config=cfg.toml
```

启动测试:

参见[测试](./basic.md#运行集成测试)

## 数据库

本项目采用 Redis, PostgreSQL 作为数据库，同时采用 sea-orm 作为 ORM 框架。为了更好地使用该 ORM 框架，在修改数据库表后，您可以运行`script/regenerate_entity.py`来重新生成 ORM 框架需要的文件

为了运行这个脚本，你首先需要运行`cargo install sea-orm-cli`

注意：请保证`sea-orm-cli`是最新的，否则会被脚本拦截，若脚本的版本更旧，请随时打开一个 issue

### 数据库迁移

`migration`中是数据库迁移模块，在 server 启动时会自动运行未运行的数据库迁移，为了定义一个新的数据库迁移，请参考[sea orm](https://www.sea-ql.org/SeaORM/docs/migration/setting-up-migration/)
