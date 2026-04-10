# 🚀 GitHub Setup Instructions

Follow these steps to publish your repository to GitHub.

---

## Step 1: Create a GitHub Account
If you don't have one, go to → https://github.com/signup

---

## Step 2: Create a New Repository on GitHub

1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `maternal-mortality-research`
   - **Description**: `Data analysis and research project on maternal mortality trends, determinants, and policy insights`
   - **Visibility**: Public (recommended for research)
   - ❌ Do NOT check "Initialize with README" (we already have one)
3. Click **"Create repository"**

---

## Step 3: Install Git (if not installed)

### Windows:
Download from → https://git-scm.com/download/win

### Linux/Mac:
```bash
sudo apt install git       # Ubuntu/Debian
brew install git           # macOS
```

---

## Step 4: Configure Git (first time only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Step 5: Initialize & Push the Repository

Open terminal inside the `maternal-mortality-research/` folder and run:

```bash
# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: Maternal Mortality Research project setup"

# Connect to GitHub (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/maternal-mortality-research.git

# Set branch name to main
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## Step 6: Verify on GitHub

Go to:
```
https://github.com/YOUR_USERNAME/maternal-mortality-research
```

You should see all your files live! ✅

---

## Step 7: Add Data Files (after cloning/downloading datasets)

```bash
# After downloading WHO/NFHS data into data/raw/
git add data/raw/
git commit -m "Add: raw datasets (WHO MMR, NFHS-5)"
git push
```

---

## Useful Git Commands

| Command | Purpose |
|---------|---------|
| `git status` | See changed files |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Save a snapshot |
| `git push` | Upload to GitHub |
| `git pull` | Download latest changes |
| `git log --oneline` | View commit history |

---

## Recommended GitHub Repository Settings

After pushing, go to your repo → **Settings** and:
- Add a **Description** and **Website** (if any)
- Add **Topics**: `maternal-mortality`, `public-health`, `data-analysis`, `python`, `india`, `who`, `gender`
- Enable **Issues** for tracking research tasks
- Add a **Wiki** for extended documentation
