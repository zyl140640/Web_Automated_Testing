import time

import pytest

from common.tools import *

if __name__ == '__main__':
    # 清除文件夹
    clear_directory()
    # 运行测试用例
    pytest.main(['-s', '-v'])
    # pytest.main(['-s', '-v',
    #              'testcases/test_3_data/test_login.py'])
    # 等待3秒
    time.sleep(3)
    # 生成Allure测试报告
    os.system("allure generate ./temps -o ./reports --clean")
