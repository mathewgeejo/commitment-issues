# Commitment Issues 🚀

An automated Python system to maintain consistent GitHub commit activity on your profile.

## Features

- **🤖 Full Automation**: Set it and forget it - runs daily at 6 AM
- **📊 Smart Commits**: 15-25 random commits per day with realistic timing
- **💬 Realistic Messages**: 50+ professional commit messages
- **⏰ Natural Timing**: Distributes commits throughout work hours
- **🔧 Configurable**: Customize commit counts, timing, and behavior
- **🌍 Cross-Platform**: Works on Windows, macOS, and Linux
- **📈 Profile Boost**: Consistent green squares on your GitHub profile

## 🚀 Quick Start

### 1. GUI Control Panel (Easiest)

```cmd
# Launch the GUI control panel
launch_gui.bat

# Or directly:
python commit_gui.py
```

**GUI Features:**
- 🎛️ Adjust commit counts (min/max per day)
- ⏰ Set timing delays between commits  
- 🕘 Configure work hours
- 💬 Add custom commit messages
- 🧪 Test automation with one click
- 🤖 Setup daily automation
- 📊 Generate manual commits

### 2. Command Line Usage

#### Manual Commits:
```bash
# Generate 20 commits immediately
python commit_generator.py 20

# Generate commits with delay  
python commit_generator.py 15 --delay 2
```

#### Automated Daily Commits:
```cmd
# Windows: Test automation
test_automation.bat

# Windows: Set up daily automation (Run as Administrator)
setup_scheduler.bat

# Linux/macOS: Set up daily cron job
./setup_cron.sh

# Manual daily run
python auto_commit.py
```

## 🔧 How Automation Works

### Daily Schedule:
- **🕕 6:00 AM**: Automation starts
- **📊 15-25 Commits**: Random count generated daily  
- **⏰ Smart Timing**: 70% during work hours (9 AM - 6 PM), 30% off-hours
- **🔄 Auto Push**: All commits automatically pushed to GitHub
- **📝 Single File**: Only modifies `activity_log.txt`

### Commit Distribution:
```
6 AM  ████░░░░░░░░░░░░░░░░░░░░░░░░  (Start + few early commits)
9 AM  ████████████████░░░░░░░░░░░░  (Work hours - most commits)
6 PM  ████████████████████░░░░░░░░  (Evening commits)
11 PM ████████████████████████░░░░  (Late commits end)
```

## ⚙️ Configuration

Customize behavior by editing `commit_config.json`:

```json
{
  "min_commits": 15,           // Minimum commits per day
  "max_commits": 25,           // Maximum commits per day  
  "min_delay_minutes": 5,      // Min delay between commits (0 for no delay)
  "max_delay_minutes": 45,     // Max delay between commits (0 for no delay)
  "work_hours_start": 9,       // Work day start (24hr format)
  "work_hours_end": 18,        // Work day end (24hr format)  
  "enable_random_timing": true // Realistic timing distribution
}
```

## 📋 Requirements

- Python 3.6+
- Git installed and configured
- GitHub repository with remote origin configured

## Setup

1. Clone or download this repository
2. Navigate to the directory
3. Ensure you have a Git remote configured:
   ```bash
   git remote add origin https://github.com/yourusername/your-repo.git
   ```
4. Run the script!

## 📊 Example Output

### Daily Automation:
```
🚀 Starting daily commit generation...
📊 Target commits for today: 23
⏰ Started at: 2025-10-10 06:00:15

[06:03:22] ✓ Committed: Fix typo in documentation
⏳ Next commit in 12 minutes at 06:15:22

[06:15:22] ✓ Committed: Update dependencies to latest versions  
⏳ Next commit in 8 minutes at 06:23:22

[06:23:22] ✓ Committed: Optimize algorithm efficiency
⏳ Next commit in 25 minutes at 06:48:22
...

📈 Daily Summary:
✅ Completed: 23/23 commits
⏰ Finished at: 2025-10-10 17:45:33
🔄 Pushing to remote repository...
✅ Successfully pushed to remote!
```

### Manual Usage:
```
python commit_generator.py 10
✓ Committed: Add error handling
✓ Committed: Improve performance  
✓ Committed: Update configuration
...
Completed: 10/10 commits generated
✅ Successfully pushed to remote!
```

## 📁 File Structure

```
commitment-issues/
├── commit_gui.py            # 🎛️ GUI Control Panel
├── launch_gui.bat          # 🚀 Launch GUI (Windows)
├── auto_commit.py           # 🤖 Main automation script
├── commit_generator.py      # 📝 Manual commit generator  
├── commit_config.json       # ⚙️ Configuration file
├── setup_scheduler.bat      # 🪟 Windows scheduler setup
├── setup_cron.sh           # 🐧 Linux/macOS cron setup
├── run_daily_commits.bat    # 🪟 Windows daily runner
├── test_automation.bat      # 🧪 Test automation
├── generate_commits.bat     # 📝 Manual generation (Windows)
└── activity_log.txt        # 📊 Generated commit log
```

## 🛡️ Safety & Best Practices

- **Safe Operations**: Only modifies a single text file (`activity_log.txt`)
- **Reversible**: All changes tracked in Git history
- **Professional**: Realistic commit messages and timing
- **Configurable**: Adjust behavior via configuration file
- **Transparent**: Clear logging and progress indicators

## 🔧 Troubleshooting

### Common Issues:

**"No remote repository configured"**
```bash
git remote add origin https://github.com/yourusername/your-repo.git
```

**Windows Task Scheduler fails**
- Run `setup_scheduler.bat` as Administrator
- Ensure Python is in your PATH

**Cron job not working (Linux/macOS)**
```bash
# Check if cron service is running
sudo systemctl status cron

# View cron logs
tail -f /var/log/cron.log
```

## 📈 Results

After setup, you'll see:
- ✅ 15-25 commits every day on your GitHub profile  
- 🟩 Consistent green squares on your contribution graph
- 📊 Realistic commit patterns with professional messages
- 🤖 Zero daily maintenance required

## ⚖️ Disclaimer

This tool is for educational and demonstration purposes. Use responsibly and ensure compliance with your organization's policies and GitHub's Terms of Service.