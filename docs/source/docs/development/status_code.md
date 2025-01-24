# OurChat 状态码

**_注：以下几种状态码在任何情况下都可能出现，请务必做好校验_**

| CodeId | CodeName            | meaning        |
| :----- | :------------------ | :------------- |
| 0      | OK                  | 执行成功       |
| 13     | INTERNAL            | 服务器内部错误 |
| 9      | FAILED_PRECONDITION | 服务器维护中   |

**_以上特殊信息不再赘述_**

## 状态码

请参考 [grpc 文档](https://grpc.io/docs/guides/status-codes/)

## 各种信息下的状态码具体解释

### 注册

| CodeId | CodeName       | Detail              | meaning        |
| :----- | :------------- | :------------------ | :------------- |
| 6      | ALREADY_EXISTS | User Already Exists | 该邮箱已被注册 |

### 登录

| CodeId | CodeName         | Detail           | meaning          |
| :----- | :--------------- | :--------------- | :--------------- |
| 5      | NOT_FOUND        | User Not Found   | 该用户不存在     |
| 3      | INVALID_ARGUMENT | Missing AuthType | 缺少AuthType参数 |
| 16     | Unauthenticated  | Wrong Password   | 密码错误         |

### 验证

该功能暂未实现

### 获取服务器信息

| CodeId | CodeName            | meaning        |
| :----- | :------------------ | :------------- |
| 0      | OK                  | 执行成功       |
| 13     | INTERNAL            | 服务器内部错误 |
| 9      | FAILED_PRECONDITION | 服务器维护中   |

### 获取账号id

| CodeId | CodeName  | Detail         | meaning      |
| :----- | :-------- | :------------- | :----------- |
| 5      | NOT_FOUND | User Not Found | 该用户不存在 |

### 获取账号信息

| CodeId | CodeName          | Detail                | meaning                               |
| :----- | :---------------- | :-------------------- | :------------------------------------ |
| 7      | PERMISSION_DENIED | Permission Denied     | 权限不足(如:获取非当前帐号的隐私信息) |
| 5      | NOT_FOUND         | User Not Found        | 用户不存在                            |
| 3      | INVALID_ARGUMENT  | Request Invalid Value | 请求值无效(如:获取不存在的字段)       |

### 设置当前账号信息

| CodeId | CodeName              | Detail   | meaning                     |
| :----- | :-------------------- | :------- | :-------------------------- |
| 6      | ALREADY_EXISTS        | Conflict | 信息冲突(如:新的ocid被占用) |
| 3      | INVALID_ARGUMENT Ocid | Too Long | 新的ocid太长                |

### 获取用户消息

| CodeId | CodeName         | Detail            | meaning        |
| :----- | :--------------- | :---------------- | :------------- |
| 3      | INVALID_ARGUMENT | Time Format Error | 无法解析时间戳 |
| 3      | INVALID_ARGUMENT | Time Missing      | 缺少time参数   |

### 发送消息

| CodeId | CodeName          | Detail            | meaning      |
| :----- | :---------------- | :---------------- | :----------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有发言权限 |
| 5      | NOT_FOUND         | Session Not Found | 会话不存在   |

### 上传

| CodeId | CodeName           | Detail                       | meaning                        |
| :----- | :----------------- | :--------------------------- | :----------------------------- |
| 3      | INVALID_ARGUMENT   | File Size Error              | 文件大小与metadata不符合       |
| 3      | INVALID_ARGUMENT   | File Hash Error              | 文件hash与metadata不符合       |
| 8      | RESOURCE_EXHAUSTED | Storage Full                 | 该用户储存空间已满             |
| 3      | INVALID_ARGUMENT   | Metadata Error               | 缺少metadata参数或metadata无效 |
| 3      | INVALID_ARGUMENT   | Incorrect Order Of Uploading | 应先上传metadata再上传数据包   |

### 下载

| CodeId | CodeName          | Detail            | meaning      |
| :----- | :---------------- | :---------------- | :----------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有下载权限 |

### 创建新会话

| CodeId | CodeName  | Detail         | meaning          |
| :----- | :-------- | :------------- | :--------------- |
| 5      | NOT_FOUND | User Not Found | 邀请的用户不存在 |

### 获取会话信息

| CodeId | CodeName         | Detail                | meaning                         |
| :----- | :--------------- | :-------------------- | :------------------------------ |
| 5      | NOT_FOUND        | Session Not Found     | 该会话不存在                    |
| 3      | INVALID_ARGUMENT | Request Invalid Value | 请求值无效(如:获取不存在的字段) |

### 设置会话信息

| CodeId | CodeName          | Detail                 | meaning                |
| :----- | :---------------- | :--------------------- | :--------------------- |
| 6      | ALREADY_EXISTS    | Conflict               | 信息冲突               |
| 7      | PERMISSION_DENIED | Cannot Set Name        | 没有设置会话名称的权限 |
| 7      | PERMISSION_DENIED | Cannot Set Avatar      | 没有设置会话头像的权限 |
| 7      | PERMISSION_DENIED | Cannot Set Description | 没有设置会话简介的权限 |

### 撤回消息

| CodeId | CodeName          | Detail            | meaning            |
| :----- | :---------------- | :---------------- | :----------------- |
| 7      | PERMISSION_DENIED | Permission Denied | 没有撤回消息的权限 |
| 5      | NOT_FOUND         | Message Not Found | 撤回的消息不存在   |

### 设置(会话中)身份

| CodeId | CodeName          | Detail              | meaning            |
| :----- | :---------------- | :------------------ | :----------------- |
| 7      | PERMISSION_DENIED | Permission Denied   | 没有设置身份的权限 |
| 5      | NOT_FOUND         | User Not In Session | 用户不存在         |
