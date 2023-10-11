# import random
#
# from auto.调试代码 import zentao_cli
#
#
# def newbug(s, uppic_steps, host, get_uid):
#     data = {"product": 5,
#             "module": 31,
#             "project": 14,
#             "openedBuild[]": "trunk",
#             "assignedTo": "fangna",
#             "type": "codeerror",
#             "title": "接口自动化bug0815_15_附图片、附件:",
#             "severity": 3,
#             "pri": 3,
#             "steps": "<p>[步骤]<img src={} alt="" /></p><br/><p>[结果]</p><br/><p>[期望]</p><br/>".format(uppic_steps),
#             "oldTaskID": 0,
#             "status": "active",
#             "uid": get_uid,
#             "caseVersion": 0,
#             "case": 0,
#             "result": 0,
#             "testtask": 0}
#
#     r = s.post(host + "/bug-create-5-0-moduleID=0.html", data=data)
#     print("提交bug,响应内容:{}".format(r.text))
#
#
# if __name__ == '__main__':
#     cli = zentao_cli("http://192.168.110.129:81/zentao", "fangna", "fangna@123")
#     cli.login()
#     newbug(cli.s, "6524b5f182371", "http://192.168.110.129:81/zentao", "6524b5f184671")

import yaml


def read_yaml(path):
    # 读取YAML文件
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    # 返回读取到的全部内容
    return data
