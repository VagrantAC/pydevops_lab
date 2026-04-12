# Python DevOps 实验室

基于《基于Python的DevOps》一书的学习项目。

## 项目结构

```
pydevops_lab/
├── labs/              # 实验目录
│   ├── lab1/         # 实验1：Python基础与环境配置
│   ├── lab2/         # 实验2：文件和文件系统自动化处理
│   └── ...
├── common/           # 共享模块
│   ├── utils/       # 工具函数
│   ├── config/      # 共享配置
│   └── helpers/     # 辅助函数
├── scripts/         # 全局脚本
│   ├── hello.py    # 示例脚本
│   ├── setup.py    # 环境设置
│   └── ...
├── tests/           # 全局测试
├── pyproject.toml   # 项目配置和依赖管理
└── .pre-commit-config.yaml  # 代码质量检查配置
```

## 环境搭建

### 1. 安装 Poetry（推荐）

```bash
# 安装 Poetry
curl -sSL https://install.python-poetry.org | python3 -

# 验证安装
poetry --version
```

### 2. 安装项目依赖

```bash
# 使用 Poetry 安装依赖
poetry install

# 或者使用 pip 安装
pip install click pytest pytest-cov python-dotenv
```

### 3. 安装 pre-commit hooks

```bash
# 安装 pre-commit
pip install pre-commit

# 安装 hooks
pre-commit install
```

## 使用指南

### 运行实验

```bash
# 运行特定实验
python labs/lab1/scripts/main.py

# 运行实验测试
pytest labs/lab1/tests/

# 运行所有测试
pytest
```

### 代码格式化

```bash
# 使用 Ruff 格式化代码
ruff format .
ruff check --fix .

# 运行 pre-commit 检查
pre-commit run --all-files
```

### 类型检查

```bash
# 运行 MyPy 类型检查
mypy
```

## 学习内容

### 已完成的实验

- **Lab 1**: Python基础与环境配置
  - Python版本检查
  - 环境配置检查
  - 基础操作演示

### 计划中的实验

#### Python 基础
- **Lab 2**: 文件和文件系统自动化处理
- **Lab 3**: 使用命令行

#### 运维技术
- **Lab 4**: Linux 实用程序
- **Lab 5**: 包管理
- **Lab 6**: 持续集成和持续部署
- **Lab 7**: 监控和日志
- **Lab 8**: pytest 在 DevOps 中的应用

#### 云技术基础
- **Lab 9**: 云计算
- **Lab 10**: Infrastructure as Code (IaC)
- **Lab 11**: 容器技术: Docker 和 Docker Compose
- **Lab 12**: 容器编排: Kubernetes 和 Docker Swarm
- **Lab 13**: Serverless 技术

#### 数据处理
- **Lab 14**: MLOps 和机器学习工程
- **Lab 15**: 数据工程

#### 案例分析
- **Lab 16**: DevOps 惨痛经验和人物访谈

## 开发工具

### 代码格式化
- **Black**: 代码格式化
- **Ruff**: 快速代码检查和格式化
- **isort**: 导入排序

### 代码质量
- **MyPy**: 静态类型检查
- **pytest**: 单元测试
- **pre-commit**: Git hooks 自动检查

## 贡献指南

1. 按照实验编号组织代码
2. 每个实验包含 README.md 说明文档
3. 保持代码格式化和类型检查通过
4. 编写相应的单元测试

## 许可证

MIT License
