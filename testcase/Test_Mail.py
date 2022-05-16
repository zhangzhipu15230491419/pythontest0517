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


if __name__ == "__main__":
    login()
