# OurChat Api 文档

## 状态码

**_注：以下几种状态码在任何情况下都可能出现，请务必做好校验_**

| CodeId | CodeName    | meaning        |
| :----- | :---------- | :------------- |
| 0      | OK          | 执行成功       |
| 13     | INTERNAL    | 服务器内部错误 |
| 14     | UNAVAILABLE | 服务器维护中   |

**_以上特殊信息不再赘述_**

请参考 [grpc 文档](https://grpc.io/docs/guides/status-codes/)

## Api

**_消息体本身不在此赘述，请查看代码中的注释_**

### AuthService

该 Service 用于完成服务器中的鉴权操作

#### Register

用于注册一个用户并返回其 token

错误:

| CodeId | CodeName         | Detail                        | meaning              |
| :----- | :--------------- | :---------------------------- | :------------------- |
| 6      | ALREADY_EXISTS   | User Already Exists           | 该邮箱已被注册       |
| 3      | INVALID_ARGUMENT | Password Is Not Strong Enough | 密码不够强           |
| 3      | INVALID_ARGUMENT | Username Is Invalid           | 用户名非法，例如过长 |
| 3      | INVALID_ARGUMENT | Email Address Is Invalid      | 不是合法的邮箱地址   |

#### Auth

用于登录一个已经存在的用户并返回其 token

错误:

| CodeId | CodeName         | Detail           | meaning            |
| :----- | :--------------- | :--------------- | :----------------- |
| 5      | NOT_FOUND        | User Not Found   | 该用户不存在       |
| 3      | INVALID_ARGUMENT | Missing AuthType | 缺少 AuthType 参数 |
| 16     | UNAUTHENTICATED  | Wrong Password   | 密码错误           |
| 16     | UNAUTHENTICATED  | Account Locked   | 帐号已锁定         |

#### Verify

用于客户端发起邮箱验证，验证帐号是否被窃取

错误:

| CodeId | CodeName         | Detail           | meaning            |
| :----- | :--------------- | :--------------- | :----------------- |
| 5      | NOT_FOUND        | User Not Found   | 该用户不存在       |
| 3      | INVALID_ARGUMENT | Missing AuthType | 缺少 AuthType 参数 |
| 16     | UNAUTHENTICATED  | Wrong Password   | 密码错误           |

### BasicService

该 Service 用于完成服务器中不需要额外权限的操作

#### GetServerInfo

获取服务器的各项基本信息，包括版本号等

无错误

#### GetId

通过帐号 ocid 获取某个帐号的 id

错误:

| CodeId | CodeName  | Detail         | meaning      |
| :----- | :-------- | :------------- | :----------- |
| 5      | NOT_FOUND | User Not Found | 该用户不存在 |

#### GetPresetUserStatus

获取预设的帐号社交状态

错误:

| CodeId | CodeName | Detail       | meaning        |
| :----- | :------- | :----------- | :------------- |
| 13     | INTERNAL | Server Error | 服务器内部错误 |

### OurChatService

该 Service 用于完成绝大部分操作，且所有操作都需要额外附带通过[AuthService](#authservice)中调用获取的 token

提供该 token 的方式为添加请求头: `Authorization: Bearer <token>`

其遵循`RFC 6750`规范，`Bearer`为目前支持的唯一验证类型。

token 本身是以`JWT`的形式传递的，所以你可以解读 token，token 中数据格式为:

```json
{
  "id": 1, // account id(not ocid)
  "exp": 1600000000 // expiration time, this is unix timestamp
}
```

一旦 token 过期，服务器会返回`UNAUTHENTICATED`错误，错误信息为`Token Expired`

如果 token 不合法，例如不是 JWT 或不包含所需要的字段，服务器会返回`UNAUTHENTICATED`错误，错误信息为`Token Invalid`

如果未提供 token，服务器会返回`UNAUTHENTICATED`错误，错误信息为`Token Missing`

#### GetAccountInfo

| CodeId | CodeName          | Detail                | meaning                               |
| :----- | :---------------- | :-------------------- | :------------------------------------ |
| 7      | PERMISSION_DENIED | Permission Denied     | 权限不足(如:获取非当前帐号的隐私信息) |
| 5      | NOT_FOUND         | User Not Found        | 用户不存在                            |
| 3      | INVALID_ARGUMENT  | Request Invalid Value | 请求值无效(如:获取不存在的字段)       |

#### SetSelfInfo

| CodeId | CodeName         | Detail              | meaning                       |
| :----- | :--------------- | :------------------ | :---------------------------- |
| 6      | ALREADY_EXISTS   | Conflict            | 信息冲突(如:新的 ocid 被占用) |
| 3      | INVALID_ARGUMENT | Ocid Too Long       | 新的 ocid 太长                |
| 3      | INVALID_ARGUMENT | Status Too Long     | 新的 Status 太长              |
| 3      | INVALID_ARGUMENT | Username Is Invalid | 用户名非法，例如过长或为空    |

#### FetchMsgs

| CodeId | CodeName         | Detail            | meaning        |
| :----- | :--------------- | :---------------- | :------------- |
| 3      | INVALID_ARGUMENT | Time Format Error | 无法解析时间戳 |
| 3      | INVALID_ARGUMENT | Time Missing      | 缺少 time 参数 |

#### SendMsg

| CodeId | CodeName          | Detail            | meaning      |
| :----- | :---------------- | :---------------- | :----------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有发言权限 |
| 5      | NOT_FOUND         | Session Not Found | 会话不存在   |

#### Upload

| CodeId | CodeName           | Detail                       | meaning                            |
| :----- | :----------------- | :--------------------------- | :--------------------------------- |
| 3      | INVALID_ARGUMENT   | File Size Error              | 文件大小与 metadata 不符合         |
| 3      | INVALID_ARGUMENT   | File Hash Error              | 文件 hash 与 metadata 不符合       |
| 8      | RESOURCE_EXHAUSTED | Storage Full                 | 该用户储存空间已满                 |
| 3      | INVALID_ARGUMENT   | Metadata Error               | 缺少 metadata 参数或 metadata 无效 |
| 3      | INVALID_ARGUMENT   | Incorrect Order Of Uploading | 应先上传 metadata 再上传数据包     |

#### Download

| CodeId | CodeName          | Detail            | meaning      |
| :----- | :---------------- | :---------------- | :----------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有下载权限 |

#### NewSession

| CodeId | CodeName  | Detail         | meaning          |
| :----- | :-------- | :------------- | :--------------- |
| 5      | NOT_FOUND | User Not Found | 邀请的用户不存在 |

#### GetSessionInfo

| CodeId | CodeName         | Detail                | meaning                         |
| :----- | :--------------- | :-------------------- | :------------------------------ |
| 5      | NOT_FOUND        | Session Not Found     | 该会话不存在                    |
| 3      | INVALID_ARGUMENT | Request Invalid Value | 请求值无效(如:获取不存在的字段) |

#### SetSessionInfo

| CodeId | CodeName          | Detail                 | meaning                |
| :----- | :---------------- | :--------------------- | :--------------------- |
| 6      | ALREADY_EXISTS    | Conflict               | 信息冲突               |
| 7      | PERMISSION_DENIED | Cannot Set Name        | 没有设置会话名称的权限 |
| 7      | PERMISSION_DENIED | Cannot Set Avatar      | 没有设置会话头像的权限 |
| 7      | PERMISSION_DENIED | Cannot Set Description | 没有设置会话简介的权限 |

#### RecallMsg

| CodeId | CodeName          | Detail            | meaning            |
| :----- | :---------------- | :---------------- | :----------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有撤回消息的权限 |
| 5      | NOT_FOUND         | Message Not Found | 撤回的消息不存在   |

#### SetRole

| CodeId | CodeName          | Detail              | meaning            |
| :----- | :---------------- | :------------------ | :----------------- |
| 7      | PERMISSION_DENIED | Permission Denied   | 没有设置身份的权限 |
| 5      | NOT_FOUND         | User Not In Session | 用户不存在         |

#### AddRole

#### DeleteSession

| CodeId | CodeName          | Detail            | meaning            |
| :----- | :---------------- | :---------------- | :----------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有删除会话的权限 |
| 5      | NOT_FOUND         | Session Not Found | 该会话不存在       |

#### LeaveSession

| CodeId | CodeName  | Detail              | meaning        |
| :----- | :-------- | :------------------ | :------------- |
| 5      | NOT_FOUND | User Not In Session | 用户不在该会话 |

#### JoinInSession

| CodeId | CodeName          | Detail            | meaning                     |
| :----- | :---------------- | :---------------- | :-------------------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 无法加入会话，例如被 ban 了 |
| 5      | NOT_FOUND         | Session Not Found | 该 session 不存在           |

#### AcceptJoinInSession

| CodeId | CodeName          | Detail            | meaning                              |
| :----- | :---------------- | :---------------- | :----------------------------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 无法同意加入会话请求，例如缺少该权限 |
| 5      | NOT_FOUND         | Session Not Found | 该 session 不存在                    |

#### MuteUser

| CodeId | CodeName          | Detail            | meaning              |
| :----- | :---------------- | :---------------- | :------------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 不具有 MuteUser 权限 |

#### UnmuteUser

| CodeId | CodeName          | Detail            | meaning                |
| :----- | :---------------- | :---------------- | :--------------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 不具有 UnmuteUser 权限 |
| 5      | NOT_FOUND         | User Not Be Muted | 用户没有被 Mute        |

#### BanUser

| CodeId | CodeName          | Detail            | meaning             |
| :----- | :---------------- | :---------------- | :------------------ |
| 7      | PERMISSION_DENIED | Permission Denied | 不具有 BanUser 权限 |

#### UnbanUser

| CodeId | CodeName          | Detail             | meaning               |
| :----- | :---------------- | :----------------- | :-------------------- |
| 7      | PERMISSION_DENIED | Permission Denied  | 不具有 UnbanUser 权限 |
| 5      | NOT_FOUND         | User Not Be Banned | 用户没有被 Ban        |

#### AddFriend

| CodeId | CodeName          | Detail                | meaning        |
| :----- | :---------------- | :-------------------- | :------------- |
| 7      | PERMISSION_DENIED | Permission Denied     | 不具有权限     |
| 6      | ALREADY_EXISTS    | Friend Already Exists | 好友关系已存在 |
| 5      | NOT_FOUND         | User Not Found        | 好友不存在     |

#### AcceptFriend

| CodeId | CodeName          | Detail                      | meaning        |
| :----- | :---------------- | :-------------------------- | :------------- |
| 7      | PERMISSION_DENIED | Permission Denied           | 不具有权限     |
| 5      | NOT_FOUND         | Friend Invitation Not Found | 好友申请不存在 |

#### DeleteFriend

| CodeId | CodeName  | Detail           | meaning        |
| :----- | :-------- | :--------------- | :------------- |
| 5      | NOT_FOUND | Friend Not Found | 好友关系不存在 |

#### GetRole

| CodeId | CodeName          | Detail         | meaning                   |
| :----- | :---------------- | :------------- | :------------------------ |
| 7      | PERMISSION_DENIED | Not In Session | 不在Session中，不具备权限 |
| 5      | NOT_FOUND         | Role Not Found | 角色不存在                |

#### Unregister

暂时没有相关错误可能发生
