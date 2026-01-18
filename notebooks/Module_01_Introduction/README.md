# Module 01: Introduction to the Project

## 📌 Module Overview
Introduction to the bike availability prediction project, setting up your environment, and understanding the problem domain. This module focuses on **orientation, confidence, and setup** — not modeling yet!

---

## 🎓 Course Development Strategy

### Pedagogical Approach
This course uses a **progressive scaffolding strategy** designed for fully online, self-paced learning:

**Scaffolding Levels by Module Type:**
- **Foundation Modules (M1)**: High scaffolding (90%) - Learn patterns through guided examples
- **Practice Modules (M2)**: Reduced scaffolding (30-40%) - Apply previous learning with hints only
- **New Concept Modules (M3-M10)**: Progressive scaffolding (70% → 30%) - Start guided, end independent

**Progressive Difficulty Within Each Notebook:**
- Part 1: Mostly complete (90%) - Learn the pattern
- Part 2: Guided practice (70%) - Practice with support
- Part 3: Moderate challenge (50%) - Balance guidance and independence
- Part 4: Independent work (30%) - Mostly on your own
- Part 5: Advanced/Optional (10%) - Minimal help, maximum learning

**Solution Notebooks:**
- All solutions are in separate `*_SOLUTIONS.ipynb` notebooks
- Encourages genuine attempts before looking
- Students choose their own learning path
- Available for support when needed

**Optional Challenges:**
- Each notebook includes advanced tasks for experienced learners
- Skip if building confidence, tackle to level up
- Not required for module completion

### For This Module (M1):
- **Scaffolding**: 90% complete code - focus on understanding concepts
- **Goal**: Build confidence, set context, establish patterns
- **Approach**: Run and observe → understand → prepare for Module 2 application
- **Solutions**: Inline (foundational module)

## 🎯 Learning Objectives
By the end of this module, you should be able to:
- ✔ Understand the bike-sharing business problem and smart cities context
- ✔ Understand the full project lifecycle (what you will build end-to-end)
- ✔ Set up your development environment (Google Colab or local)
- ✔ Know which open data sources will be used and why
- ✔ Successfully run notebooks and verify your setup
- ✔ Load and inspect a sample dataset with basic exploration
- ✔ Define the prediction problem clearly

## ✅ Your Tasks
Complete the following notebooks in this folder:

### M1_01_project_overview.ipynb
**Purpose**: Set context, motivate learners, explain what you'll build
**Time**: ~30-45 minutes (reading + reflection)
- Welcome & course overview
- Smart cities and bike-sharing context
- Why this project matters
- End-to-end workflow preview (all 10 modules)
- Portfolio outcomes
- **No code** - pure orientation

### M1_02_environment_setup.ipynb
**Purpose**: Remove all technical barriers and build confidence
**Time**: ~45-90 minutes (setup + verification)
- Google Colab setup (step-by-step)
- Local environment setup (alternative)
- Install required packages
- Test Python environment
- Verify library versions and imports
- **Minimal code** - just setup verification
- **Troubleshooting** - common issues and solutions

### M1_03_open_data_sources.ipynb
**Purpose**: Understand where data comes from and why open data matters
**Time**: ~30-45 minutes (reading + light coding)
- What is open data?
- Primary data sources (bike + weather APIs)
- Light API demo: fetch and peek at data
- Brief mention of enrichment sources (holidays, geography, etc.)
- Link to full data catalog
- **Light code** - builds confidence with APIs

### M1_04_sample_data_exploration.ipynb
**Purpose**: Build confidence with hands-on data exploration
**Time**: ~90-120 minutes (hands-on analysis)
- Load sample dataset (pre-downloaded CSV)
- Basic EDA: `.info()`, `.describe()`, `.head()`
- Simple time series visualization
- Define the prediction problem (features & target)
- Set project goals and success metrics
- **Hands-on code** - practical data science skills
- **Reflection exercises** - with example answers

**Total Module Time**: ~4-6 hours for thorough completion

## 📝 Naming Convention
Follow this pattern: `M1_{number}_{description}.ipynb`

Examples:
- `M1_01_project_overview.ipynb`
- `M1_02_environment_setup.ipynb`
- `M1_03_open_data_sources.ipynb`
- `M1_04_sample_data_exploration.ipynb`

## 💡 Tips
- Start with the [notebook template](../notebook_template.ipynb) for consistent structure
- Review the [example notebook](../example_data_exploration.ipynb) for best practices
- Use markdown cells to explain your thinking process
- Include code comments for clarity
- Save your work frequently
- Follow the [coding standards](../../docs/standards/coding_standards.md)
- Don't worry about perfection - focus on learning!
- Run each notebook cell-by-cell to understand the flow

## 📚 Resources
- 📓 [Notebook Template](../notebook_template.ipynb) - Copy this to start
- 🎓 [Example Notebook](../example_data_exploration.ipynb) - See best practices
- 📐 [Coding Standards](../../docs/standards/coding_standards.md) - Write clean code
- 📚 [Code Snippets](../../docs/standards/code_snippets.md) - Quick reference
- 🔧 [Google Colab Setup](../../docs/setup/setup_google_colab.md) - Cloud setup
- 🌐 [Open Data Sources](../../docs/reference/open_data_sources.md) - Full data catalog
- 📦 [Dependency Management](../../docs/setup/dependency_management.md) - Environment setup

## 📚 Additional Learning Resources
Module 01 introduces key concepts with links to comprehensive documentation:
- 🧠 [Data Science Thinking Framework](../../docs/guides/DATA_SCIENCE_THINKING_FRAMEWORK.md) - Strategic DS workflow
- 🤖 [ML Model Types Reference](../../docs/guides/ML_MODEL_TYPES_REFERENCE.md) - Model selection guide
- 🎯 [Target Variable Selection Guide](../../docs/guides/TARGET_VARIABLE_SELECTION_GUIDE.md) - Problem definition
- 🐼 [Pandas Quick Reference](../../docs/guides/PANDAS_QUICK_REFERENCE.md) - DataFrame operations

## ✨ Definition of Done (Checkpoint)
Before moving to Module 02, ensure:
- [ ] ✅ You can open the repo in Google Colab (or run locally)
- [ ] ✅ All Module 01 notebooks run without errors
- [ ] ✅ You understand the bike-sharing problem and business context
- [ ] ✅ You know the primary data sources (bikes + weather)
- [ ] ✅ You can load sample data and perform basic EDA
- [ ] ✅ You can clearly define the prediction problem
- [ ] ✅ Your environment is set up and verified
- [ ] ✅ You understand the full learning journey (10 modules)

**Key Outcome**: Confidence and clarity — you know what you're building and why!

### 📝 Self-Evaluation
Complete the [Module 01 Self-Evaluation](MODULE_01_SELF_EVALUATION.md) to:
- ✅ Verify you've achieved all learning objectives
- 🔍 Identify areas that need more review
- 💪 Build confidence before moving to Module 02
- 📝 Reflect on your learning journey

**This is especially important for remote/online learners!**

---
**Next Module:** [Module 02 - Data Acquisition](../Module_02_Data_Acquisition/) - Fetching real-world data from APIs
