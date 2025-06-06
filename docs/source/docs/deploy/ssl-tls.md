# 为服务器设置 SSL/TLS 证书

在一个规模不大或是内网中的服务器，通常不需要设置 SSL/TLS 证书。然而，如果你正在设置一个公共的服务器，设置一个 SSL/TLS 证书是很有必要的，这可以有效防止一些恶意的攻击。

首先，你需要一个可用的证书，你可以选择[Let's Encrypt](https://letsencrypt.org/)的免费证书，也可以选择其他的商业证书。

接下来，为服务器配置 SSL/TLS 加密有两种方法：

## 与现有的代理服务结合(Recommended)

下面以[nginx](https://www.nginx.com/)+[Let's Encrypt](https://letsencrypt.org/)为例，配置 nginx 的 SSL/TLS 加密:

- 使用[certbot](https://certbot.eff.org/)安装证书

- 修改 docker 服务映射到的端口（optional）

修改`docker/compose.yml`的`port`，例如将`7777:7777`修改为`17777:7777`，将端口映射到本地的`17777`端口

您可能需要在`/etc/docker/daemon.json`加入`{"iptables":false}`来禁用`iptables`，同时可能需要`ufw`之类的软件来帮助禁用`17777`端口暴露到公网。

- 在`nginx.conf`中加入类似以下配置:

```nginx
server {
    server_name  xxx.com;

    location / {
        grpc_pass grpc://127.0.0.1:17777;
    }

    http2 on;

    listen 7777 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/xxx.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/xxx.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}

server {
    server_name  xxx.com;

    location / {
        proxy_pass http://127.0.0.1:17778;
    }

    listen 7778 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/xxx.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/xxx.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}
```

从而将外部的流量转发到内部的端口，配合上 certbot 自动管理的 ssl 证书，就可以完成 SSL/TLS 加密的设置了。这种方式不需要特别修改 server，换句话说，`tls.enable`不需要设置为`true`

## 独立启用 SSL/TLS 加密

Ourchat Server 本身也可以配置证书加密，而不需要依赖 nginx，操作步骤如下：

- 使用[certbot](https://certbot.eff.org/)获取证书

- 根据证书设置`ourchat.toml`

将`tls.enable`设置为`true`，

并按照以下表格设置：

| 字段                       | 用途                                 |
| -------------------------- | ------------------------------------ |
| `tls.server_tls_cert_path` | 服务端证书的`.pem`文件路径。         |
| `tls.server_key_cert_path` | 服务端证书的`.key`文件路径。         |
| `client_tls_cert_path`     | 客户端证书的`.pem`文件路径。         |
| `client_key_cert_path`     | 客户端证书的`.key`文件路径。         |
| `ca_tls_cert_path`         | 服务端证书的根证书的`.pem`文件路径。 |
| `client_ca_tls_cert_path`  | 客户端证书的根证书的`.pem`文件路径。 |

参数在`server`和`http_server`中同时存在，可以根据需要来启用 TLS。

同时，客户端证书用于双向验证，不作为强制要求，仅在特殊情况下设置。
