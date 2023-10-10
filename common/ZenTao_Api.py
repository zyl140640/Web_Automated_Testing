import requests

loginhost = "http://192.168.110.129:81/zentao/index.php?m=user&f=login"  # 登录url
add_bughost = "http://192.168.110.129:81/zentao/index.php?m=bug&f=create&productID=5&branch=0&extra=moduleID=0"  # new bug url


def add_bug():
    header = {'Content-Type': "application/x-www-form-urlencoded; charset=utf-8"}  # 设置请求头
    datas = {"account": "fangna", "password": "fangna@123"}  # 定义请求的数据
    s = requests.session()  # 实例化一个session对象
    response = s.post(loginhost, headers=header, data=datas)  # 使用session发起请求

    print(response.content)

    data = {
        "product": "5",  # int 所属产品 * 必填
        "openedBuild": "trunk",  # int | trunk 影响版本 * 必填
        "branch": "2",  # int 分支 / 平台
        "module": "31",  # int 所属模块
        "project": "17",  # int 所属项目
        "assignedTo": "fangna",  # string 指派给
        "deadline": "2020-07-28",  # date 截止日期 日期格式：YY - mm - dd，如：2019 - 01 - 01
        "type": "codeerror",  # bug类型
        "severity": "3",  # int 严重程度 取值范围：1 | 2 | 3 | 4
        "pri": "3",  # int 优先级 取值范围：0 | 1 | 2 | 3 | 4
        "keywords": "",  # string 关键词
        "title": "接口提交",  # 标题
        "story": "",  # 需求
        "steps": "set bug link in here"  # string 重现步骤
    }
    responses = s.post(add_bughost, headers=header, data=data)
    print(responses.content.decode("utf-8"))


if __name__ == '__main__':
    add_bug()
