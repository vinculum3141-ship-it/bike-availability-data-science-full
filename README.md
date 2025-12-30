# 🚴 Bike Availability – End-to-End Data Science Project

This repository is a **project-based learning template** covering the full data science lifecycle:

- Data acquisition & integration
- Exploration & feature engineering
- Modeling & validation
- Visualization & automation
- Experimentation & collaboration

All tools are **open source** and runnable **free of charge** using Google Colab.

---

## ⚡ Quick Start

**New to the project?** Follow these steps:

### 🎓 For Students/Learners (Recommended Path)

1. **🔧 Setup Environment FIRST** - Choose ONE option:
   - **Option A (Easiest)**: Use [Google Colab](docs/setup_google_colab.md) - No installation needed! ✨
   - **Option B (Local)**: Run `./setup.sh` and select "Student profile" - Automated setup 🚀
   - **Option C (Manual)**: See [Installation Guide](docs/installation_profiles.md) for details

2. **📖 Start Learning**: Open [Module 01 README](notebooks/Module_01_Introduction/README.md) and follow the notebooks

3. **📓 Use Templates**: [Notebook Template](notebooks/notebook_template.ipynb) for your own notebooks

4. **👀 Learn Best Practices**: [Example Notebook](notebooks/example_data_exploration.ipynb)

### 👨‍💻 For Developers/Contributors

- **Full setup guide**: [Installation Profiles](docs/installation_profiles.md) - Choose developer or full profile
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md) - Code standards and workflow
- **Code Quality**: [Coding Standards](docs/coding_standards.md) - Professional Python code

**Need help?** Check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines and support.

---

## 🎯 Learning Objectives

By completing this project, you will learn how to:

- Work with real-world open data
- Build reproducible data science pipelines
- Train and validate machine learning models
- Communicate insights with dashboards
- Apply industry-aligned best practices

---

## 🚀 Getting Started (Recommended)

> **💡 First time here?** See [Installation Profiles Guide](docs/installation_profiles.md) to understand your options, or just pick one below!

### Option 1: Google Colab (No Setup Required) ⭐ **Recommended for Beginners**
1. Fork or clone this repository
2. Open any notebook in `notebooks/`
3. Click **Open in Colab**
4. Run the setup cell in each notebook

See [Google Colab Setup Guide](docs/setup_google_colab.md) for detailed instructions.

### Option 2: Local Setup with Script (Automated) ⭐ **Best for Local Development**

**Requirements**: Python 3.9 or higher, bash shell

```bash
# Clone the repository
git clone https://github.com/[username]/bike-availability-data-science.git
cd bike-availability-data-science

# Run the interactive setup script
./setup.sh
```

The script will:
- ✅ Check Python version
- ✅ Create virtual environment
- ✅ Let you choose your profile (student/developer/full)
- ✅ Install packages
- ✅ Generate sample data

See [Setup Script Guide](docs/setup_script_guide.md) for details.

### Option 3: Manual Local Setup

**Requirements**: Python 3.9 or higher

```bash
# Clone the repository
git clone https://github.com/[username]/bike-availability-data-science.git
cd bike-availability-data-science

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Choose your installation profile:

# For students/learners (recommended for course)
pip install -e .

# For developers (includes testing, docs tools)
pip install -e ".[dev]"

# For full environment (includes JupyterLab)
pip install -e ".[all]"

# Or use traditional requirements files:
pip install -r requirements.txt        # Student profile
pip install -r requirements-dev.txt   # Developer profile
```

**What's the difference?** See [Installation Profiles Guide](docs/installation_profiles.md) for a detailed comparison.

See [Dependency Management Guide](docs/dependency_management.md) for more details.

## 📂 Repository Structure
- `notebooks/` – Step-by-step course notebooks (see module READMEs for guidance)
- `src/` – Reusable Python modules (templates with TODO docstrings)
- `data/` – Raw and processed datasets (with organization guides)
- `apps/` – Interactive dashboards
- `pipelines/` – Automation scripts
- `capstone/` – Final project with guidelines and rubric
- `docs/` – Documentation, best practices, and guides

## 📚 Learning Resources

This template includes comprehensive guides to help you succeed:

### Getting Started
- 📘 [Google Colab Setup](docs/setup_google_colab.md) - Run notebooks in the cloud
- 📦 [Dependency Management](docs/dependency_management.md) - Install and manage packages
- 🤝 [Contributing Guidelines](CONTRIBUTING.md) - Code standards and workflow

### Coding & Best Practices  
- 📐 [Coding Standards](docs/coding_standards.md) - Write clean, professional Python code
- 📚 [Code Snippets](docs/code_snippets.md) - Quick reference for common tasks
- 📓 [Notebook Template](notebooks/notebook_template.ipynb) - Start your notebooks right
- 🎓 [Example Notebook](notebooks/example_data_exploration.ipynb) - See best practices in action

### Data & Modeling
- 🌐 [Open Data Sources](docs/open_data_sources.md) - Where to find bike and weather data
- � [Experiment Best Practices](docs/experiment_best_practices.md) - Track ML experiments
- 📋 [Model Documentation](docs/model_documentation_guidelines.md) - Document your models
- 📊 [Reporting Template](docs/reporting_template.md) - Present your findings

## �🧠 Capstone Project
The `capstone/` folder contains a full end-to-end assignment that you can
use as a portfolio project.

- [Capstone Guidelines](capstone/capstone_guidelines.md) - Project requirements and timeline
- [Grading Rubric](capstone/grading_rubric.md) - Assessment criteria

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
