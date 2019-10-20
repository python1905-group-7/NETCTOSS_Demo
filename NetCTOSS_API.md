# NetCTOSS_API文档



## 1、get_user

**获取当前登录管理员的信息**



接口调用请求说明：

```
http请求方式：GET
URL：/login/get_user/
```

请求接口参数：无



返回说明

正确返回JSON数据：

```
{
    "msg": "get",
    "status": 200,
    "user": {
        "id": 1,
        "admin_code": "cluom",
        "password": "cluom",
        "name": "name",
        "telephone": "110",
        "email": "c_l-m@qq.com", 
        "enrolldate": "2019-10-19"
    }
}
```

| 参数   | 说明               |
| ------ | ------------------ |
| msg    | 接口操作提示       |
| status | 状态码             |
| user   | 当前登录管理员信息 |

管理员未登录时返回JSON数据：

```
{
	"msg": "未登录",
	"status": 201
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |