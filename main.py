import os
import time

import pytest

if __name__ == '__main__':
    # 执行pytest
    pytest.main(['-s', '-v'])
    # pytest.main(['-s', '-v', 'testcases/test_project.py::TestAddProject'])
    time.sleep(3)
    # 生成测试报告
    os.system("allure generate ./temps -o ./reports --clean")
