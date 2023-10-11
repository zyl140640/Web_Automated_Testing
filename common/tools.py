import os
from os import listdir
import json

import yaml


def detect_video():
    my_path = "./case_video/"

    for file_name in listdir(my_path):

        if file_name.endswith('.webm'):
            os.remove(my_path + file_name)


# 需要转换格式的视频文件，文件真实存在


# 设置报告窗口的标题
def set_windows_title(new_title):
    """  设置打开的 Allure 报告的浏览器窗口标题文案
    @param new_title:  需要更改的标题文案 【 原文案为：Allure Report 】
    @return: 没有返回内容，调用此方法传入需要更改的文案即可修改窗体标题温拿
    """
    # report_title_filepath：这里主要是去拿到你的HTML测试报告的绝对路径【记得换成你自己的】
    report_title_filepath = r"reports/index.html"
    # 定义为只读模型，并定义名称为: f
    with open(report_title_filepath, 'r+', encoding="utf-8") as f:
        # 读取当前文件的所有内容
        all_the_lines = f.readlines()
        f.seek(0)
        f.truncate()
        # 循环遍历每一行的内容，将 "Allure Report" 全部替换为 → new_title(新文案)
        for line in all_the_lines:
            f.write(line.replace("Allure Report", new_title))
        # 关闭文件
        f.close()


# 测试报告文案获取的文件地址
title_filepath = r"reports/widgets/summary.json"


# 获取 summary.json 文件的数据内容
def get_json_data(name):
    # 定义为只读模型，并定义名称为f
    with open(title_filepath, 'rb') as f:
        # 加载json文件中的内容给params
        params = json.load(f)
        # 修改内容
        params['reportName'] = name
        # 将修改后的内容保存在dict中
        dict = params
    # 关闭json读模式
    f.close()

    # 返回dict字典内容
    return dict


# 写入json文件
def write_json_data(dict):
    # 定义为写模式，名称定义为r
    with open(title_filepath, 'w', encoding="utf-8") as r:
        # 将dict写入名称为r的文件中
        json.dump(dict, r, ensure_ascii=False, indent=4)
    # 关闭json写模式
    r.close()


def read_yaml(path):
    """
     读取yaml文件内容
    :param path: 文件路径
    :return: 返回文件全部内容
    示例:  data[""]   data[""][""]
    """
    # 读取YAML文件
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    # 返回读取到的全部内容
    return data
