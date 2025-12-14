# 消息内的Markdown

为了确保用户消息的丰富性与传递的便携性，我们对Markdown基础语法进行了一些扩展

## 媒体

目前共有三种媒体

- 图片
- 视频
- 文件

消息内的媒体标签分为两种

- 网络媒体(__注意：考虑到安全性，OurChat官方客户端会对来自网络的内容进行明显的标记，我们强烈建议第三方客户端也实现该功能__)
- 服务器媒体

在消息中，一个媒体标签写作

```markdown
!(alt)[TS://content "title"]
```

其中字符T代表媒体类型

|字符|媒体类型|
|:--|:-------|
| I |  图片  |
| V |  视频  |
| F |  文件  |

字符S代表来源

|字符|     来源     |content对应内容|
|:--|:-------------|:--------------|
| O | OurChat服务器 |     媒体key    |
| N |      网络     |    媒体的url   |

因此，来自OurChat服务器的图片(key为xxx)写作：

```markdown
!(alt)[IO://xxx "title"]
```

来自网络的图片写作：

```markdown
!(alt)[IN://https://ourchat.skyuoi.org/resources/images/logo.png "title"]
```
