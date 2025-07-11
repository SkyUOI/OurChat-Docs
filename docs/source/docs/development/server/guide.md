# 服务端各部分开发指南

## 权限

### Session 操作权限

#### 定义位置

请参考`server/migration/src/m20241229_022701_add_role_for_session.rs`文件，并在`PredefinedPermissions`和`PredefinedRoles`中添加自己所需的权限和角色。

大体上来说，如果你定义了一个新 permission，你需要考虑要将它添加到哪些原有的角色中，例如，无论你添加了什么 permission, Admin 总是该具有此权限。

然后请注意，不要直接修改下方的`init_role_table`函数，以防止数据库迁移的相关问题，正确做法是使用`sea migrate generate xxx`，然后在里面编写新的权限相关代码。

#### 权限相关操作

- `if_permission_exist`: 检查某权限是否存在
- `get_all_roles_of_session`: 获取某个 session 定义的所有角色
- `query_session_role`: 获取所有在某个 session 中为特定角色的用户
