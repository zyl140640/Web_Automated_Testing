import requests
import json


class zentao_cli(object):
    session = None  # 用于实现单例类，避免多次申请sessionID
    sid = None

    def __init__(self, url, account, password, override=False):
        self.url = url
        self.account = account
        self.password = password
        self.session_override = override
        self.pages = {
            "sid": "/api-getSessionID.json",  # 获取sid的接口
            "login": "/user-login.json?zentaosid={0}",  # 登录的接口
            "get_product_list": "/product-index-no.json",
        }
        self.s = None
        self.sid = None

    def req_get(self, url):
        # 请求并返回结果
        web = requests.get(url)
        print(f"cookies是: {web.cookies}")
        if web.status_code == 200:
            resp = json.loads(web.content)
            if resp.get("status") == "success":
                return True, resp
            else:
                return False, resp

    def req_post(self, url, body):
        # 请求并返回结果
        res = requests.post(url=url, data=body)
        print(f"cookies是: {res.cookies}")
        if res.status_code == 200:
            resp = json.loads(res.content)
            if resp.get("status") == "success":
                return True, resp
            else:
                return False, resp

    def login(self):
        if self.s is None:
            if not self.session_override and zentao_cli.session is not None:
                self.s = zentao_cli.session
                self.sid = zentao_cli.sid
            else:
                # 新建会话
                self.s = requests.session()
                res, resp = self.req_get(self.url.rstrip("/") + self.pages["sid"])
                if res:
                    print("获取sessionID成功")
                    self.sid = json.loads(resp["data"])["sessionID"]
                    zentao_cli.sid = self.sid
                    body = {'account': self.account, 'password': self.password, 'keepLogin[]': 'on',
                            'referer': self.url.rstrip("/") + '/my/'}
                    login_res, login_resp = self.req_post(self.url.rstrip("/") + self.pages["login"].format(self.sid),
                                                          body)
                    if login_res:
                        print("登录成功")
                        zentao_cli.session = self.s

                print(f"res的内容{res}")
                print(f"resp的内容{resp}")

    def get_product_list(self):
        req_url = self.url.rstrip("/") + self.pages["get_product_list"]
        res, resp = self.req_get(req_url + "?zentaosid=" + self.sid)
        if res:
            data = resp['data']
            products = json.loads(data)['products']
            return products.keys(), products.values()

    def get_prodoct_bug(self):
        url = "http://192.168.110.129:81/zentao/bug-create-5-0-moduleID=0.json"
        header = {'Content-Type': "application/x-www-form-urlencoded; charset=utf-8",
                  'zentaosid': self.sid
                  }  # 设置请求头
        data = {
            "product": "5",  # int 所属产品 * 必填
            "module": "38",  # int 所属模块
            "project": "17",  # int 所属项目
            "openedBuild": "trunk",  # int | trunk 影响版本 * 必填
            "assignedTo": "fangna",  # string 指派给
            "deadline": "2020-07-28",  # date 截止日期 日期格式：YY - mm - dd，如：2019 - 01 - 01
            "type": "codeerror",  # bug类型
            "os": "",
            "browser": "",
            "color": "",
            "title": "feedback",  # 标题
            "severity": "3",  # int 严重程度 取值范围：1 | 2 | 3 | 4
            "branch": "2",  # int 分支 / 平台
            "bugPhase": "live",  # bug在什么环境发现
            "pri": "3",  # int 优先级 取值范围：0 | 1 | 2 | 3 | 4
            "keywords": "",  # string 关键词
            "story": 1143,  # 需求
            "steps": "set bug link in here"  # string 重现步骤
        }
        ss = requests.post(url=url, data=data, headers=header)
        print("结果" + ss.text)


if __name__ == "__main__":

    cli = zentao_cli("http://192.168.110.129:81/zentao", "fangna", "fangna@123")
    cli.login()
    cli.get_prodoct_bug()
    print(cli.get_product_list())
