# 🐍 Python Project Template with GitHub Actions

<div align="center">

**A minimal Python project template with automated testing, linting, and CI/CD pipeline**

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)](https://python.org)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Flake8](https://img.shields.io/badge/Flake8-4B32C3?logo=python&logoColor=white)](https://flake8.pycqa.org/)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)

</div>

## 📖 Overview

This repository serves as a learning template for contributing to open-source projects using the **fork and pull request** workflow. It includes a simple Python project with:

- ✅ Sample functions with docstrings
- ✅ Unit tests using **pytest**
- ✅ Code linting with **flake8**
- ✅ Automated CI/CD pipeline with **GitHub Actions**

The main branch contains a bug that needs to be fixed, providing hands-on experience with the contribution workflow.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10** or higher
- **Git** installed on your system
- A **GitHub account**

### Installation

1. **Fork this repository** (click the "Fork" button in the top-right corner)

2. **Clone your fork** locally:
```bash
git clone https://github.com/YOUR-USERNAME/git-task.git
cd git-task
```

1. **Create a virtual environment** (recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

1. **Install dependencies**:

```
pip install flake8 pytest
```

## 🧪 Testing & Linting

### Run Tests with Pytest

```
pytest testing.py
```

### Run Linting with Flake8

```
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## 📂 Project Structure

```
git-task/
├── .github/
│   └── workflows/
│       └── python-app.yml     # CI/CD pipeline configuration
├── main.py                    # Main Python module with sample functions
├── testing.py                 # Unit tests for main.py
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore rules
```

## 🔧 How to Contribute (Fix the Bug)

The `main.py` file currently has a bug that causes tests to fail. Follow these steps to fix it:

### Step 1: Create a Branch

```
git checkout -b fix-add-function
```

### Step 2: Fix the Bug

Open `main.py` and locate the `add()` function. The current implementation has an error:

```
def add(number_a:int, number_b:int):
    return number_a  + number_b  # ← Incorrect spacing/operator? (hint: check the tests)
```

Review `testing.py` to understand what the expected behavior is, then fix the function.

### Step 3: Stage and Commit Your Changes

```
git add main.py
git commit -m "Fix: Correct add function to pass all tests"
```

### Step 4: Push Your Changes

```
git push origin fix-add-function
```

### Step 5: Open a Pull Request

1. Go to your fork on GitHub
1. Click **"Contribute"** → **"Open Pull Request"**
1. Add a clear title and description explaining your fix
1. Click **"Create Pull Request"**

### Step 6: Wait for CI Checks

The GitHub Actions workflow will automatically:

- Run `flake8` linting
- Execute `pytest` tests

If all checks pass, your PR is ready for review!

## 🤖 GitHub Actions CI/CD Pipeline

The included workflow (`.github/workflows/python-app.yml`) automatically:

1. **Triggers** on `push` and `pull_request` to the `main` branch
1. **Sets up** Python 3.10
1. **Installs** dependencies (flake8, pytest)
1. **Lints** code with flake8
1. **Runs** tests with pytest

### Workflow Configuration

```
name: Python application
on:
  push: { branches: [ "main" ] }
  pull_request: { branches: [ "main" ] }
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with: { python-version: "3.10" }
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest
      - name: Lint with flake8
        run: flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
      - name: Test with pytest
        run: pytest testing.py
```

## 📚 Learning Resources

- [Contributing to a Project (GitHub Docs)](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
- [Fork a Repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Pytest Documentation](https://docs.pytest.org/)
- [Flake8 Documentation](https://flake8.pycqa.org/)

## 🎯 Key Takeaways

By completing this task, you'll learn:

1. **Forking** a repository to create your own copy
1. **Cloning** your fork to work locally
1. **Creating branches** for isolated development
1. **Making commits** with meaningful messages
1. **Pushing changes** to your remote fork
1. **Opening pull requests** to propose changes
1. **Understanding CI/CD** through GitHub Actions

## 🤝 Contributing

This is a learning exercise, but if you have suggestions for improvement:

1. Fork the repository
1. Create your feature branch (`git checkout -b feature/improvement`)
1. Commit your changes (`git commit -m 'Add improvement'`)
1. Push to the branch (`git push origin feature/improvement`)
1. Open a Pull Request

## 📄 License

This project is licensed under the **MIT License** - feel free to use it for learning purposes.

## 📬 Support

If you get stuck:

- Review the [GitHub Docs on Contributing](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
- Check the **Issues** tab for common problems
- Open a new issue if you need help
<div align="center">
**Happy Contributing!** 🚀✨
</div>

