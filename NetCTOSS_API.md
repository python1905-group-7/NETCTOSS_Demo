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

```json
{
    "msg": "获取成功!",
    "status": 200,
    "data": {
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
| data   | 当前登录管理员信息 |



管理员未登录时返回JSON数据：

```json
{
	"msg": "未登录!",
	"status": 201
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



## 2、get_cost

**根据资费ID获取资费信息**



接口调用请求说明：

```
http请求方式：GET
URL：/fee/get_cost/
```

请求接口参数：

| 参数    | 说明   | 数据类型 |
| ------- | ------ | -------- |
| cost_id | 资费ID | String   |



返回说明

正确返回JSON数据：

```json
{
    "msg": "获取成功!",
    "status": 200,
    "data": {
        "id": 1,
        "creatime": "2013-05-14 01:17",
        "startime": "2019-10-21 14:24",
        "name": "5.9元套餐",
        "base_duration": "20",
        "base_cost": 6.0,
        "unit_cost": 0.0111,
        "status": null,
        "descr": "5.9元20小时/月,超出部分0.0111分/秒",
        "cost_type": "2"
    }
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |
| data   | 资费信息     |



未查询到数据时返回JSON数据:

```json
{
	"msg": "没有资费信息!",
	"status": 404
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



管理员未登录时返回JSON数据：

```json
{
	"msg": "未登录!",
	"status": 201
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



## 3、get_cost_list

**获取所有资费信息**



接口调用请求说明：

```
http请求方式：GET
URL：/fee/get_cost_list/
```

请求接口参数：无



返回说明

正确返回JSON数据：

```json
{
    "msg": "获取成功!",
    "status": 200,
    "data": [
        {
            "id": 1,
            "creatime": "2013-05-14 01:17",
            "startime": "2019-10-21 14:24",
            "name": "5.9元套餐",
            "base_duration": "20",
            "base_cost": 6.0,
            "unit_cost": 0.0111,
            "status": null,
            "descr": "5.9元20小时/月,超出部分0.0111分/秒",
            "cost_type": "2"
        },
        ...
    ]
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |
| data   | 资费信息列表 |



未查询到数据时返回JSON数据:

```json
{
	"msg": "没有资费信息!",
	"status": 404
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



管理员未登录时返回JSON数据：

```json
{
	"msg": "未登录!",
	"status": 201
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



## 4、add_cost

**添加资费信息**



接口调用请求说明：

```
http请求方式：GET
URL：/fee/add_cost/
```

请求接口参数：

| 参数          | 说明     | 数据类型 |
| ------------- | -------- | -------- |
| name          | 资费名称 | String   |
| cost_type     | 资费类型 | String   |
| base_duration | 基本时长 | String   |
| base_cost     | 基本费用 | String   |
| unit_cost     | 单位费用 | String   |
| descr         | 资费说明 | String   |



返回说明

正确返回JSON数据：

```json
{
	"msg": "添加成功!",
	"status": 200
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



资费名称重复返回JSON数据:

```json
{
	"msg": "资费名称重复!",
	"status": 501
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



传入的数据类型错误返回JSON数据:

```json
{
	"msg": "数据类型错误!",
	"status": 500
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



管理员未登录时返回JSON数据：

```json
{
	"msg": "未登录!",
	"status": 201
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



## 5、update_to_cost_status

**修改资费状态**



接口调用请求说明：

```
http请求方式：GET
URL：/fee/update_to_cost_status/
```

请求接口参数：

| 参数    | 说明   | 数据类型 |
| ------- | ------ | -------- |
| cost_id | 资费ID | String   |



返回说明

正确返回JSON数据：

```json
{
	"msg": "修改成功!",
	"status": 200
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



传入的数据类型错误返回JSON数据:

```json
{
	"msg": "数据类型错误!",
	"status": 500
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



没有资费信息返回JSON数据:

```json
{
	"msg": "没有该资费的信息!",
	"status": 404
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



管理员未登录时返回JSON数据：

```json
{
	"msg": "未登录!",
	"status": 201
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |





## 6、update_to_cost

**修改资费信息**



接口调用请求说明：

```
http请求方式：GET
URL：/fee/update_to_cost/
```

请求接口参数：

| 参数    | 说明   | 数据类型 |
| ------- | ------ | -------- |
| cost_id | 资费ID | String |
| name| 资费名称 | String |
| cost_type     | 资费类型 | String |
| base_duration | 基本时长 | String |
| base_cost     | 基本费用 | String |
| unit_cost     | 单位费用 | String |
| descr         | 资费说明 | String |



返回说明

正确返回JSON数据：

```json
{
	"msg": "修改成功!",
	"status": 200
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



传入的数据类型错误返回JSON数据:

```json
{
	"msg": "数据类型错误!",
	"status": 500
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



没有资费信息返回JSON数据:

```json
{
	"msg": "没有该资费的信息!",
	"status": 404
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



资费名称重复返回JSON数据:

```json
{
	"msg": "资费名称重复!",
	"status": 501
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



管理员未登录时返回JSON数据：

```json
{
	"msg": "未登录!",
	"status": 201
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |





## 7、delete_to_cost

**删除资费信息**



接口调用请求说明：

```
http请求方式：GET
URL：/fee/delete_to_cost/
```

请求接口参数：

| 参数    | 说明   | 数据类型 |
| ------- | ------ | -------- |
| cost_id | 资费ID | String   |



返回说明

正确返回JSON数据：

```json
{
	"msg": "删除成功!",
	"status": 200
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



没有资费信息返回JSON数据:

```json
{
	"msg": "没有该资费的信息!",
	"status": 404
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



管理员未登录时返回JSON数据：

```json
{
	"msg": "未登录!",
	"status": 201
}
```

| 参数   | 说明         |
| ------ | ------------ |
| msg    | 接口操作提示 |
| status | 状态码       |



