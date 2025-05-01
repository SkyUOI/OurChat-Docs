# 服务端网络开发事项

- [SSL/TLS 证书生成](#ssltls证书生成)

## SSL/TLS证书生成
本项目用openssl生成证书生成步骤总体可概括为：

### 生成私钥key

具体而言，可以创建两个文件夹certs和private,
certs中存放最后可以使用的文件，private中存放
中间文件。

第一步生成RSA私钥，举例如下

```bash
openssl genrsa -aes256 -out private/private-key-name.pem 8192
```
其中8192为密钥长度，可自行选择。该命令会提示你输入一个密码，请记住他。


对于非根证书而言，还需要去除私钥文件的加密保护并输出为新文件，命令举例如下
```bash
openssl rsa -in private/private-key-name.pem -out certs/private-key-name.key
```

### 依据私钥生成请求文件csr

请求文件生成命令举例如下
```bash
openssl req -new -key private/private-key-name.pem -out private/crt-name.csr
```
`crt-name`为证书文件名，一般与``private-key-name``一致。

输入后会提示输入一大堆信息。例如国家简码，地区，什么的，如果是根证书，如实填写或者不写都可以。
如果你想要点仪式感，那么就认真写。
**而如果是非根证书**，那么`Common Name`这个
选项要填域名，其他可以随便填。


这一步可能需要输入你刚才设置的pem密码。

### 如果非根证书，那么此时嵌入域名信息

如果是非根证书，请创建一个文件 `private/crt-name.dns.ext` ，
然后粘贴以下信息：
```bash
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth, clientAuth
subjectAltName=@SubjectAlternativeName
 
[ SubjectAlternativeName ]
DNS.1=your.domain.name
DNS.2=此处填写你的网站的域名.cn
DNS.3=如果有多个域名就这么增加.com
DNS.4=*.当然支持泛解析域名.net
```
后面会使用这个文件。

如果你没有域名，而是持有一个固定IP，那么使用如下文件，请创建一个文件 `private/crt-name.ip.ext` ，然后粘贴以下信息：
```bash
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth, clientAuth
subjectAltName=@SubjectAlternativeName
 
[SubjectAlternativeName]
IP.1=192.168.1.2
IP.2=222.90.155.789
```
后面用哪个就附加哪个。一般来说，只需要域名的信息就行了。

### 签发证书pem

使用这个指令签发根证书，有效期为10年
```bash
openssl x509 -req -days 3650 -sha256 -extensions v3_ca -signkey private/private-key-name.pem -i
```
使用这个指令用ca签发非根证书`crt-name.pem`
```bash
openssl x509 -req -days 730 -CA certs/ca-name.pem -CAkey private/ca-private-key-name.pem -CAserial ca-name.srl -CAcreateserial -in private/crt-name.csr -out certs/crt-name.pem -extfile private/crt-name.dns.ext
```
其中，`ca-private-key-name`为根证书的密钥名字。