# coding:utf-8
import requests, hashlib, time, json


class bbxrequest:
    access_key1 = "a10000001"  # 账号1 的 登陆密钥
    secret1 = "b10000001"  # 账号1的 加密密钥
    access_key2 = "a10000002"
    secret2 = "b10000002"
    # header
    header = {
        "Host": "api.bbx.com",
        "Bbx-Accesskey": "a10000001",  # 此处是登录密钥
        "Bbx-Sign": "",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Accept-Language": "zh-Hans-CN;q=1",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "BTStore/1.0 (iPhone; iOS 11.2.2; Scale/2.00)",
        "Content-Type": "application/json"
    }

    #  Way :1 和2 分别是买卖单类型
    submit_oder_buy_data = {"category": 1, "fee_coin_code": "BBX", "stock_code": "ETH/BBX", "price": 2000000000,
                             "vol": 100000000, "way": 1, "nonce": 1520315223}

    def __init__(self):
        pass

    def run(self):
        self.submit_oder_buy_data["nonce"] = int(time.time())
        self.bbxsign = json.dumps(self.submit_oder_buy_data) + self.secret1
        self.header["Bbx-Sign"] = self.getmd5_value(text=self.bbxsign)
        print("HEADER is : ", self.header)
        print("BODY is : ", json.dumps(self.submit_oder_buy_data))
        self.request()

    def getorder(self):
        pass
        orderrequest = requests.get('http://api.bbx.com/v1/ifmarket/vipGetOrders')
        # 这段还没通

    def order_cancel(self):
        pass

    def request(self):
        request = requests.post('http://api.bbx.com/v1/ifmarket/vipSubmitOrder', headers=self.header,
                                data=json.dumps(self.submit_oder_buy_data))
        response_bbx = request.text
        print(response_bbx)

    def getmd5_value(self, text):
        field5 = hashlib.md5()
        field5.update(text.encode(encoding="utf-8"))
        md5value = field5.hexdigest()
        assert isinstance(md5value, object)
        return md5value


if __name__ == '__main__':
    pass
    bbx = bbxrequest()
    bbx.run()
