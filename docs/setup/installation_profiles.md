# Installation Options Comparison

> **⚡ Quick Decision Tree**: [Jump to "Which Should You Use?"](#-which-should-you-use)

This document explains the different ways to install dependencies and what each includes.

---

## 🧭 Quick Start: Choose Your Path

```
START: What are you doing?
│
├─ 📚 Taking the course / Learning data science
│  └─ ✅ USE: Student Profile
│     │
│     ├─ No installation? → Use Google Colab (easiest!)
│     ├─ Want automation? → Run ./setup.sh (choose option 1)
│     └─ Manual control? → pip install -e .
│
├─ 🛠️ Contributing to course / Developing content
│  └─ ✅ USE: Developer Profile
│     └─ Run: pip install -e ".[dev]"
│
└─ 🚀 Want everything + JupyterLab IDE
   └─ ✅ USE: Full Profile
      └─ Run: pip install -e ".[all]"
```

**👉 Most users should use Student Profile** - it has everything needed for learning!

---

## 📦 Three Installation Profiles

### 1. **Student/Learner** (Default - Recommended for Course)

**What you get:**
- ✅ All core data science packages
- ✅ Everything needed for notebooks
- ✅ Basic code quality tools (black, pylint, flake8)
- ✅ Dashboard tools (streamlit)

**What you DON'T get:**
- ❌ Testing frameworks (pytest)
- ❌ Documentation generators (sphinx)
- ❌ Advanced profiling tools
- ❌ JupyterLab (basic Jupyter works in notebooks)

**Install:**
```bash
pip install -e .
```

**Use case:** You're taking the course, working through notebooks, learning data science.

---

### 2. **Developer** (For Course Development & Maintenance)

**What you get:**
- ✅ Everything from Student profile
- ✅ **Testing:** pytest, pytest-cov, pytest-mock
- ✅ **Documentation:** sphinx, sphinx-rtd-theme, myst-parser
- ✅ **Extra linting:** pydocstyle, bandit, isort
- ✅ **Notebook tools:** nbqa, nbconvert
- ✅ **Profiling:** memory-profiler, line-profiler

**Install:**
```bash
pip install -e ".[dev]"
```

**Use case:** You're developing course content, writing tests, maintaining the repository, or want to contribute.

---

### 3. **Full** (Everything)

**What you get:**
- ✅ Everything from Developer profile
- ✅ **JupyterLab:** Full IDE experience
- ✅ **Jupyter extensions:** Enhanced notebook features
- ✅ All possible tools

**Install:**
```bash
pip install -e ".[all]"
```

**Use case:** You want the complete development environment with all bells and whistles.

---

## 📊 Package Count Comparison

| Profile | Core Packages | Dev Tools | Jupyter Tools | Total Approx. |
|---------|---------------|-----------|---------------|---------------|
| Student | 18 | 0 | 0 | ~18 packages |
| Developer | 18 | 15+ | 0 | ~33 packages |
| Full | 18 | 15+ | 5+ | ~38 packages |

---

## 🎯 Installation Methods Comparison

### Method 1: Using pyproject.toml (Modern - Recommended)

```bash
# Student
pip install -e .

# Developer
pip install -e ".[dev]"

# Full
pip install -e ".[all]"
```

**Pros:**
- ✅ Clean, standardized
- ✅ Automatic entry points (`generate-sample-data` command)
- ✅ Tool configs included
- ✅ Easy to choose profile

**Cons:**
- Requires understanding of extras syntax

---

### Method 2: Using requirements files (Traditional)

```bash
# Student
pip install -r requirements.txt

# Developer
pip install -r requirements-dev.txt
```

**Note:** `requirements-dev.txt` includes base via `-r requirements.txt`

**Pros:**
- ✅ Familiar to most users
- ✅ Simple syntax
- ✅ Works everywhere

**Cons:**
- ❌ Two files to maintain
- ❌ No tool configuration
- ❌ No entry points
- ❌ Only 2 profiles (not 3)

---

### Method 3: Using setup.sh (Automated)

```bash
./setup.sh
```

**Interactive menu offers all three profiles!**

**Pros:**
- ✅ Most beginner-friendly
- ✅ Checks Python version
- ✅ Creates venv automatically
- ✅ Verifies installation
- ✅ Generates sample data

**Cons:**
- Only for bash/Linux/macOS (Windows users need WSL or manual setup)

---

## 🤔 Which Should You Use?

### 🎓 For Students/Learners (Recommended)

**👉 You're taking this course and want to learn data science**

**Best options (pick ONE):**

1. **🌐 Google Colab** (No installation at all!)
   - Open notebooks directly in browser
   - See [Google Colab Setup Guide](setup_google_colab.md)
   - ✅ Fastest way to start learning

2. **🚀 Automated Script** (Easiest local setup)
   ```bash
   ./setup.sh  # Choose option 1 (Student Profile)
   ```
   - Handles everything automatically
   - See [Setup Script Guide](setup_script_guide.md)

3. **🎯 Modern Install** (Manual but clean)
   ```bash
   pip install -e .
   ```
   - Uses modern Python standards
   - Gives you `generate-sample-data` command

4. **📜 Traditional Install** (If preferred)
   ```bash
   pip install -r requirements.txt
   ```
   - Classic requirements file approach

**What you get:** ~18 core packages for data science learning

---

### 👨‍💻 For Course Developers/Contributors

**👉 You're developing course content or contributing code**

```bash
# Recommended
pip install -e ".[dev]"

# OR traditional
pip install -r requirements-dev.txt
```

**What you get:** Student packages + testing (pytest) + docs (sphinx) + profiling tools

---

### 🚀 For Maximum Features (Power Users)

**👉 You want JupyterLab and all possible tools**

```bash
pip install -e ".[all]"
```

---

## 📝 What's in Each Requirements File?

### requirements.txt (Core)
```
pandas, numpy, scipy
scikit-learn, xgboost, shap
matplotlib, seaborn, plotly
requests
ydata-profiling
mlflow
papermill, ipywidgets
streamlit
black, pylint, flake8, mypy
python-dotenv, python-dateutil, tqdm
```

### requirements-dev.txt (Includes requirements.txt + Development Tools)
```
-r requirements.txt  # ← Includes everything above
pytest, pytest-cov, pytest-mock
sphinx, sphinx-rtd-theme, myst-parser
pydocstyle, bandit, isort
jupyterlab, jupyter-contrib-nbextensions
nbqa, nbconvert
memory-profiler, line-profiler
```

---

## 🔄 Switching Between Profiles

You can upgrade your installation at any time:

```bash
# Started with student, want dev tools now?
pip install -e ".[dev]"

# Want everything?
pip install -e ".[all]"

# Go back to minimal?
pip uninstall [package-names]
# OR recreate venv
rm -rf .venv
python3.9 -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## 💡 Recommendations by Role

| Your Role | Recommended Profile | Why |
|-----------|-------------------|-----|
| **Student** | Student | Focus on learning, not tooling |
| **Teaching Assistant** | Developer | Help students, review code |
| **Course Author** | Full | Create content, test everything |
| **Contributor** | Developer | Write tests, improve code |
| **Curious Learner** | Full | Explore all capabilities |

---

## ✅ Verification

After installation, verify what you have:

```bash
# Check installed packages
pip list

# Check if dev tools are available
pytest --version      # Should work if dev/all installed
sphinx-build --version  # Should work if dev/all installed
jupyter lab --version   # Should work if all installed

# Check entry points
generate-sample-data --help  # Should work with pyproject.toml install
```

---

## 🆘 Troubleshooting

### "I installed 'student' but want dev tools"
```bash
pip install -e ".[dev]"
```

### "Too many packages, slow installation"
Stick with student profile! It's all you need for the course.

### "I want JupyterLab but not all dev tools"
```bash
pip install -e .
pip install jupyterlab
```

### "requirements-dev.txt vs pyproject.toml [dev]?"
They're almost identical! Use whichever syntax you prefer:
- `pip install -r requirements-dev.txt` (traditional)
- `pip install -e ".[dev]"` (modern)

---

## 📚 Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [pyproject.toml specification](https://peps.python.org/pep-0621/)
- [Dependency Management Guide](dependency_management.md)
- [Python Version Setup](python_version_setup.md)

---

**Bottom line:** If you're learning, use **Student** profile. If you're developing, use **Developer** profile. Simple! 🎯
