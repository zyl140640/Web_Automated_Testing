# test_search.py
import os
import time

import pytest

from common.tools import detect_video

if __name__ == '__main__':
    # 清空录屏文件
    detect_video()
    # 执行pytest
    pytest.main(['-s', '-v'])
    time.sleep(3)
    # 生成测试报告
    os.system("allure generate ./temps -o ./reports --clean")
