# 端到端加密

- [流程概述](#流程概述)
- [发送消息时的注意事项](#发送消息时的注意事项)

## 流程概述

### 注册用户

假设流程中涉及的操作方为：

| 操作方  | 描述             |
|:------:|:---------------:|
| server | 服务器           |
| userA  | 该用户执行注册操作 |

userA在向server注册前要生成一对RSA密钥对——公钥和私钥，并在`RegisterRequest`中将`public_key`字段设置为公钥。确保私钥不能泄漏给任何其他操作者，包括服务器，并保存在本地。

### 创建端到端加密的群聊

| 操作方  | 描述         |
|:------:|:-----------:|
| server | 服务器       |
| userA  | 该用户创建群聊 |

userA先创建一个用于对称加密（任何算法均可）的`room_key`，保存在本地，确保不泄漏给其他不信任的操作者，包括服务器。

接着userA向server发送请求创建群聊时，在`NewSessionRequest`中设置`e2ee_on`为`true`即可。

### 同意某人加入群聊

假设流程中涉及的操作方为：

| 操作方  | 描述                                |
|:------:|:----------------------------------:|
| server | 服务器                              |
| userA  | 某个已在该群的用户                     |
| userB  | 尚未在该群的用户，将要向userA发送入群申请 |

1. userB向server发送`join_session`请求

2. userA将收到`JoinSessionApproval`的消息，其中将包含userB的公钥，即`public_key`字段。用`public_key`加密`room_key`, 获得加密后的`encrypted_room_key`

3. userA向server发送`allow_user_join_session`请求，将`room_key`字段设置为`encrypted_room_key`

4. userB将收到`AllowUserJoinSessionNotification`的消息，其中将包含`room_key`字段，内容是`encrypted_room_key`，利用自己的RSA私钥将其解密，得到`room_key`原始内容，同样，不能泄漏给其他不信任的操作者，包括服务器。

### 邀请某人加入群聊

假设流程中涉及的操作方为：

| 操作方  | 描述                             |
|:------:|:-------------------------------:|
| server | 服务器                           |
| userA  | 某个已在该群的用户，将要邀请userB加入 |
| userB  | 尚未在该群的用户                   |

1. userA向server发送`invite_user_to_session`请求

2. userB将收到`InviteUserToSession`的消息，接着利用其中的信息，向server发送`accept_join_session_approval`请求

3. userA将收到`AcceptSessionNotification`的消息，其中将包含userB的公钥，即`public_key`字段。用`public_key`加密`room_key`, 获得加密后的`encrypted_room_key`

4. userA向server发送`send_room_key`请求，将`room_key`字段设置为`encrypted_room_key`

5. userB将收到`ReceiveRoomKeyNotification`的消息，其中将包含`room_key`字段，内容是`encrypted_room_key`，利用自己的RSA私钥将其解密，得到`room_key`原始内容，同样，不能泄漏给其他不信任的操作者，包括服务器。

### `room_key`的更换

更换条件：当距离上次更换相差一定时间（可设置）或有人退出群聊时，该群会被标记，当有人在被标记的群发言时，会进行密钥交换操作。用户向服务器发送的`e2eeize_session`请求也可以让该群的`room_key`进行更换。

假设流程中涉及的操作方为：

| 操作方  | 描述                   |
|:------:|:---------------------:|
| server | 服务器                 |
| userA  | 首个在群被标记后发言的用户 |
| userB  | 其他在该群的用户         |

1. 需要更新时，userA会在消息发送成功后收到`UpdateRoomKeyNotification`的消息，这时需要userA对该群的`room_key`进行更新操作，以及还有若干`SendRoomKeyNotification`的消息，其中包含其他成员的公钥，以下以userB为例

2. userA将更新后的`room_key`利用userB的公钥加密，获得加密后的`encrypted_room_key`

3. userA向server发送`send_room_key`请求，将`room_key`字段设置为`encrypted_room_key`

4. userB将收到`ReceiveRoomKeyNotification`的消息，其中将包含`room_key`字段，内容是`encrypted_room_key`，利用自己的RSA私钥将其解密，得到`room_key`原始内容，同样，不能泄漏给其他不信任的操作者，包括服务器。

### 切换群聊的端到端加密状态（开/关）

假设流程中涉及操作方为：

| 操作方  | 描述                       |
|:------:|:-------------------------:|
| server | 服务器                     |
| userA  | 在该群且具有`Owner`权限的用户 |

#### 设置群聊为端到端加密

1. userA向server发送`e2eeize_session`请求

2. 随后就是[更换`room_key`的流程](#room_key的更换)

#### 设置群聊为非端到端加密

1. userA向server发送`dee2eeize_session`请求

## 发送消息时的注意事项

在端到端加密的群聊里，每个用户选择在发送消息时若选择加密，则利用`room_key`加密。

一个`room_key`一直到被更换之前，都对期间发的消息有效，任何持有`room_key`的客户端都可以对被加密的消息解密。
