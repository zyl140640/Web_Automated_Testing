# import requests
#
# session = requests.Session()
#
# login_url = "http://192.168.110.210:9016/api/Auth/Login"
# project_url = "http://192.168.110.210:9016/api/Project/Project?ProjectName=&OrderColumn=CreateTime&OrderType=desc&PageIndex=1&PageSize=20&EnterpriseId=&BelongOrganId="
# gateway_url = "http://192.168.110.210:9016/api/Project/Gateway/Gateway?PageIndex=1&PageSize=20&GatewaySN=&OrderColumn=CreateTime&OrderType=desc&GatewayName=&ProjectName=&ProjectId=&BelongOrganId=&EnterpriseId="
# device_url = "http://192.168.110.210:9016/api/Project/Device/List?PageIndex=1&PageSize=20&DeviceName=&Status=&GatewayStatus=&AlarmStatus=&GatewayName=&GatewaySN=&ProjectName=&ProjectId=&OrderColumn=CreateTime&OrderType=desc&EnterpriseId=&BelongOrganId=&DeviceStatus="
# UserNO = "root1"
# Pwd = "123456"
# Code = "1115qi"
# payload = "{\"UserNO\":\"root1\",\"Pwd\":\"123456\",\"OpenId\":\"\",\"Code\":\"1115qi\"}"
# headers = {
#     'Cookie': 'SECKEY_ABVK=2QCE4HDGLZlGSj4UX0LG3s96sv1EvvwWPq/WoiBxjAw%3D; BMAP_SECKEY=PLtNgsecuApGVxHN1bu0NX8YpFXgu76o8HcIf_LHoURLDsWnP02Z8qTuZOe_P97lSAWtN2ZUmtxC62mTgws2KWf3PVbgk1mRGwhmfBhS9eFlgD9-kLAA0TmlpL8XfI1kMn0SXjKZGbNvWC5LSUWaWI8eUCKVdzH_QtfXWYO4E2N01EXrP8aTi9bfA0-4ZBaQ',
#     'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
#     'Content-Type': 'application/json;charset=UTF-8',
#     'Accept': '*/*',
#     'Host': '192.168.110.210:9016',
#     'Connection': 'keep-alive'
# }
# #
# responses = session.post(login_url, headers=headers, data=payload)
# token = responses.json()['Data']['Token']
#
# headers = {
#     'Authorization': f'Bearer {token}',
#     'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
#     'Accept': '*/*',
#     'Host': '192.168.110.210:9016',
#     'Connection': 'keep-alive'
# }
#
# project_response = requests.request("GET", project_url, headers=headers)
# project_count = project_response.json()['Data']['TotalCount']
#
# gateway_response = requests.request("GET", gateway_url, headers=headers)
# gateway_count = gateway_response.json()['Data']['TotalCount']
#
# device_response = requests.request("GET", device_url, headers=headers)
# device_count = device_response.json()['Data']['TotalCount']
#
# print(
#     f"企业编码: {Code},用户账号: {UserNO},项目总数: {project_count},网关总数: {gateway_count},设备总数: {gateway_count}")
import subprocess

if __name__ == '__main__':
    # os.system('adb devices')
    odes = "adb devices"
    re = subprocess.getoutput('adb devices')
    print(re)
    pi = subprocess.Popen(odes, shell=True, stdout=subprocess.PIPE)
    print(pi.stdout.read())
