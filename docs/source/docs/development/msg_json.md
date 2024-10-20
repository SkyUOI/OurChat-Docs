﻿# OurChat 信息传递格式

## 账号

### 注册信息

**_Server <- Client_**

```json
// E.g.
{
  "code": 4,
  "email": "123456@ourchat.com", // 注册使用的邮箱
  "password": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", // 注册密码(已加密)
  "name": "Outchat" // 昵称
}
```

| key      | ValueType | comment          |
| :------- | :-------- | :--------------- |
| email    | String    | 注册邮箱         |
| password | String    | 注册密码(已加密) |
| name     | String    | 昵称             |

### 注册返回信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 5,
  "ocid": "0000000000", // 注册账号的ocid
  "status": 0 // 状态码，返回运行状态
}
```

| key    | ValueType | comment                                                                       |
| :----- | :-------- | :---------------------------------------------------------------------------- |
| ocid   | String    | 该账号的 ocid                                                                 |
| status | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#注册返回信息) |

### 登录信息

**_Server <- Client_**

```json
// E.g.
{
  "code": 6,
  "login_type": 1, // 登录方式,此处1表示使用ocid登录
  "account": "0000000000", // 邮箱/ocid
  "password": "密码"
}
```

| key        | ValueType | comment                      |
| :--------- | :-------- | :--------------------------- |
| login_type | Number    | 0 为邮箱登录，1 为 ocid 登录 |
| account    | String    | 账号绑定的邮箱或 ocid        |
| password   | String    | 密码                         |

### 登录返回信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 7,
  "ocid": "0000000000", // 该账号的ocid
  "status": 0 // 状态码，返回运行状态
}
```

| key    | ValueType | comment                                                                       |
| :----- | :-------- | :---------------------------------------------------------------------------- |
| ocid   | String    | 该账号的 ocid                                                                 |
| status | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#登录返回信息) |

### 获取账号信息

**_Server <- Client_**

```json
// E.g.
{
  "code": 10,
  "ocid": "0000000000", //该账号的ocid
  "request_values": [
    "ocid",
    "display_name"
    // ...
  ]
}
```

| key            | ValueType | comment              |
| :------------- | :-------- | :------------------- |
| ocid           | String    | 该账号的 ocid        |
| request_values | Array     | 需要服务端返回的信息 |

| request_value      | ValueType | comment                                                           |
| :----------------- | :-------- | :---------------------------------------------------------------- |
| ocid               | String    | 该账号的 ocid                                                     |
| email              | String    | 该账号绑定的邮箱(仅本账号可获取，非本账号返回 null)               |
| user_name          | String    | 用户名                                                            |
| display_name       | String    | 备注名                                                            |
| status             | Number    | 该账号的状态                                                      |
| avatar_key         | String    | 获取头像时需要用到的密钥                                          |
| time               | String    | 该账号注册的时间戳                                                |
| public_update_time | String    | 该账号公共(即不包括**sessions**和**friends**)数据最后更新的时间戳 |
| update_time        | String    | 该账号所有数据最后更新的时间戳(仅本账号可获取，非本账号返回 null) |
| sessions           | Array     | 该账号加入/创建的会话列表(仅本账号可获取，非本账号返回 null)      |
| friends            | Array     | 该账号的好友列表 (仅本账号可获取，非本账号返回 null)              |

### 获取账号信息返回信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 11,
  "data": {
    "ocid": "0000000000", // 该账号的 ocid
    "user_name": "OurChat" // 该账号的昵称
    // ...
  },
  "status": 0 // 状态码，返回运行状态
}
```

| key    | ValueType | comment                                                                               |
| :----- | :-------- | :------------------------------------------------------------------------------------ |
| data   | Object    | 账号信息,详情[见上**获取账号信息**`request_value`](#获取账号信息)                     |
| status | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#获取账号信息返回信息) |

### 注销

**_Server <- Client_**

```json
// E.g.
{
  "code": 16
}
```

**_警告：该注销是删除帐号的意思，请勿误用接口_**

### 注销返回信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 17,
  "status": 0 // 状态码，返回运行状态
}
```

| key    | ValueType | comment                                                                       |
| :----- | :-------- | :---------------------------------------------------------------------------- |
| status | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#注销返回信息) |

### 设置账号信息

**_Server <- Client_**

```json
// E.g.
{
  "code": 19,
  "data": {
    "user_name": "OurChat1" // 更改后的账号昵称
    // ...
  }
}
```

| key  | ValueType | comment                                    |
| :--- | :-------- | :----------------------------------------- |
| data | Object    | 需要更改的账号信息，可设置的字段见下面表格 |

可设置的字段：

| key        | ValueType |
| :--------- | :-------- |
| user_name  | String    |
| avatar_key | String    |
| status     | Number    |

以上字段具体意义见[**获取账号信息**`request_value`](#获取账号信息)

### 设置好友信息

**_Server <- Client_**

```json
// E.g.
{
  "code": 27,
  "ocid": "0000000000",
  "data": {
    "display_name": "OurChat1" // 更改后的好友昵称
    // ...
  }
}
```

| key  | ValueType | comment                                    |
| :--- | :-------- | :----------------------------------------- |
| ocid | String    | 需要更改的好友的 ocid                      |
| data | Object    | 需要更改的好友信息，可设置的字段见下面表格 |

可设置的字段：

| key          | ValueType |
| :----------- | :-------- |
| display_name | String    |

### 设置账号信息返回信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 20,
  "status": 0 // 状态码，返回运行状态
}
```

| key    | ValueType | comment                                                                               |
| :----- | :-------- | :------------------------------------------------------------------------------------ |
| status | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#设置账号信息返回信息) |

## 会话

### 获取会话信息

**_Server <- Client_**

```json
// E.g.
{
  "code": 1,
  "session_id": 1145141919, // 该会话的ID,
  "request_values": [
    "name"
    // ...
  ]
}
```

| key            | ValueType | comment              |
| :------------- | :-------- | :------------------- |
| session_id     | Number    | 该会话的 ID          |
| request_values | Array     | 需要服务端返回的信息 |

| request_value | valueType | comment                    |
| :------------ | :-------- | :------------------------- |
| session_id    | Number    | 该会话的 ID                |
| name          | String    | 会话名称                   |
| avatar_key    | String    | 获取头像时需要用到的密钥   |
| time          | String    | 该会话创建的时间戳         |
| update_time   | String    | 该会话数据最后更新的时间戳 |
| members       | Array     | 该会话的成员列表           |
| owner         | Array     | 该会话拥有者的 ocid        |

### 获取会话信息返回信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 2,
  "data": {
    "session_id": 1145141919, // 该会话的ID
    "name": "Session1" // 会话名称
    // ...
  },
  "status": 0 // 状态码，返回运行状态
}
```

| key    | ValueType | comment                                                                               |
| :----- | :-------- | :------------------------------------------------------------------------------------ |
| data   | Object    | 账号信息,详情[见上**获取会话信息**`request_value`](#获取会话信息)                     |
| status | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#获取会话信息返回信息) |

### 新建会话请求信息

**_Server <- Client_**

```json
// E.g.1
{
  "code": 8,
  "members": [
    "0000000000",
    "0000000001"
    // ...
  ]
}
```

```json
// E.g.2
{
  "code": 8,
  "avatar_key": "key", // 获取头像时需要用到的密钥
  "name": "OurChat Session", // 会话名称,可选
  "members": [
    "0000000000",
    "0000000001"
    // ...
  ]
}
```

| key        | ValueType | comment                             |
| :--------- | :-------- | :---------------------------------- |
| avatar_key | String    | 获取头像时需要用到的密钥            |
| name       | String    | 会话名称,可选(如不填写使用默认名称) |
| members    | Array     | 会话成员                            |

### 新建会话返回信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 9,
  "session_id": 1145141919, // 仅当创建成功时有此字段
  "status": 0 // 状态码，返回运行状态
}
```

| key        | ValueType | comment                                                                           |
| :--------- | :-------- | :-------------------------------------------------------------------------------- |
| session_id | Number    | 会话 id                                                                           |
| status     | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#新建会话返回信息) |

## 邀请加入会话

**_Server -> Client_**

```json
{
  "code": 24,
  "session_id": 1145141919,
  "inviter_id": "0000000000",
  "message": "邀请加入会话",
  "expire_timestamp": "2024-10-19T11:29:06.392122930+00:00"
}
```

| key              | valueType | comment    |
| :--------------- | :-------- | :--------- |
| session_id       | Number    | 会话 id    |
| inviter_id       | String    | 邀请者 id  |
| message          | String    | 留言       |
| expire_timestamp | String    | 失效时间戳 |

## 邀请加入会话返回信息

**_Server <- Client_**

```json
// E.g.
{
  "code": 25,
  "session_id": 1145141919,
  "accept": true
}
```

| key        | ValueType | comment          |
| :--------- | :-------- | :--------------- |
| session_id | Number    | 会话 id          |
| accept     | Boolean   | 对邀请的同意情况 |

## 同意加入会话返回信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 26,
  "status": 0
}
```

| key    | ValueType | comment                                                                               |
| :----- | :-------- | :------------------------------------------------------------------------------------ |
| status | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#同意加入会话返回信息) |

## 服务器

### 获取服务器状态

**_Server <-> Client_**

```json
// E.g.
{
  "code": 12,
  "status": 0 // 状态码，返回运行状态
}
```

| key    | ValueType | comment                                                                         |
| :----- | :-------- | :------------------------------------------------------------------------------ |
| status | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#获取服务器状态) |

## 验证码

### 发起验证

**_Server -> Client_**

```json
// E.g.
{
  "code": 13
}
```

### 生成验证码

#### 请求生成

**_Server <- Client_**

```json
// E.g.
{
  "code": 14,
  "email": "123456@ourchat.com" // 验证邮箱
}
```

| key   | ValueType | comment  |
| :---- | :-------- | :------- |
| email | String    | 验证邮箱 |

#### 返回消息

```json
// E.g.
{
  "code": 23,
  "status": 0
}
```

| key    | ValueType | comment                                                                   |
| :----- | :-------- | :------------------------------------------------------------------------ |
| status | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#邮件发送) |

### 验证状态

**_Server -> Client_**

```json
// E.g.
{
  "code": 15,
  "status": 0 // 状态码，返回运行状态
}
```

| key    | ValueType | comment                                                                   |
| :----- | :-------- | :------------------------------------------------------------------------ |
| status | Number    | 状态码，返回运行状态，详情见[**状态码**`status`](status_code.md#验证状态) |

## 其他信息

### 获取信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 0,
  "session_id": 1145141919, //发送此消息的会话id
  "msgs": [
    {
      "time": "2024-10-19T11:29:06.392122930+00:00", // 发送消息的时间戳
      "sender_id": "0000000000",
      "msg_id": "1643212388",
      "bundle_msg": [
        {
          "type": 0 // 用户消息类型
          // ...相关数据
        }
      ]
    }
    // ...
  ]
}
```

| key        | ValueType | comment               |
| :--------- | :-------- | :-------------------- |
| msgs       | Array     | 发送的消息列表        |
| session_id | Number    | 消息全部属于该会话 id |
| msgs       | Array     | 消息列表              |

### 用户发送信息

**_Server <- Client_**

```json
{
  "code": 29,
  "session_id": 1145141919,
  "time": "2024-10-19T11:29:06.392122930+00:00",
  "bundle_msg": [
    {
      "type": 0
      // ...
    }
    // ...
  ]
}
```

### 发送信息返回信息

**_Server -> Client_**

```json
{
  "code": 30,
  "status": 0,
  "msg_id": "1643212388"
}
```

### 请求获取消息

**_Server <- Client_**

```json
// E.g.
{
  "code": 28,
  "time": "2024-10-19T11:29:06.392122930+00:00"
}
```

返回[用户发送消息](#获取信息)

**_Warning:该接口调用后，考虑到消息可能有很多，可能不会一次性返回所有信息，注意分批接收！_**

| key  | ValueType | comment                    |
| :--- | :-------- | :------------------------- |
| time | String    | 接收来自该时间戳之后的消息 |

| key        | ValueType | comment                                                      |
| :--------- | :-------- | :----------------------------------------------------------- |
| time       | String    | 发消息的时间戳                                               |
| msg_id     | Number    | message 的 ID，唯一 **(注意：传输给服务器时无此字段)**       |
| sender     | Object    | 发送者的相关数据                                             |
| ocid       | String    | 发送者的 ocid                                                |
| session_id | Number    | 发送者的会话 id                                              |
| msg        | Array     | 消息列表                                                     |
| type       | Number    | 用户消息类型，详细见[**用户消息传递格式**](user_msg_json.md) |

### 错误信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 18,
  "details": "错误信息"
}
```

| Key     | ValueType | Comment  |
| :------ | :-------- | :------- |
| details | String    | 异常信息 |

### 文件上传请求

**_Server <- Client_**

```json
// E.g.
{
  "code": 21,
  "hash": "asdcdfdvdfdvfddf",
  "auto_clean": true,
  "size": 10000
}
```

| key                  | ValueType | Comment                         |
| :------------------- | :-------- | :------------------------------ |
| hash                 | String    | 文件`sha256`哈希                |
| auto_clean(optional) | Boolean   | 该文件是否自动清理,默认为 false |
| size                 | Number    | 上传文件的字节数                |

**注意，此处仅为上传文件的一部分，参见[http 部分的上传格式](./http_api.md#文件上传)**

### 文件上传返回信息

**_Server -> Client_**

```json
// E.g.
{
  "code": 22,
  "status": 0,
  "key": "sdjoqjdoqjodo",
  "hash": "dsodjsodjosjdoshdowho"
}
```

| key    | ValueType | Comment                                                                           |
| :----- | :-------- | :-------------------------------------------------------------------------------- |
| key    | String    | 资源密钥，用于请求头`Key:`中，验证发送者身份并且是资源访问唯一标识符              |
| hash   | String    | 文件的`sha256`哈希                                                                |
| status | Number    | 状态码，非零时其余字段不存在，参考[**状态码**](./status_code.md#上传文件返回信息) |
