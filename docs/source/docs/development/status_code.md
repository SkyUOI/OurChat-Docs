# OurChat 状态码

## 状态码表格

| code | meaning        |
| :--- | :------------- |
| 0    | 运行成功       |
| 1    | 服务器错误     |
| 2    | 服务器维护中   |
| 3    | 请求信息不存在 |
| 4    | 新增信息已存在 |
| 5    | 参数错误       |
| 6    | 账号限制       |
| 7    | 等待超时       |
| 8    | 未知错误       |

## 各种信息下的状态码解释

### 获取会话信息返回信息

| code | meaning      |
| :--- | :----------- |
| 0    | 获取成功     |
| 1    | 服务器错误   |
| 2    | 服务器维护中 |
| 3    | 该会话不存在 |
| 8    | 未知错误     |

### 注册返回信息

| code | meaning      |
| :--- | :----------- |
| 0    | 注册成功     |
| 1    | 服务器错误   |
| 2    | 服务器维护中 |
| 4    | 邮箱已存在   |
| 5    | 未完成验证   |
| 8    | 未知错误     |

### 登录返回信息

| code | meaning       |
| :--- | :------------ |
| 0    | 登录成功      |
| 1    | 服务器错误    |
| 2    | 服务器维护中  |
| 5    | 账号/密码错误 |
| 8    | 未知错误      |

### 新建会话返回信息

| code | meaning              |
| :--- | :------------------- |
| 0    | 新建成功             |
| 1    | 服务器错误           |
| 2    | 服务器维护中         |
| 6    | 到达创建会话数量上限 |
| 8    | 未知错误             |

### 获取账号信息返回信息

| code | meaning      |
| :--- | :----------- |
| 0    | 获取成功     |
| 1    | 服务器错误   |
| 2    | 服务器维护中 |
| 3    | 该账号不存在 |
| 8    | 未知错误     |

### 获取服务器状态

| code | meaning      |
| :--- | :----------- |
| 0    | 服务器正常   |
| 2    | 服务器维护中 |
| 8    | 未知错误     |

### 验证状态

| code | meaning      |
| :--- | :----------- |
| 0    | 验证通过     |
| 1    | 服务器错误   |
| 2    | 服务器维护中 |
| 7    | 验证超时     |
| 8    | 未知错误     |

### 注销返回信息

| code | meaning      |
| :--- | :----------- |
| 0    | 注销成功     |
| 1    | 服务器错误   |
| 2    | 服务器维护中 |
| 5    | 未完成验证   |
| 8    | 未知错误     |

### 设置账号信息返回信息

| code | meaning       |
| :--- | :------------ |
| 0    | 设置成功      |
| 1    | 服务器错误    |
| 2    | 服务器维护中  |
| 5    | json 格式错误 |
| 8    | 未知错误      |

### 上传文件返回信息

| code | meaning        |
| :--- | :------------- |
| 0    | 上传成功       |
| 1    | 服务器内部错误 |
| 2    | 服务器维护中   |
| 6    | 请求被拒绝     |

### 邮件发送

| code | meaning              |
| :--- | :------------------- |
| 0    | 上传成功             |
| 1    | 服务器内部错误       |
| 3    | 请求邮箱无法发送成功 |
| 6    | 请求被拒绝           |

### 同意加入会话返回信息

| code | meaning        |
| :--- | :------------- |
| 0    | 同意成功       |
| 1    | 服务器内部错误 |
| 2    | 服务器维护中   |
| 6    | 请求被拒绝     |
