# 🔐 API Key Management Guide

**Forward-Looking Best Practices**

This guide provides best practices for managing API keys when working with services that require authentication. While the core course uses free APIs without authentication (CityBikes, Open-Meteo, KNMI), these patterns become essential when expanding to other data sources.

**Approach**: Simple, cloud-aligned pattern using `secrets.json` for local development and environment variables for production.

---

## 🎯 When You Need This

**APIs in this course** (no keys needed):
- ✅ CityBikes API
- ✅ Open-Meteo API  
- ✅ KNMI Weather API

**APIs you might use later** (require keys):
- 🔑 OpenWeatherMap (paid tier)
- 🔑 Google Maps API
- 🔑 Twitter API
- 🔑 Most commercial data services

**This guide helps you** transition from course projects to real-world data sources that require secure authentication.

---

## ⚠️ The Problem: Hardcoded Secrets

### ❌ What NOT to Do

```python
# NEVER DO THIS!
API_KEY = "sk_live_a1b2c3d4e5f6g7h8i9j0"  # Hardcoded secret

response = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": f"Bearer {API_KEY}"}
)
```

**Why this is dangerous:**
1. 🚨 Key gets committed to git (visible in history forever)
2. 🚨 Exposed on GitHub/GitLab (bots scan for keys within minutes)
3. 🚨 Shared accidentally when showing code
4. 🚨 Can't change keys without changing code
5. 🚨 Different keys for dev/prod requires code changes

---

## ✅ Simple Cloud-Aligned Approach

### Two-Tier Strategy

**Local Development** → `secrets.json` file (gitignored)  
**Production** → Environment variables (from cloud secret stores)

This approach:
- ✅ Simple (just JSON, no extra dependencies)
- ✅ Mirrors cloud-native patterns

---

## 🔧 Local Development: secrets.json

### Step 1: Create `secrets.json`

Create a file named `secrets.json` in your project root:

```json
{
  "openweather_api_key": "your_openweather_key_here",
  "google_maps_api_key": "your_google_maps_key_here",
  "database_url": "postgresql://user:pass@localhost:5432/bikes",
  "environment": "development"
}
```

**Why JSON?**
- Simple and readable
- No additional Python packages needed
- Easy to parse with `json` module (built-in)
- Clear separation from `.venv` folders

### Step 2: Add to `.gitignore`

**CRITICAL**: Ensure `secrets.json` is in your `.gitignore`:

```bash
# .gitignore

# Python virtual environment
.venv/
venv/
env/

# Secrets (NEVER commit!)
secrets.json
secrets.*.json

# Other
__pycache__/
*.pyc
```

Verify it's ignored:
```bash
git status  # secrets.json should NOT appear
git check-ignore secrets.json  # Should output: secrets.json
```

### Step 3: Load in Python

**Simple loading function**:
```python
import json
import os
from pathlib import Path

def load_secret(key: str, default=None):
    """
    Load secret from secrets.json (local) or environment variable (production).
    
    Local development: Reads from secrets.json
    Production: Reads from environment variables
    
    Parameters:
    -----------
    key : str
        Secret key name (lowercase with underscores)
    default : any
        Default value if secret not found
    
    Returns:
    --------
    Secret value or default
    """
    # Try environment variable first (production)
    env_value = os.getenv(key.upper())
    if env_value:
        return env_value
    
    # Fall back to secrets.json (local development)
    secrets_file = Path(__file__).parent / 'secrets.json'
    
    if secrets_file.exists():
        with open(secrets_file) as f:
            secrets = json.load(f)
            return secrets.get(key, default)
    
    return default

# Usage
API_KEY = load_secret('openweather_api_key')

if not API_KEY:
    raise ValueError("openweather_api_key not found in secrets.json or environment!")
```

---

## ☁️ Production: Environment Variables

In production (cloud), set environment variables directly - **do NOT deploy `secrets.json`**.

### Cloud Platforms

**AWS (Systems Manager Parameter Store)**:
```bash
aws ssm put-parameter \
    --name /myapp/openweather_api_key \
    --value "your_key_here" \
    --type SecureString
```

**Google Cloud (Secret Manager)**:
```bash
echo -n "your_key_here" | gcloud secrets create openweather-api-key --data-file=-
```

**Azure (Key Vault)**:
```bash
az keyvault secret set \
    --vault-name mykeyvault \
    --name openweather-api-key \
    --value "your_key_here"
```

**Heroku**:
```bash
heroku config:set OPENWEATHER_API_KEY=your_key_here
```

### Local Testing with Environment Variables

You can also set environment variables locally for testing production-like behavior:

**Linux/Mac**:
```bash
export OPENWEATHER_API_KEY="your_key_here"
python script.py
```

**Windows (PowerShell)**:
```powershell
$env:OPENWEATHER_API_KEY = "your_key_here"
python script.py
```

---

## 📝 Complete Working Example

### File Structure
```
bike-availability-project/
├── .gitignore              # Includes secrets.json
├── secrets.json            # Local secrets (NOT in git)
├── secrets.example.json    # Template (CAN commit this)
├── config.py               # Secret loading logic
└── fetch_weather.py        # Your application code
```

### File: `secrets.example.json`
```json
{
  "openweather_api_key": "your_openweather_key_here",
  "google_maps_api_key": "your_google_maps_key_here",
  "database_url": "postgresql://user:password@localhost:5432/bikes",
  "environment": "development"
}
```
**Note**: This template CAN be committed to git. Users copy it to `secrets.json` and fill in real values.

### File: `config.py`
```python
"""
Configuration and secret management.

Loads secrets from:
- secrets.json (local development)
- Environment variables (production)
"""

import json
import os
from pathlib import Path
from typing import Optional

# Determine project root
PROJECT_ROOT = Path(__file__).parent

def load_secret(key: str, required: bool = False) -> Optional[str]:
    """
    Load secret from secrets.json or environment variable.
    
    Priority:
    1. Environment variable (UPPERCASE)
    2. secrets.json (lowercase_with_underscores)
    
    Parameters:
    -----------
    key : str
        Secret key name (use lowercase_with_underscores)
    required : bool
        If True, raise error if secret not found
    
    Returns:
    --------
    str or None
        Secret value or None if not found
    
    Example:
    --------
    >>> api_key = load_secret('openweather_api_key', required=True)
    """
    # Try environment variable first (production)
    env_key = key.upper()
    env_value = os.getenv(env_key)
    
    if env_value:
        return env_value
    
    # Fall back to secrets.json (local development)
    secrets_file = PROJECT_ROOT / 'secrets.json'
    
    if secrets_file.exists():
        try:
            with open(secrets_file) as f:
                secrets = json.load(f)
                value = secrets.get(key)
                
                if value:
                    return value
        except json.JSONDecodeError as e:
            print(f"⚠️ Warning: Could not parse secrets.json: {e}")
    
    # Secret not found
    if required:
        raise ValueError(
            f"Required secret '{key}' not found!\n"
            f"Set environment variable {env_key} or add to secrets.json"
        )
    
    return None

def get_environment() -> str:
    """Get current environment (development, staging, production)."""
    return load_secret('environment') or 'development'

# Load common secrets
OPENWEATHER_API_KEY = load_secret('openweather_api_key')
DATABASE_URL = load_secret('database_url')
```

### File: `fetch_weather.py`
```python
"""
Fetch weather data using OpenWeatherMap API.
"""

import requests
from config import load_secret

def fetch_weather(city: str):
    """
    Fetch current weather for a city using OpenWeatherMap API.
    
    Requires openweather_api_key in secrets.json or OPENWEATHER_API_KEY env var.
    """
    # Load API key
    api_key = load_secret('openweather_api_key', required=True)
    
    # Make API request
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None

# Usage
if __name__ == "__main__":
    weather = fetch_weather("Amsterdam")
    if weather:
        print(f"Temperature: {weather['main']['temp']}°C")
        print(f"Conditions: {weather['weather'][0]['description']}")
```

### Setup Instructions for Users

**1. Copy template:**
```bash
cp secrets.example.json secrets.json
```

**2. Edit `secrets.json` with your actual keys**

**3. Verify it's gitignored:**
```bash
git check-ignore secrets.json  # Should output: secrets.json
```

**4. Run your code:**
```bash
python fetch_weather.py
```

---

## 🔒 Security Best Practices

### 1. **Never Commit secrets.json**
```bash
# Before committing, always check:
git status          # secrets.json should NOT appear
git diff --cached   # No keys should be visible
```

### 2. **Provide a Template**
```bash
# Create secrets.example.json (can commit)
cp secrets.json secrets.example.json

# Remove actual values
# Edit secrets.example.json to replace real values with placeholders
```

### 3. **Different Secrets for Each Environment**
```json
// secrets.development.json
{
  "openweather_api_key": "dev_key_12345",
  "environment": "development"
}

// secrets.production.json (DON'T deploy this - use env vars instead!)
{
  "openweather_api_key": "prod_key_67890",
  "environment": "production"
}
```

Load with:
```python
import os

environment = os.getenv('ENVIRONMENT', 'development')
secrets_file = f'secrets.{environment}.json'
```

### 4. **Rotate Keys Regularly**
- Generate new keys every 3-6 months
- Immediately rotate if exposed
- Use key expiration features when available

### 5. **Validate Secrets Are Loaded**
```python
def validate_secrets():
    """Validate required secrets are configured."""
    required = ['openweather_api_key', 'database_url']
    missing = []
    
    for key in required:
        if not load_secret(key):
            missing.append(key)
    
    if missing:
        raise ValueError(
            f"Missing required secrets: {', '.join(missing)}\n"
            f"Create secrets.json or set environment variables"
        )

# Run on startup
validate_secrets()
```

---

## 🎓 Jupyter Notebook Special Case

Jupyter notebooks present unique challenges since code is often shared.

### ❌ Bad: Hardcoded in Notebook
```python
# Cell 1 - NEVER DO THIS
API_KEY = "sk_live_a1b2c3d4e5f6"
```

### ✅ Good: Load from Config Module
```python
# Cell 1 - Setup
import sys
sys.path.append('..')  # If notebook in subfolder

from config import load_secret

API_KEY = load_secret('openweather_api_key', required=True)
print("✅ API key loaded successfully!")
```

### ✅ Better: User-Friendly Error Messages
```python
# Cell 1 - Setup with helpful errors
import sys
sys.path.append('..')

try:
    from config import load_secret
    API_KEY = load_secret('openweather_api_key', required=True)
    print("✅ API key loaded successfully!")
except ValueError as e:
    print("❌ API key not found!")
    print("\n📝 To fix this:")
    print("   1. Copy secrets.example.json to secrets.json")
    print("   2. Edit secrets.json with your OpenWeatherMap API key")
    print("   3. Restart this notebook")
    raise
```

### 🧹 Before Sharing Notebooks
Always clear output before sharing:
```bash
# Clear all cell outputs
jupyter nbconvert --clear-output --inplace notebook.ipynb

# Or use VS Code: Notebook > Clear All Outputs
```

---

## 🐳 Docker & Containers

When using Docker, pass environment variables at runtime (don't copy secrets.json into container):

**docker-compose.yml**:
```yaml
services:
  app:
    build: .
    environment:
      - OPENWEATHER_API_KEY=${OPENWEATHER_API_KEY}
      - DATABASE_URL=${DATABASE_URL}
    # DO NOT mount secrets.json!
```

**Dockerfile** (don't copy secrets):
```dockerfile
FROM python:3.11

WORKDIR /app

# Copy application code
COPY src/ ./src/
COPY config.py ./

# DO NOT: COPY secrets.json ./

# Application reads from environment variables
CMD ["python", "src/main.py"]
```

**Run with environment variables**:
```bash
docker run -e OPENWEATHER_API_KEY=$OPENWEATHER_API_KEY myapp
```

---

## 🚨 What If I Already Committed a Secret?

If you accidentally committed `secrets.json` or a hardcoded key:

### 1. **Rotate the Key Immediately**
- Go to the service and generate a new key
- Revoke the exposed key
- Don't just delete from git - keys remain in history!

### 2. **Remove from Git History**
```bash
# Remove file from git history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch secrets.json" \
  --prune-empty --tag-name-filter cat -- --all

# Force push (WARNING: affects all collaborators)
git push origin --force --all
```

**Better approach**: Use BFG Repo-Cleaner:
```bash
# Install BFG: https://rtyley.github.io/bfg-repo-cleaner/
bfg --delete-files secrets.json
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

### 3. **Notify Your Team**
- Alert collaborators to the exposed key
- Inform the service provider if required
- Document the incident for future learning

---

## 📚 Additional Resources

### Tools
- **BFG Repo-Cleaner**: Remove secrets from git history
- **git-secrets**: Prevent committing secrets to git
- **truffleHog**: Scan git repos for secrets
- **direnv**: Auto-load environment variables per directory

### Services
- **AWS Secrets Manager**: Cloud-based secret storage
- **Google Cloud Secret Manager**: GCP secret management
- **Azure Key Vault**: Azure secret storage
- **HashiCorp Vault**: Enterprise secret management

### Reading
- [OWASP Secret Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [The Twelve-Factor App - Config](https://12factor.net/config)

---

## ✅ Quick Checklist

Before expanding to authenticated APIs:

- [ ] Create `secrets.example.json` template (can commit)
- [ ] Add `secrets.json` to `.gitignore`
- [ ] Verify with `git check-ignore secrets.json`
- [ ] Create `config.py` with `load_secret()` function
- [ ] Load secrets using config module (not hardcoded)
- [ ] Validate required secrets on startup
- [ ] Never print/log actual secret values
- [ ] Clear Jupyter outputs before sharing
- [ ] Document required secrets in README
- [ ] Use environment variables in production (not secrets.json)

---

## 🎯 Summary

**Key Takeaways**:
1. ✅ Use `secrets.json` for local development (gitignored, simple JSON)
2. ✅ Use environment variables for production (from cloud secret stores)
3. ✅ Create `load_secret()` function that checks both sources
4. ✅ Provide `secrets.example.json` template for team members
5. ✅ Validate secrets are loaded before using
6. ✅ Never deploy `secrets.json` to production
7. ✅ Clear Jupyter outputs before sharing

**Why This Approach?**
- Simple: No dependencies (just built-in `json` module)
- Clear: No confusion with Python `.venv` folders
- Cloud-aligned: Mirrors production environment variable patterns
- Educational: Shows both local and production approaches

**Remember**: The APIs in this course don't require keys, but these patterns are essential for real-world projects. Practice them now so they're second nature when you need them!

---

**Related Guides**:
- [Open Data Sources](../reference/open_data_sources.md) - Free APIs without authentication
- [Coding Standards](../standards/coding_standards.md) - General code quality practices

**Module References**:
- [Module 02 Overview](../../notebooks/Module_02_Data_Acquisition/MODULE_02_OVERVIEW.md) - Brief mention of secret management

### Linux/Mac:
```bash
# Set for current session
export OPENWEATHER_API_KEY="your_key_here"

# Set permanently (add to ~/.bashrc or ~/.zshrc)
echo 'export OPENWEATHER_API_KEY="your_key_here"' >> ~/.bashrc
source ~/.bashrc
```

### Windows (Command Prompt):
```cmd
# Set for current session
set OPENWEATHER_API_KEY=your_key_here

# Set permanently
setx OPENWEATHER_API_KEY "your_key_here"
```

### Windows (PowerShell):
```powershell
# Set for current session
$env:OPENWEATHER_API_KEY = "your_key_here"

# Set permanently
[System.Environment]::SetEnvironmentVariable('OPENWEATHER_API_KEY', 'your_key_here', 'User')
```

### Python Usage (no dotenv needed):
```python
import os

# Reads from system environment
API_KEY = os.getenv('OPENWEATHER_API_KEY')
```

---

## 📝 Complete Working Example

### Example: OpenWeatherMap Integration

**File: `.env`**
```bash
OPENWEATHER_API_KEY=a1b2c3d4e5f6g7h8i9j0
```

**File: `fetch_weather.py`**
```python
import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def fetch_weather(city: str):
    """
    Fetch current weather for a city using OpenWeatherMap API.
    
    Requires OPENWEATHER_API_KEY environment variable.
    """
    # Get API key from environment
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    # Validate key exists
    if not api_key:
        raise ValueError(
            "OPENWEATHER_API_KEY not found!\n"
            "Create a .env file with: OPENWEATHER_API_KEY=your_key_here"
        )
    
    # Make API request
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None

# Usage
if __name__ == "__main__":
    weather = fetch_weather("Amsterdam")
    if weather:
        print(f"Temperature: {weather['main']['temp']}°C")
        print(f"Conditions: {weather['weather'][0]['description']}")
```

---

## 🔒 Security Best Practices

### 1. **Never Commit Secrets**
```bash
# Before committing, always check:
git status          # .env should not appear
git diff --cached   # No keys should be visible
```

### 2. **Use Different Keys for Dev/Prod**
```bash
# .env.development
OPENWEATHER_API_KEY=dev_key_12345

# .env.production  
OPENWEATHER_API_KEY=prod_key_67890
```

Load the appropriate one:
```python
import os
from dotenv import load_dotenv

environment = os.getenv('ENVIRONMENT', 'development')
load_dotenv(f'.env.{environment}')
```

### 3. **Rotate Keys Regularly**
- Generate new keys every 3-6 months
- Immediately rotate if exposed
- Use key expiration features when available

### 4. **Limit Key Permissions**
- Use read-only keys when possible
- Restrict by IP address if supported
- Set usage quotas
- Enable alerting for unusual activity

### 5. **Document Required Keys**
Create a `.env.example` file (this CAN be committed):

```bash
# .env.example - Template for required environment variables

# Copy this to .env and fill in your actual values
# cp .env.example .env

# Weather API Keys
OPENWEATHER_API_KEY=your_key_here
WEATHERAPI_KEY=your_key_here

# Map API Keys
GOOGLE_MAPS_API_KEY=your_key_here

# Database Connection
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Environment Configuration
ENVIRONMENT=development
DEBUG=True
```

---

## 🎓 Jupyter Notebook Special Case

Jupyter notebooks present unique challenges since code is often shared.

### ❌ Bad: Hardcoded in Notebook
```python
# Cell 1 - NEVER DO THIS
API_KEY = "sk_live_a1b2c3d4e5f6"
```

### ✅ Good: Load from Environment
```python
# Cell 1 - Setup
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

if not API_KEY:
    print("⚠️ Warning: OPENWEATHER_API_KEY not found!")
    print("Create a .env file in project root with your API key")
```

### ✅ Better: User-Friendly Fallback
```python
# Cell 1 - Setup with prompt fallback
import os
from dotenv import load_dotenv
from getpass import getpass

load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')

if not API_KEY:
    print("📝 OPENWEATHER_API_KEY not found in environment")
    print("You can either:")
    print("  1. Create a .env file with: OPENWEATHER_API_KEY=your_key")
    print("  2. Enter it now (won't be saved)")
    
    use_prompt = input("\nEnter key manually? (y/n): ").lower() == 'y'
    if use_prompt:
        API_KEY = getpass("Enter API key: ")
    else:
        raise ValueError("API key required!")

print("✅ API key loaded!")
```

### 🧹 Before Sharing Notebooks
Always clear output before sharing:
```bash
# Clear all cell outputs
jupyter nbconvert --clear-output --inplace notebook.ipynb

# Or use VS Code: Notebook > Clear All Outputs
```

---

## 🐳 Docker & Containers

When using Docker, pass environment variables at runtime:

**docker-compose.yml**:
```yaml
services:
  app:
    build: .
    environment:
      - OPENWEATHER_API_KEY=${OPENWEATHER_API_KEY}
      - DATABASE_URL=${DATABASE_URL}
    env_file:
      - .env
```

**docker run**:
```bash
docker run -e OPENWEATHER_API_KEY=$OPENWEATHER_API_KEY myapp
```

---

## ☁️ Cloud Deployment

Different platforms have different secret management:

### Heroku
```bash
heroku config:set OPENWEATHER_API_KEY=your_key_here
```

### AWS (Parameter Store)
```bash
aws ssm put-parameter \
    --name /myapp/openweather-key \
    --value "your_key_here" \
    --type SecureString
```

### Google Cloud
```bash
echo -n "your_key_here" | gcloud secrets create openweather-key --data-file=-
```

### Azure
```bash
az keyvault secret set \
    --vault-name mykeyvault \
    --name openweather-key \
    --value "your_key_here"
```

---

## 🚨 What If I Already Committed a Key?

If you accidentally committed an API key:

### 1. **Rotate the Key Immediately**
- Go to the service and generate a new key
- Revoke the exposed key
- Don't just delete from git - keys remain in history!

### 2. **Remove from Git History** (Nuclear Option)
```bash
# WARNING: Rewrites git history, affects all collaborators
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/file/with/key" \
  --prune-empty --tag-name-filter cat -- --all

git push origin --force --all
```

### 3. **Notify Your Team**
- Alert collaborators to the exposed key
- Inform the service provider if required
- Document the incident for future learning

---

## 📚 Additional Resources

### Tools
- **python-dotenv**: https://github.com/theskumar/python-dotenv
- **direnv**: Auto-load environment variables per directory
- **git-secrets**: Prevent committing secrets to git
- **truffleHog**: Scan git repos for secrets

### Services
- **1Password / Bitwarden**: Password managers with secret sharing
- **HashiCorp Vault**: Enterprise secret management
- **AWS Secrets Manager**: Cloud-based secret storage
- **GitHub Secrets**: CI/CD secret management

### Reading
- [OWASP Secret Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [The Twelve-Factor App - Config](https://12factor.net/config)

---

## ✅ Quick Checklist

Before expanding to authenticated APIs:

- [ ] Install `python-dotenv`: `pip install python-dotenv`
- [ ] Create `.env` file in project root
- [ ] Add `.env` to `.gitignore`
- [ ] Verify with `git check-ignore .env`
- [ ] Create `.env.example` template (can commit this)
- [ ] Load with `load_dotenv()` in code
- [ ] Validate keys are loaded with error checking
- [ ] Never print/log actual key values
- [ ] Clear Jupyter outputs before sharing
- [ ] Document required keys in README

---

## 🎯 Summary

**Key Takeaways**:
1. ✅ Use `.env` files for local development (never commit them)
2. ✅ Use system environment variables for production
3. ✅ Validate keys are loaded before using
4. ✅ Use different keys for dev/prod/test
5. ✅ Rotate keys regularly
6. ✅ Clear Jupyter outputs before sharing
7. ✅ Provide `.env.example` for team members

**Remember**: The APIs in this course don't require keys, but these patterns are essential for real-world projects. Practice them now so they're second nature when you need them!

---

**Related Guides**:
- [Open Data Sources](../reference/open_data_sources.md) - Free APIs without authentication
- [Coding Standards](../standards/coding_standards.md) - General code quality practices

**Module References**:
- [Module 02 Overview](../../notebooks/Module_02_Data_Acquisition/MODULE_02_OVERVIEW.md) - Brief mention of environment variables
