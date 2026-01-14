# 📚 Documentation

Welcome to the Bike Availability Data Science Course documentation! This folder contains all supporting materials organized by purpose.

---

## 🗂️ Folder Structure

### 🔧 [`setup/`](setup/) - Getting Started & Environment Setup

**For:** First-time users setting up their environment

| Document | Description |
|----------|-------------|
| [Google Colab Setup](setup/setup_google_colab.md) | Cloud-based setup (no installation required) |
| [Setup Script Guide](setup/setup_script_guide.md) | Automated local setup using `setup.sh` |
| [Installation Profiles](setup/installation_profiles.md) | Manual installation options (student/developer/full) |
| [Python Version Setup](setup/python_version_setup.md) | Python version requirements and troubleshooting |
| [Dependency Management](setup/dependency_management.md) | Managing packages and virtual environments |

**Start here if:** You're new to the course and need to set up your environment.

---

### 📖 [`guides/`](guides/) - Learning Resources & Core Concepts

**For:** Students learning data science concepts referenced from notebooks

| Document | Description | Module |
|----------|-------------|--------|
| [Data Science Thinking Framework](guides/DATA_SCIENCE_THINKING_FRAMEWORK.md) | Strategic DS workflow and decision-making | Module 01 |
| [ML Model Types Reference](guides/ML_MODEL_TYPES_REFERENCE.md) | Comprehensive model selection guide | Module 01 |
| [Target Variable Selection Guide](guides/TARGET_VARIABLE_SELECTION_GUIDE.md) | How to define your prediction problem | Module 01 |
| [Pandas Quick Reference](guides/PANDAS_QUICK_REFERENCE.md) | DataFrame operations cheat sheet | Module 01 |

**Use these when:** Notebooks link to them for deeper conceptual understanding.

---

### ⚙️ [`standards/`](standards/) - Development Best Practices

**For:** Developers writing code and maintaining quality

| Document | Description |
|----------|-------------|
| [Coding Standards](standards/coding_standards.md) | Python style guide and best practices |
| [Code Snippets](standards/code_snippets.md) | Reusable code patterns and templates |
| [Experiment Best Practices](standards/experiment_best_practices.md) | ML experiment tracking and versioning |
| [Model Documentation Guidelines](standards/model_documentation_guidelines.md) | How to document ML models |
| [Reporting Template](standards/reporting_template.md) | Standard format for analysis reports |

**Use these when:** Writing code, running experiments, or documenting work.

---

### 📋 [`reference/`](reference/) - Project Reference & Meta

**For:** Understanding data sources and navigating the repository

| Document | Description |
|----------|-------------|
| [Open Data Sources](reference/open_data_sources.md) | Catalog of bike and weather data APIs |
| [README Navigation](reference/README_NAVIGATION.md) | Map of all READMEs in the repository |
| [Learner Experience Improvements](reference/LEARNER_EXPERIENCE_IMPROVEMENTS.md) | Course design decisions and rationale |

**Use these when:** Looking for data sources or understanding repository structure.

---

## 🧭 Quick Navigation

**I want to...**

| Goal | Go to |
|------|-------|
| Set up my environment for the first time | [`setup/`](setup/) → Start with [Google Colab](setup/setup_google_colab.md) or [Local Setup](setup/setup_script_guide.md) |
| Understand data science concepts | [`guides/`](guides/) → See [DS Thinking Framework](guides/DATA_SCIENCE_THINKING_FRAMEWORK.md) |
| Learn about ML models | [`guides/`](guides/) → See [ML Model Types](guides/ML_MODEL_TYPES_REFERENCE.md) |
| Write better code | [`standards/`](standards/) → See [Coding Standards](standards/coding_standards.md) |
| Find data sources | [`reference/`](reference/) → See [Open Data Sources](reference/open_data_sources.md) |
| Navigate the repo | [`reference/`](reference/) → See [README Navigation](reference/README_NAVIGATION.md) |

---

## 📚 How Documentation is Used

### In Notebooks
Notebooks contain **concise, actionable guidance** and link to comprehensive docs when deeper understanding is needed:

```markdown
### Quick Reference
- Feature X does Y
- Use when Z

**For comprehensive guide:** See [Guide Name](../../docs/guides/GUIDE_NAME.md)
```

### In Module READMEs
Module READMEs list relevant documentation for that module's topics.

### Standalone Use
All docs are self-contained and can be read independently.

---

## 🔄 Maintenance

**Adding new documentation:**
1. Choose the appropriate folder based on purpose
2. Follow existing naming conventions (lowercase with underscores)
3. Update this README with a link and description
4. Reference from relevant notebooks/READMEs

**File naming:**
- Use descriptive names: `concept_name.md` not `doc1.md`
- Keep lowercase with underscores
- Be specific: `ml_model_types_reference.md` not `models.md`

---

## 🤝 Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines and documentation standards.

---

**Need help?** Check [README Navigation](reference/README_NAVIGATION.md) for a complete map of all documentation in the repository.
