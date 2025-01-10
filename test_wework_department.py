# 创建部门
import requests


class TestWeworkDepatmet:
    # 获取token
    def setup_class(self):
        self.corpid = "wwcc04894b92fd9047"
        self.corpsecret = "zBVws3TQeW83eUhs0JCXepnvQHO-n44WqAQZm8q0HhU"
        # 获取token
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid":self.corpid,
            "corpsecret":self.corpsecret
        }
        r = requests.request(url=url,method="get",params=params)
        print(r.json())
        self.token = r.json().get("access_token")
        print(self.token)

    # 创建部门
    def test_create_department(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": "青春中心4层1",
            "name_en": "QCZX41",
            "parentid": 1,
            "order": 1,
            "id": 4
        }
        # r = requests.request(url=url, method="post", data=data)，这样写报错，研究一下
        r = requests.request(url=url, method="post", json=data)
        print(r.json())
        assert r.status_code == 200
        assert r.json().get("errcode") == 0
        ids = r.json().get("id")
        assert ids == 4