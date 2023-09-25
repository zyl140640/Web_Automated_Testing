import os
import time

import pytest

if __name__ == '__main__':
    # # 清空录屏文件
    # detect_video()
    # 执行pytest
    pytest.main(['-s', '-v', ])
    # pytest.main(['-s', '-v', 'testcases/test_add_gateway.py::TestAddGateway::test_add_gateway'])
    time.sleep(3)
    # 生成测试报告
    os.system("allure generate ./temps -o ./reports --clean")
