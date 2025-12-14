# 消息内的Markdown

为了确保用户消息的丰富性与传递的便携性，我们对Markdown基础语法进行了一些扩展

## 图片

消息内的Image标签分为两种

- 网络图片
- 服务器图片

### 网络图片

网络图片与Markdown语法一致，即 `![alt](url "title")`
由于网络图片的安全性问题，在OurChat官方客户端内，网络图片旁将存在安全性提示，我们强烈建议第三方客户端也提供该功能

### 服务器图片

服务器图片是指经过upload api上传到服务器的图片
在消息内写作`![alt](ourchat://key "title")`
key即为调用upload api所返回的key
