import os
import time

''
import pytest

from common.tools import *

if __name__ == '__main__':
    clear_directory()
    # 执行pytest
    pytest.main(['-s', '-v'])
    # pytest.main(['-s', '-v',
    #              'testcases/test_2_project/gateway_manage/test_gateway_pt.py::TestGatewayXieYi::test_read_gateway'])
    time.sleep(3)
    # 生成测试报告
    os.system("allure generate ./temps -o ./reports --clean")
    # # 修改Allure测试报告标题
    # set_windows_title("御控工业云平台Web自动化测试报告")
    # report_title = get_json_data("御控工业云平台Web自动化测试报告")
    # write_json_data(report_title)
    # # Jenkins上运行会导致出问题，找不到文件
