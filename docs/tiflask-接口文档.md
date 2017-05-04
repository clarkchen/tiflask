# tiflask 接口文档 - 打分和特征查询接口

## 接口地址
`http://127.0.0.1:5000/api/user_score`

## 请求方式
* Restful Get
* Restful Post

## 请求参数
`{"phone":"18500195632"}`

## 返回结果
```json
{
  "data": {
    "features": {
      "read_article_num": 2,
      "read_article_type_num": 1,
      "recent_3_read_article_type_num": 0,
      "recent_3_read_article_num": 0
    },
    "score": 13
  },
  "update_time": "2017-01-18 17:15:28",
  "success": 1,
  "version": "3.8.3",
  "message": "succ query"
}
```

#### 返回字段说明
| 字段名字    | 含义         | 取值                                | 格式 |
|:------------|:-------------|:------------------------------------|:-----|
| data        | 返回具体信息 | {"score": float, "features": {xxx}} | dict |
| success     | 是否查询成功 | 1:成功 0:失败                       | int  |
| message     | 查询结果信息 | "succ query":成功  "fail query"     | str  |
| update_time | 本次查询时间 |                                     | str  |
| version     | 接口版本号   |                                     | str  |

#### 返回具体信息 Data 对象说明
| 字段名字 | 含义           | 取值                                       | 格式  |
|:---------|:---------------|:-------------------------------------------|:------|
| score    | 用户的评分     | [0-1000]                                   | float |
| features | 用户的具体特征 | 参见 [《用户特征列表》](docs/用户特征列表.md) | dict  |


## 请求范例

```python
# 数据计算范例
url = "http://127.0.0.1:5000/api/user_score"
data = {"phone": "18500195632"}
 
import requests, json
# post 请求
ret_value = requests.post(url, json=data)
# 结果处理
clark = json.loads(ret_value.text, encoding="utf-8")
print(json.dumps(clark), ret_value.status_code)
 
import requests, json
# get 请求
ret_value = requests.post(url, json=data)
# 结果处理
clark = json.loads(ret_value.text, encoding="utf-8")
print(json.dumps(clark), ret_value.status_code)
```
