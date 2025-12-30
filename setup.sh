#!/bin/bash

# ═══════════════════════════════════════════════════════════
# Bike Availability Data Science - Environment Setup Script
# ═══════════════════════════════════════════════════════════
#
# This script sets up the Python environment for the course.
# It will:
#   1. Check Python version (requires 3.9+)
#   2. Create virtual environment
#   3. Install dependencies
#   4. Verify installation
#   5. Generate sample data
#
# Usage:
#   chmod +x setup.sh
#   ./setup.sh
#
# ═══════════════════════════════════════════════════════════

set -e  # Exit on error

echo "════════════════════════════════════════════════════════════"
echo "🚴 Bike Availability Data Science - Environment Setup"
echo "════════════════════════════════════════════════════════════"
echo ""

# ─────────────────────────────────────────────────────────────
# 1. Check Python version
# ─────────────────────────────────────────────────────────────

echo "📋 Step 1: Checking Python version..."

# Try different Python commands
if command -v python3.9 &> /dev/null; then
    PYTHON_CMD="python3.9"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Error: Python not found!"
    echo "   Please install Python 3.9 or higher."
    exit 1
fi

# Check version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

echo "   Found: Python $PYTHON_VERSION"

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 9 ]); then
    echo "❌ Error: Python 3.9 or higher is required!"
    echo "   Current version: $PYTHON_VERSION"
    echo "   Please upgrade your Python installation."
    exit 1
fi

echo "✅ Python version check passed!"
echo ""

# ─────────────────────────────────────────────────────────────
# 2. Create virtual environment
# ─────────────────────────────────────────────────────────────

echo "📋 Step 2: Creating virtual environment..."

if [ -d ".venv" ]; then
    echo "⚠️  Virtual environment already exists."
    read -p "   Do you want to recreate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "   Removing existing .venv..."
        rm -rf .venv
    else
        echo "   Using existing .venv"
    fi
fi

if [ ! -d ".venv" ]; then
    echo "   Creating .venv with $PYTHON_CMD..."
    $PYTHON_CMD -m venv .venv
    echo "✅ Virtual environment created!"
else
    echo "✅ Using existing virtual environment!"
fi

echo ""

# ─────────────────────────────────────────────────────────────
# 3. Activate virtual environment
# ─────────────────────────────────────────────────────────────

echo "📋 Step 3: Activating virtual environment..."

source .venv/bin/activate

echo "✅ Virtual environment activated!"
echo ""

# ─────────────────────────────────────────────────────────────
# 4. Upgrade pip
# ─────────────────────────────────────────────────────────────

echo "📋 Step 4: Upgrading pip..."

python -m pip install --upgrade pip setuptools wheel --quiet

echo "✅ pip upgraded!"
echo ""

# ─────────────────────────────────────────────────────────────
# 5. Install dependencies
# ─────────────────────────────────────────────────────────────

echo "📋 Step 5: Installing dependencies..."
echo ""
echo "Choose installation type:"
echo "  1) Student (core packages only) - Recommended for course"
echo "  2) Developer (includes testing, docs, profiling tools)"
echo "  3) Full (everything including Jupyter extras)"
echo ""
read -p "Enter choice (1/2/3) [1]: " -n 1 -r INSTALL_CHOICE
echo ""
echo ""

# Default to student if no choice
if [ -z "$INSTALL_CHOICE" ]; then
    INSTALL_CHOICE="1"
fi

case $INSTALL_CHOICE in
    2)
        echo "   Installing core + development tools..."
        pip install -e ".[dev]" --quiet
        INSTALL_TYPE="developer"
        ;;
    3)
        echo "   Installing everything (core + dev + jupyter)..."
        pip install -e ".[all]" --quiet
        INSTALL_TYPE="full"
        ;;
    *)
        echo "   Installing core packages..."
        pip install -e . --quiet
        INSTALL_TYPE="student"
        ;;
esac

echo "✅ Dependencies installed! (Type: $INSTALL_TYPE)"
echo ""

# ─────────────────────────────────────────────────────────────
# 6. Verify installation
# ─────────────────────────────────────────────────────────────

echo "📋 Step 6: Verifying installation..."

python -c "
import sys
import pandas as pd
import numpy as np
import sklearn
import matplotlib
import seaborn

print('   ✅ pandas:', pd.__version__)
print('   ✅ numpy:', np.__version__)
print('   ✅ scikit-learn:', sklearn.__version__)
print('   ✅ matplotlib:', matplotlib.__version__)
print('   ✅ seaborn:', seaborn.__version__)
"

echo "✅ All core packages verified!"
echo ""

# ─────────────────────────────────────────────────────────────
# 7. Generate sample data
# ─────────────────────────────────────────────────────────────

echo "📋 Step 7: Generating sample data..."

if [ -f "data/raw/sample_bike_weather.csv" ]; then
    echo "⚠️  Sample data already exists."
    read -p "   Do you want to regenerate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        python src/generate_sample_data.py
    else
        echo "   Keeping existing sample data."
    fi
else
    python src/generate_sample_data.py
fi

echo "✅ Sample data ready!"
echo ""

# ─────────────────────────────────────────────────────────────
# 8. Summary
# ─────────────────────────────────────────────────────────────

echo "════════════════════════════════════════════════════════════"
echo "🎉 Setup Complete!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "Your environment is ready to go!"
echo ""
echo "📂 Project structure:"
echo "   ✅ Virtual environment: .venv/"
echo "   ✅ Sample data: data/raw/sample_bike_weather.csv"
echo "   ✅ Notebooks: notebooks/"
echo ""
echo "🚀 Next steps:"
echo "   1. Activate the environment (if not already active):"
echo "      source .venv/bin/activate"
echo ""
echo "   2. Start Jupyter:"
echo "      jupyter notebook"
echo ""
echo "   3. Open the first notebook:"
echo "      notebooks/Module_01_Introduction/M1_01_project_overview.ipynb"
echo ""
echo "📚 Documentation:"
echo "   - README.md - Project overview"
echo "   - docs/python_version_setup.md - Environment details"
echo "   - docs/dependency_management.md - Package management"
echo ""
echo "💡 Tip: To deactivate the environment later, just type 'deactivate'"
echo ""
echo "════════════════════════════════════════════════════════════"
