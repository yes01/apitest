
# 公共的操作函数

def login(s):
    '''登录获取token'''
    # s = requests.session()  # 会话  代码里面的浏览器，模拟浏览器的功能
    url = "https://uat.cubeace.com/gameflaskapi/api/v1/account/websignin"
    body = {
        "text": "0.0012@qq.com",
        "password": "12345678"
    }

    # 转json
    r = s.post(url, json=body)
    print(r.json())

    # token
    accessToken = r.json()["result"]["accessToken"]
    print("取出accessToken:%s" % accessToken)

    h = {
        "authorization": "Bearer "+"accessToken %s" % accessToken
    }
    s.headers.update(h)  # 更新到session会话
    # 更新之后的头部
    print(s.headers)
    return accessToken
