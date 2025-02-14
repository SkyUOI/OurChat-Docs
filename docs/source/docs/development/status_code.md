# OurChat 状态码

**_注：以下几种状态码在任何情况下都可能出现，请务必做好校验_**

| CodeId | CodeName    | meaning        |
| :----- | :---------- | :------------- |
| 0      | OK          | 执行成功       |
| 13     | INTERNAL    | 服务器内部错误 |
| 14     | UNAVAILABLE | 服务器维护中   |

**_以上特殊信息不再赘述_**

## 状态码

请参考 [grpc 文档](https://grpc.io/docs/guides/status-codes/)

## 各种信息下的状态码具体解释

### AuthService/Register

| CodeId | CodeName       | Detail              | meaning        |
| :----- | :------------- | :------------------ | :------------- |
| 6      | ALREADY_EXISTS | User Already Exists | 该邮箱已被注册 |

### AuthService/Auth

| CodeId | CodeName         | Detail           | meaning            |
| :----- | :--------------- | :--------------- | :----------------- |
| 5      | NOT_FOUND        | User Not Found   | 该用户不存在       |
| 3      | INVALID_ARGUMENT | Missing AuthType | 缺少 AuthType 参数 |
| 16     | Unauthenticated  | Wrong Password   | 密码错误           |

### AuthService/Verify

| CodeId | CodeName         | Detail           | meaning            |
| :----- | :--------------- | :--------------- | :----------------- |
| 5      | NOT_FOUND        | User Not Found   | 该用户不存在       |
| 3      | INVALID_ARGUMENT | Missing AuthType | 缺少 AuthType 参数 |
| 16     | Unauthenticated  | Wrong Password   | 密码错误           |

### BasicService/GetServerInfo

| CodeId | CodeName    |    meaning     |
| :----- | :---------- | :------------: |
| 0      | OK          |    执行成功    |
| 13     | INTERNAL    | 服务器内部错误 |
| 14     | UNAVAILABLE |  服务器维护中  |

### BasicServer/GetId

| CodeId | CodeName  | Detail         | meaning      |
| :----- | :-------- | :------------- | :----------- |
| 5      | NOT_FOUND | User Not Found | 该用户不存在 |

### OurChatService/GetAccountInfo

| CodeId | CodeName          | Detail                | meaning                               |
| :----- | :---------------- | :-------------------- | :------------------------------------ |
| 7      | PERMISSION_DENIED | Permission Denied     | 权限不足(如:获取非当前帐号的隐私信息) |
| 5      | NOT_FOUND         | User Not Found        | 用户不存在                            |
| 3      | INVALID_ARGUMENT  | Request Invalid Value | 请求值无效(如:获取不存在的字段)       |

### OurChatService/SetSelfInfo

| CodeId | CodeName              | Detail   | meaning                       |
| :----- | :-------------------- | :------- | :---------------------------- |
| 6      | ALREADY_EXISTS        | Conflict | 信息冲突(如:新的 ocid 被占用) |
| 3      | INVALID_ARGUMENT Ocid | Too Long | 新的 ocid 太长                |

### OurChatService/FetchMsgs

| CodeId | CodeName         | Detail            | meaning        |
| :----- | :--------------- | :---------------- | :------------- |
| 3      | INVALID_ARGUMENT | Time Format Error | 无法解析时间戳 |
| 3      | INVALID_ARGUMENT | Time Missing      | 缺少 time 参数 |

### OurChatService/SendMsg

| CodeId | CodeName          | Detail            | meaning      |
| :----- | :---------------- | :---------------- | :----------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有发言权限 |
| 5      | NOT_FOUND         | Session Not Found | 会话不存在   |

### OurChatService/Upload

| CodeId | CodeName           | Detail                       | meaning                            |
| :----- | :----------------- | :--------------------------- | :--------------------------------- |
| 3      | INVALID_ARGUMENT   | File Size Error              | 文件大小与 metadata 不符合         |
| 3      | INVALID_ARGUMENT   | File Hash Error              | 文件 hash 与 metadata 不符合       |
| 8      | RESOURCE_EXHAUSTED | Storage Full                 | 该用户储存空间已满                 |
| 3      | INVALID_ARGUMENT   | Metadata Error               | 缺少 metadata 参数或 metadata 无效 |
| 3      | INVALID_ARGUMENT   | Incorrect Order Of Uploading | 应先上传 metadata 再上传数据包     |

### OurChatService/Download

| CodeId | CodeName          | Detail            | meaning      |
| :----- | :---------------- | :---------------- | :----------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有下载权限 |

### OurChatService/NewSession

| CodeId | CodeName  | Detail         | meaning          |
| :----- | :-------- | :------------- | :--------------- |
| 5      | NOT_FOUND | User Not Found | 邀请的用户不存在 |

### OurChatService/GetSessionInfo

| CodeId | CodeName         | Detail                | meaning                         |
| :----- | :--------------- | :-------------------- | :------------------------------ |
| 5      | NOT_FOUND        | Session Not Found     | 该会话不存在                    |
| 3      | INVALID_ARGUMENT | Request Invalid Value | 请求值无效(如:获取不存在的字段) |

### OurChatService/SetSessionInfo

| CodeId | CodeName          | Detail                 | meaning                |
| :----- | :---------------- | :--------------------- | :--------------------- |
| 6      | ALREADY_EXISTS    | Conflict               | 信息冲突               |
| 7      | PERMISSION_DENIED | Cannot Set Name        | 没有设置会话名称的权限 |
| 7      | PERMISSION_DENIED | Cannot Set Avatar      | 没有设置会话头像的权限 |
| 7      | PERMISSION_DENIED | Cannot Set Description | 没有设置会话简介的权限 |

### OurChatService/RecallMsg

| CodeId | CodeName          | Detail            | meaning            |
| :----- | :---------------- | :---------------- | :----------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有撤回消息的权限 |
| 5      | NOT_FOUND         | Message Not Found | 撤回的消息不存在   |

### OurChatService/SetRole

| CodeId | CodeName          | Detail              | meaning            |
| :----- | :---------------- | :------------------ | :----------------- |
| 7      | PERMISSION_DENIED | Permission Denied   | 没有设置身份的权限 |
| 5      | NOT_FOUND         | User Not In Session | 用户不存在         |

### OurChatService/AddRole

### OurChatService/DeleteSession

| CodeId | CodeName          | Detail            | meaning            |
| :----- | :---------------- | :---------------- | :----------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有删除会话的权限 |
| 5      | NOT_FOUND         | Session Not Found | 该会话不存在       |

### OurChatService/LeaveSession

| CodeId | CodeName  | Detail              | meaning        |
| :----- | :-------- | :------------------ | :------------- |
| 5      | NOT_FOUND | User Not In Session | 用户不在该会话 |

### OurChatService/JoinInSession

| CodeId | CodeName          | Detail            | meaning                     |
| :----- | :---------------- | :---------------- | :-------------------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 无法加入会话，例如被 ban 了 |
| 5      | NOT_FOUND         | Session Not Found | 该 session 不存在           |

### OurChatService/AcceptJoinInSession

| CodeId | CodeName          | Detail            | meaning                              |
| :----- | :---------------- | :---------------- | :----------------------------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 无法同意加入会话请求，例如缺少该权限 |
| 5      | NOT_FOUND         | Session Not Found | 该 session 不存在                    |

### OurChatService/MuteUser

| CodeId | CodeName          | Detail            | meaning              |
| :----- | :---------------- | :---------------- | :------------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 不具有 MuteUser 权限 |

### OurChatService/UnmuteUser

| CodeId | CodeName          | Detail            | meaning                |
| :----- | :---------------- | :---------------- | :--------------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 不具有 UnmuteUser 权限 |
| 5      | NOT_FOUND         | User Not Be Muted | 用户没有被 Mute        |

### OurChatService/BanUser

| CodeId | CodeName          | Detail            | meaning             |
| :----- | :---------------- | :---------------- | :------------------ |
| 7      | PERMISSION_DENIED | Permission Denied | 不具有 BanUser 权限 |

### OurChatService/UnbanUser

| CodeId | CodeName          | Detail             | meaning               |
| :----- | :---------------- | :----------------- | :-------------------- |
| 7      | PERMISSION_DENIED | Permission Denied  | 不具有 UnbanUser 权限 |
| 5      | NOT_FOUND         | User Not Be Banned | 用户没有被 Ban        |

### OurChatService/AddFriend

### OurChatService/AcceptFriend

### OurChatService/DeleteFriend
