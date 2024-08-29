# http信息交换格式

## 文件上传

接口:`/upload/{url}`
请求类型:`post`

|参数|说明|默认值|
|:--|:--|:---|
|key|验证密钥|不适用|
|auto_clean|该图片是否自动清理|true|

|状态码|说明|
|:---|:---|
|NotFound|请求上传的资源不存在|
|InternalServerError|服务器内部错误|
|BadRequest|哈希不匹配等|
|Ok|成功|

直接上传文件内容即可

**关于获取该接口，参见[交换格式](./msg_json.md#图片上传请求)**
