# Setup Troubleshooting Reference Guide

**Purpose**: Comprehensive solutions for common setup issues encountered in M1_02_environment_setup.ipynb

**Quick Navigation:**
- [Permission Denied Errors](#permission-denied)
- [Jupyter/IPython Kernel Errors](#kernel-errors)
- [SSL Certificate Errors](#ssl-errors)
- [Command not found: pip](#pip-not-found)
- [Getting Additional Help](#getting-help)
- [Troubleshooting Checklist](#checklist)

---

## Permission Denied Errors {#permission-denied}

**Problem**: Cannot install packages or create files

**On Mac/Linux** (needs administrator):
```bash
# ❌ DON'T USE sudo pip (installs to system, causes conflicts)
sudo pip install package

# ✅ USE virtual environment instead
python -m venv venv
source venv/bin/activate
pip install package
```

**On Windows** (needs administrator):
- Right-click Command Prompt → "Run as Administrator"
- Or use virtual environment (preferred)

---

## Jupyter/IPython Kernel Errors {#kernel-errors}

**Problem**: "Kernel died" or "Kernel not responding"

**Solutions**:
```bash
# Install/upgrade ipykernel
pip install --upgrade ipykernel

# Register kernel
python -m ipykernel install --user --name=venv

# In Jupyter, select: Kernel → Change Kernel → venv
```

**If kernel keeps dying**:
- Code has infinite loop → Add safeguards
- Memory error → Reduce dataset size
- Package conflict → Create fresh venv

---

## SSL Certificate Errors {#ssl-errors}

**Problem**: `SSL: CERTIFICATE_VERIFY_FAILED` when accessing APIs

**For APIs/web requests**:
```python
import requests
response = requests.get(url, verify=False)  # Disable SSL verification
# WARNING: Only for learning/development!
```

**For pip installations**:
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package_name
```

**Permanent fix** (Mac - common issue):
```bash
# Navigate to Python install folder
cd "/Applications/Python 3.11/"
# Run certificate installer
./Install Certificates.command
```

---

## "Command not found: pip" {#pip-not-found}

**Problem**: Terminal doesn't recognize `pip`

**Solutions**:
```bash
# Option 1: Use python -m pip instead
python -m pip install package_name
python3 -m pip install package_name  # If python points to Python 2

# Option 2: Ensure pip is installed
python -m ensurepip --upgrade

# Option 3: Check PATH (advanced)
echo $PATH  # Should include Python's scripts directory
```

---

## 🆘 Getting Additional Help {#getting-help}

**If you're still stuck after trying these solutions:**

1. **Check documentation**:
   - 🔧 [Setup Script Guide](../../docs/setup/setup_script_guide.md)
   - 📦 [Dependency Management](../../docs/setup/dependency_management.md)
   - 🐍 [Python Version Setup](../../docs/setup/python_version_setup.md)
   - 📊 [Installation Profiles](../../docs/setup/installation_profiles.md)

2. **Search your error message**:
   - Copy the exact error text
   - Search: `"your error message" python jupyter`
   - StackOverflow often has solutions

3. **Ask for help**:
   - GitHub Issues: [Create an issue](https://github.com/vinculum3141-ship-it/bike-availability-data-science-full/issues)
   - Include: Error message, what you tried, your OS and Python version

4. **Start fresh**:
   ```bash
   # Delete old venv and recreate
   rm -rf venv
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

---

## 📋 Troubleshooting Checklist {#checklist}

Before asking for help, verify you've tried:

- [ ] Checked error message carefully (what does it actually say?)
- [ ] Virtual environment is activated (`(venv)` in prompt?)
- [ ] Python version is 3.9+ (`python --version`)
- [ ] Packages are installed (`pip list` shows them)
- [ ] Restarted kernel after installation
- [ ] Verified file paths exist (`os.path.exists(...)`)
- [ ] Tried restarting terminal/Colab session
- [ ] Read relevant documentation guides
- [ ] Searched error message online

**Most issues are solved by**: Activating venv, restarting kernel, or reinstalling packages!
