# Commitment Issues 🚀

A Python script to generate GitHub commits for profile activity demonstration.

## Features

- Generate multiple commits with meaningful messages
- Creates/modifies files in a structured way
- Configurable delay between commits
- Cross-platform compatibility
- Safe and reversible (creates only text files)

## Usage

### Python Script (Cross-platform)

```bash
# Generate 10 commits
python commit_generator.py 10

# Generate 5 commits with 2-second delay between each
python commit_generator.py 5 --delay 2

# Specify a different repository path
python commit_generator.py 10 --path /path/to/repo
```

### Windows Batch Script

```cmd
# Generate 10 commits
generate_commits.bat 10

# Generate 5 commits with 2-second delay
generate_commits.bat 5 2
```

## How It Works

1. **File Creation/Modification**: The script creates or modifies text files (progress.txt, notes.md, changelog.txt, etc.)
2. **Git Operations**: Each file change is staged and committed with a random, meaningful commit message
3. **Push Option**: After generating commits, you'll be prompted to push to your remote repository

## Files Created

The script will create and modify these files:
- `progress.txt` - Project progress tracker
- `notes.md` - Development notes
- `changelog.txt` - Project changelog  
- `tasks.txt` - Task list
- `dev_log.md` - Development log

## Requirements

- Python 3.6+
- Git installed and configured
- A Git repository (will initialize one if needed)

## Setup

1. Clone or download this repository
2. Navigate to the directory
3. Ensure you have a Git remote configured:
   ```bash
   git remote add origin https://github.com/yourusername/your-repo.git
   ```
4. Run the script!

## Example Output

```
Generating 5 commits...
✓ Committed: Fix typo in documentation  
✓ Committed: Update README formatting
✓ Committed: Add error handling
✓ Committed: Improve performance
✓ Committed: Update dependencies

Completed: 5/5 commits generated

Push commits to remote repository? (y/n): y
Pushing to remote...
✓ Successfully pushed to remote!
```

## Safety Notes

- This script only creates/modifies text files
- All changes are reversible through Git
- Files created are meaningful development artifacts
- Commit messages are realistic and professional

## Disclaimer

This tool is for educational and demonstration purposes. Use responsibly and in accordance with your organization's policies.