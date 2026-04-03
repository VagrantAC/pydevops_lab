# 🐍 Python DevOps 实验室

> **Project Context for AI Assistant**

---

## 📋 Project Overview

**Python DevOps 实验室** (Python DevOps Lab) is a learning project based on the book *"基于 Python 的 DevOps"* (DevOps with Python).

| Attribute | Value |
|-----------|-------|
| **Status** | ✅ Initialized |
| **Language** | Python ^3.10 |
| **Type** | Learning/Educational |
| **Package Manager** | Poetry |
| **Framework** | pytest |

### 🎯 Purpose
- Learn Python for DevOps practices
- Practice automation, CI/CD, containerization, and cloud technologies
- Build hands-on experience with modern DevOps tooling

### 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| **Language** | Python |
| **Package Manager** | Poetry |
| **Testing** | pytest, pytest-cov |
| **Linting** | ruff, black, mypy |
| **Containers** | Docker, Docker Compose |
| **Orchestration** | Kubernetes, Docker Swarm |
| **Cloud** | IaC, Serverless |
| **Data** | MLOps, Data Engineering |

---

## 📁 Project Structure

```
pydevops_lab/
├── 📄 README.md           # Project documentation
├── 📄 QWEN.md             # AI assistant context (this file)
├── 📄 pyproject.toml      # Poetry config & tool settings
├── 📄 poetry.lock         # Locked dependencies
├── 📄 .gitignore          # Git ignore rules
├── 📂 src/                # Source code
│   └── __init__.py
├── 🧪 tests/              # Test code
│   └── __init__.py
├── 🔧 scripts/            # Utility scripts
│   └── hello.py
├── ⚙️ config/             # Configuration files [TODO]
└── 📚 docs/               # Documentation [TODO]
```

---

## 📚 Learning Curriculum

### 1️⃣ Python Fundamentals
| # | Topic |
|---|-------|
| 1 | Python DevOps basics |
| 2 | File and filesystem automation |
| 3 | Command-line usage |

### 2️⃣ DevOps Technologies
| # | Topic |
|---|-------|
| 4 | Linux utilities |
| 5 | Package management |
| 6 | CI/CD (Continuous Integration/Deployment) |
| 7 | Monitoring and logging |
| 8 | pytest for DevOps |

### 3️⃣ Cloud Technologies
| # | Topic |
|---|-------|
| 9 | Cloud computing fundamentals |
| 10 | Infrastructure as Code (IaC) |
| 11 | Containerization: Docker & Docker Compose |
| 12 | Orchestration: Kubernetes & Docker Swarm |
| 13 | Serverless architectures |

### 4️⃣ Data Engineering
| # | Topic |
|---|-------|
| 14 | MLOps and ML engineering |
| 15 | Data engineering practices |

### 5️⃣ Case Studies
| # | Topic |
|---|-------|
| 16 | DevOps lessons learned and interviews |

---

## ⚙️ Building and Running

```bash
# Install dependencies
poetry install

# Run scripts
poetry run python scripts/hello.py
poetry run python scripts/hello.py --name DevOps

# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=src --cov-report=html

# Lint code
poetry run black .
poetry run ruff check .
poetry run mypy .

# Add new dependency
poetry add <package-name>

# Add dev dependency
poetry add --group dev <package-name>
```

---

## 📏 Development Conventions

### Code Style
- ✅ Follow **PEP 8** for Python code
- ✅ Use **type hints** where appropriate
- ✅ Write **docstrings** for public functions/classes

### Testing Practices
- ✅ Use **pytest** for all tests
- ✅ Place tests in `tests/` directory
- ✅ Name test files as `test_*.py`
- ✅ Aim for good test coverage

### Project Structure
| Directory | Purpose |
|-----------|---------|
| `src/` | Source code |
| `scripts/` | Utility scripts |
| `config/` | Configuration files |
| `docs/` | Documentation |

---

## 🚀 Next Steps

1. [ ] Create project directory structure
2. [ ] Initialize `requirements.txt` with dependencies
3. [ ] Set up basic project scaffolding
4. [ ] Start with Python fundamentals exercises
5. [ ] Progress through the learning topics sequentially

---

## 🤖 Notes for AI Assistant

| Guideline | Description |
|-----------|-------------|
| 🎓 **Educational Focus** | This is a learning project — prioritize educational value |
| 📖 **Follow Curriculum** | Adhere to the book's curriculum structure |
| 💡 **Clear Explanations** | Provide clear explanations for DevOps concepts |
| ✨ **Best Practices** | Include production-ready code patterns |
| 🧪 **Test Coverage** | When adding code, include tests to demonstrate pytest usage |

---

*Last updated: 2026-03-29*
