# 登录
# 1.导入包

import requests


# 2.定义登录方法
def login():
    # 3.定义测试数据
    url = "http://211.103.136.242:8064/authorizations/"
    data = {"username": "python", "password": "12345678"}
    # 4.发送POST请求
    r = requests.post(url, json=data)
    # 5.输出结果
    print(r.json())
    print(r.headers)


# 用户个人信息
def info():
    # 参数
    url = "http://211.103.136.242:8064/user/"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" \
            ".eyJ1c2VybmFtZSI6InB5dGhvbiIsInVzZXJfaWQiOjEsImVtYWlsIjoiOTUyNjczNjM4QHFxLmNvbSIsImV4cCI6MTY1MjkyODYxNX0" \
            ".uVgbYm5twpV3fUUE1xF0RKgragIcjF2cmL-ynvhSWZs "
    headers = {
        'Authorization': 'JWT' + token

    }
    # get请求
    r = requests.get(url, headers=headers)
    # 输出
    print(r.json())


# 获取商品列表数据


def goods_list():
    # 参数
    url = "http://211.103.136.242:8064/categories/115/skus/"
    data = {
        "page": "1",
        "page_size": "10",
        "ordering": "create_time"
    }
    # 请求
    r = requests.get(url, json="data")
    # 结果
    print(r.json())


# 添加商品到购物车
def cart():
    # 参数
    url = "http://211.103.136.242:8064/cart/"
    data = {"sku_id": "3", "count": "1", "selected": "true"}
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" \
            ".eyJ1c2VybmFtZSI6InB5dGhvbiIsInVzZXJfaWQiOjEsImVtYWlsIjoiOTUyNjczNjM4QHFxLmNvbSIsImV4cCI6MTY1MjkyODYxNX0" \
            ".uVgbYm5twpV3fUUE1xF0RKgragIcjF2cmL-ynvhSWZs "
    headers = {
        'Authorization': 'JWT' + token

    }
    # 请求
    r = requests.post(url, json=data, headers=headers)
    # 结果
    print(r.json())


# 订单
def order():
    # 参数
    url = "http://211.103.136.242:8064/orders/"
    data = {"address": "1", "pay_methid": "1"}
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" \
            ".eyJ1c2VybmFtZSI6InB5dGhvbiIsInVzZXJfaWQiOjEsImVtYWlsIjoiOTUyNjczNjM4QHFxLmNvbSIsImV4cCI6MTY1MjkyODYxNX0" \
            ".uVgbYm5twpV3fUUE1xF0RKgragIcjF2cmL-ynvhSWZs "
    headers = {
        'Authorization': 'JWT' + token

    }
    # 请求
    r = requests.post(url, json=data, headers=headers)
    # 结果
    print(r.json())


if __name__ == "__main__":
    login()
    info()
    goods_list()
    cart()
    order()
