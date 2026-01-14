# Changelog

All notable changes to the Bike Availability Data Science Course will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

> **Note**: Repository cleanup and Module 02 preparation  
> **Date**: 2026-01-14

### Added
- **Module 02 README** - Development planning notes
  - Added implementation topics and API integration patterns
  - Added estimated structure (4-5 notebooks)
  - Added error handling and data storage conventions

### Changed
- **.gitignore** - Now ignores `.vscode/` directory
  - Prevents editor-specific settings from being committed

### Removed
- **MODULE_01_SUMMARY.md** - Removed temporary summary document
  - Information integrated into CHANGELOG and Module 02 README

---

## [0.2.1] - 2026-01-14 (Documentation & Changelog)

### Added
- **CHANGELOG.md** - Comprehensive version history tracking
  - Documents all versions from v0.0.1 to v0.2.0
  - Tracks all 15 commits for Module 01 development
  - Includes detailed timeline and commit references

---

## [0.2.0] - 2026-01-14 (Module 01 Refinements & Fixes)

### Fixed
- **M1_04_sample_data_exploration.ipynb** - Fixed seaborn deprecation warning (commit bc1d95b)
  - Changed `seaborn-v0_8-darkgrid` style reference to current version
- **M1_04_sample_data_exploration.ipynb** - Fixed root path issues (commit d920251)
  - Corrected file path handling for data loading
  - Ensured compatibility with both Colab and local environments
- **M1_01_project_overview.ipynb** - Fixed Colab button reference (commit a5486c6)

### Changed
- **M1_03_open_data_sources.ipynb** - Enhanced open data explanations (commit 17af28e)
  - Expanded coverage of open data concepts
  - Added more detailed API exploration examples
- **notebooks/Module_01_Introduction/README.md** - Aligned with read-not-do approach (commit 01896a8)

### Added
- **M1_R1_fetching_bike_data.ipynb** - Tutor resource notebook (commit a638887)
  - Amsterdam-specific bike data fetching examples
  - Demonstrates filtering networks by country (Netherlands)
  - Shows real OV-fiets API usage
  - Additional resource for instructors and advanced learners
- **Capstone project** - Added self evaluation guide (commit 0d1fbf7)

---

## [0.1.0] - 2025-12-30 (Module 01 Complete - Initial Implementation)

### Added
- **Module 01: Introduction** (4 core notebooks + 1 resource) ✅
  - M1_01_project_overview.ipynb - Project context and learning journey (commit 01896a8)
  - M1_02_environment_setup.ipynb - Environment setup with profile comparison (commit d5cd9c8)
  - M1_03_open_data_sources.ipynb - Open data concepts and API demos (commit 610105b)
  - M1_04_sample_data_exploration.ipynb - Complete EDA with visualizations (commit fe81552)
  - Updated Module 01 README with 4-notebook structure (commit fe81552)
- Modern project configuration (`pyproject.toml`) - commit a2e5b0d
  - Python 3.9-3.12 support specification
  - Three installation profiles: student, developer, full
  - Tool configurations (black, pylint, mypy, pytest)
  - Entry points for CLI commands
- Interactive setup script (`setup.sh`) - commit a2e5b0d
  - Automatic Python version detection
  - Virtual environment creation
  - Profile-based installation (student/developer/full)
  - Installation verification
  - Sample data generation
- Sample data generator (`src/generate_sample_data.py`) - commit f79ce87
  - CLI interface with argparse
  - Configurable stations, days, date ranges
  - Realistic bike availability patterns (commuter, tourist, leisure)
  - Weather effects and temporal patterns
  - Reproducible with random seed
- Sample dataset (`data/raw/sample_bike_weather.csv`) - commit f79ce87
  - 81 rows of synthetic data (80 data + 1 header)
  - 2 stations (Centraal Station, Museumplein), 2-3 days coverage
  - Combined bike and weather features
- Documentation - commits 2cc7c0b, 0e45f4c, 88deae7
  - `docs/python_version_setup.md` - Python version requirements and setup guide
  - `docs/installation_profiles.md` - Detailed comparison of installation options with decision tree
  - `docs/setup_script_guide.md` - Setup script documentation
  - `docs/LEARNER_EXPERIENCE_IMPROVEMENTS.md` - Design decisions for learner UX improvements
  - Enhanced README.md with learner-focused Quick Start

### Changed
- Updated `notebooks/Module_01_Introduction/README.md` - commit fe81552
  - Expanded from 3 to 4 notebooks structure
  - Added detailed learning objectives
  - Included "Definition of Done" checklist
  - Enhanced tips and resources sections

---

## [0.0.1] - 2024-01-XX (Initial Repository Structure)

### Added
- Initial repository structure
  - `notebooks/` directory with 10 module placeholders
  - `src/` directory for reusable Python code
  - `data/` directory structure (raw/processed)
  - `docs/` directory for documentation
  - `apps/` for Streamlit dashboard
  - `pipelines/` for automation
  - `capstone/` for final project
- Core documentation
  - README.md with project overview
  - CONTRIBUTING.md with guidelines
  - LICENSE (MIT)
- Requirements files
  - `requirements.txt` - Core dependencies
  - `requirements-dev.txt` - Development dependencies
- Documentation guides
  - `docs/coding_standards.md` - PEP 8 and best practices
  - `docs/code_snippets.md` - Quick reference examples
  - `docs/dependency_management.md` - Package management
  - `docs/experiment_best_practices.md` - MLflow tracking
  - `docs/model_documentation_guidelines.md` - Model docs
  - `docs/open_data_sources.md` - Data source catalog
  - `docs/reporting_template.md` - Report structure
  - `docs/setup_google_colab.md` - Colab setup guide
  - `docs/README_NAVIGATION.md` - Documentation navigation guide
- Template notebooks
  - `notebooks/notebook_template.ipynb` - Standard structure
  - `notebooks/example_data_exploration.ipynb` - Best practices example
- Module structure
  - 10 module directories created
  - README files for each module with placeholders
- Configuration
  - `.python-version` file (3.9)
  - `.gitignore` for Python projects

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| Unreleased | 2026-01-14 | Documentation tracking files |
| 0.2.0 | 2026-01-14 | Module 01 refinements and fixes |
| 0.1.0 | 2025-12-30 | Module 01 complete with modern project config |
| 0.0.1 | 2024-XX-XX | Initial repository structure |

---

## Release Notes Format

Each release includes:

### Added
- New features, modules, notebooks, or documentation

### Changed
- Changes to existing functionality or content

### Deprecated
- Features or content that will be removed in future versions

### Removed
- Features or content removed in this version

### Fixed
- Bug fixes or corrections

### Security
- Security-related changes or fixes

---

## Module Development Progress

| Module | Status | Notebooks | Current Version |
|--------|--------|-----------|-----------------|
| Module 01: Introduction | ✅ Complete | 5/5 (4 core + 1 resource) | 0.2.0 |
| Module 02: Data Acquisition | 🚧 Planning | 0/? | - |
| Module 03: Exploration | 📋 Planned | 0/? | - |
| Module 04: Feature Engineering | 📋 Planned | 0/? | - |
| Module 05: Modeling | 📋 Planned | 0/? | - |
| Module 06: Validation | 📋 Planned | 0/? | - |
| Module 07: Visualization | 📋 Planned | 0/? | - |
| Module 08: Automation | 📋 Planned | 0/? | - |
| Module 09: Experimentation | 📋 Planned | 0/? | - |
| Module 10: Collaboration | 📋 Planned | 0/? | - |
| Capstone Project | 🚧 Templates | Self-eval guide added | - |

**Legend:**
- ✅ Complete - All notebooks finished and tested
- 🚧 In Progress - Actively being developed
- 📋 Planned - Not yet started

---

## Contributing to the Changelog

When making changes:

1. Add your changes under `[Unreleased]` section
2. Use appropriate category (Added, Changed, Fixed, etc.)
3. Be specific and concise
4. Reference issue numbers if applicable
5. Group related changes together

Example:
```markdown
### Added
- Module 02: Data Acquisition
  - M2_01_amsterdam_api.ipynb - Fetch bike data from Amsterdam API
  - M2_02_weather_api.ipynb - Fetch weather data from Open-Meteo
```

---

## Semantic Versioning

This project uses semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR** (1.0.0): Complete course with all 10 modules + capstone
- **MINOR** (0.X.0): Complete module or significant feature addition
- **PATCH** (0.0.X): Bug fixes, minor documentation updates, typos

Current: **Unreleased** → Will become **0.2.0** when Module 01 is released

---

## Useful Links

- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Repository Issues](https://github.com/vinculum3141-ship-it/bike-availability-data-science-full/issues)
- [Contributing Guidelines](CONTRIBUTING.md)
