# Public Info

对于每个个人，信息被分为公有的和私有的。公有信息即意味着可以被任何人访问，不论其是不是本人或好友。数据库中保存了`update_time`和`public_update_time`两者，分别用于表示所有信息最后的更新时间和公有信息最后的更新时间。

其中，公有信息列举如下(grpc中的字段名称)，未列出的都是私有信息:

|字段|
|:---|
|user_name|
|user_defined_status|
|avatar_key|
|ocid|
