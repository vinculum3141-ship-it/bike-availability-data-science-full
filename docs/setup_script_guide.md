# Setup Script for Quick Environment Setup

This script helps you quickly set up your Python environment for the course.

## Usage

```bash
# Make the script executable
chmod +x setup.sh

# Run the setup
./setup.sh
```

The script will:
1. Check your Python version
2. Create a virtual environment
3. Install all dependencies
4. Verify the installation
5. Generate sample data

## What it does

- Creates `.venv` directory for virtual environment
- Installs all required packages from `pyproject.toml`
- Runs verification tests
- Generates sample bike and weather data

## After Setup

To activate your environment in the future:

```bash
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

To deactivate:

```bash
deactivate
```
