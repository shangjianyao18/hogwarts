import requests


class TestWeworkToken:
    def setup_class(self):
        self.corpid = "wwcc04894b92fd9047"
        self.corpsecret = "zBVws3TQeW83eUhs0JCXepnvQHO-n44WqAQZm8q0HhU"

        # 通过请求，获取token
    # def test_get_token(self):
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
    #     r = requests.request(url=url,method="get")
    #     print(r.json())
    #     token = r.json().get("access_token")
    #     print(f"获取到的token为:{token}")

    def test_get_token_dict(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {
            "corpid":self.corpid,
            "corpsecret":self.corpsecret
        }
        r = requests.request(url=url,method="get",params=param)
        print(r.text)
        token = r.json().get("access_token")
        print(f"获取到的token为：{token}")




