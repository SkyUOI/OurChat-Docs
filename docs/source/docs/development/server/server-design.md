# 服务端架构

服务端并不是单个程序，而是由多个程序共同构成的分布式服务，涉及到的服务如下：

- 主服务: OurChatServer

这是单个节点，可以处理几乎所有的基本请求，在舍弃其它组件的情况下也可以正常运行，是组成分布式系统的主要核心服务，同时也可以单独部署

- HttpServer: HTTP 服务

负责处理 HTTP 请求,如邮件验证等

- 负载均衡器：LoadBalancer

负责将请求和流量均摊到节点上

- Consul: 服务发现和注册中心

负责注册各个节点，并提供服务发现的能力

- Redis: 内存数据库

用于高性能的缓存

- PostgreSQL: 数据库

用于持久化数据

- JuiceFS: 分布式文件系统

具体参考其官网 [JuiceFS](https://juicefs.com)

组件之间可以通过 RPC 的方式进行通信，通过非对称加密签名来签名 JWT 进行身份验证