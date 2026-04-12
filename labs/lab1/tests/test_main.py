"""Lab 1 测试文件"""

import sys
from pathlib import Path

# 添加scripts目录到路径
scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

import main


def test_check_python_version():
    """测试Python版本检查"""
    result = main.check_python_version()
    assert result is True


def test_check_environment():
    """测试环境检查"""
    result = main.check_environment()
    assert result is True


def test_basic_operations():
    """测试基础操作"""
    result = main.basic_operations()
    assert result is True


def test_main():
    """测试主函数"""
    result = main.main()
    assert result == 0
