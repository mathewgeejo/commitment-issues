#!/usr/bin/env python3
"""
GitHub Commit Generator
A script to generate multiple commits for demonstration purposes.
"""

import os
import sys
import subprocess
import random
import datetime
import argparse
from pathlib import Path

class CommitGenerator:
    def __init__(self, repo_path=None):
        self.repo_path = Path(repo_path) if repo_path else Path.cwd()
        self.commit_messages = [
            "Fix typo in documentation",
            "Update README formatting",
            "Refactor code structure",
            "Add error handling",
            "Improve performance",
            "Update dependencies",
            "Fix bug in main function",
            "Add new feature",
            "Remove unused code",
            "Update configuration",
            "Enhance user experience",
            "Fix security vulnerability",
            "Optimize algorithm",
            "Add unit tests",
            "Update comments",
            "Clean up code",
            "Fix formatting issues",
            "Add logging functionality",
            "Update version number",
            "Merge branch updates"
        ]
        
        self.target_file = "activity_log.txt"
        self.base_content = "# Activity Log\n\nThis file tracks project activity and changes.\n\n"

    def run_git_command(self, command):
        """Execute a git command and return the result."""
        try:
            result = subprocess.run(
                command,
                cwd=self.repo_path,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Git command failed: {e}")
            print(f"Error output: {e.stderr}")
            return None

    def ensure_git_repo(self):
        """Ensure we're in a git repository."""
        if not (self.repo_path / ".git").exists():
            print("Not a git repository. Initializing...")
            self.run_git_command("git init")
            
        # Check if we have a remote origin
        result = self.run_git_command("git remote -v")
        if not result:
            print("Warning: No remote repository configured.")
            print("Add a remote with: git remote add origin <your-repo-url>")

    def modify_activity_file(self):
        """Modify the single activity log file."""
        filepath = self.repo_path / self.target_file
        
        if not filepath.exists():
            # Create the file for the first time
            with open(filepath, 'w') as f:
                f.write(self.base_content)
        
        # Add a new entry with timestamp and random activity
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        activities = [
            "Code optimization performed",
            "Documentation updated", 
            "Bug fix implemented",
            "Feature enhancement added",
            "Security improvement made",
            "Performance tuning completed",
            "Code refactoring done",
            "Unit tests updated",
            "Configuration adjusted",
            "Dependencies reviewed",
            "Error handling improved",
            "Logging functionality enhanced",
            "Code cleanup performed",
            "Algorithm optimization",
            "User interface improved"
        ]
        
        activity = random.choice(activities)
        new_entry = f"[{timestamp}] {activity}\n"
        
        with open(filepath, 'a') as f:
            f.write(new_entry)

    def make_commit(self, message=None):
        """Make a single commit."""
        # Modify the single activity file
        self.modify_activity_file()
        
        # Add to git
        self.run_git_command(f"git add {self.target_file}")
        
        # Commit with message
        if not message:
            message = random.choice(self.commit_messages)
        
        commit_msg = f'"{message}"'
        result = self.run_git_command(f"git commit -m {commit_msg}")
        
        if result is not None:
            print(f"✓ Committed: {message}")
            return True
        else:
            print(f"✗ Failed to commit: {message}")
            return False

    def generate_commits(self, count, delay=0):
        """Generate multiple commits."""
        print(f"Generating {count} commits...")
        
        successful_commits = 0
        
        for i in range(count):
            if self.make_commit():
                successful_commits += 1
            
            # Add delay between commits if specified
            if delay > 0 and i < count - 1:
                import time
                time.sleep(delay)
        
        print(f"\nCompleted: {successful_commits}/{count} commits generated")
        
        # Automatically push to remote
        if successful_commits > 0:
            print("Automatically pushing to remote...")
            result = self.run_git_command("git push")
            if result is not None:
                print("✓ Successfully pushed to remote!")
            else:
                print("✗ Failed to push. Make sure you have a remote configured.")
                print("You can manually push later with: git push")

def main():
    parser = argparse.ArgumentParser(description="Generate GitHub commits for profile activity")
    parser.add_argument("count", type=int, help="Number of commits to generate")
    parser.add_argument("--delay", type=float, default=0, help="Delay between commits in seconds")
    parser.add_argument("--path", type=str, help="Repository path (default: current directory)")
    
    args = parser.parse_args()
    
    if args.count <= 0:
        print("Error: Commit count must be positive")
        sys.exit(1)
    
    if args.count > 100:
        confirm = input(f"You're about to generate {args.count} commits. Continue? (y/n): ")
        if confirm.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)
    
    generator = CommitGenerator(args.path)
    generator.ensure_git_repo()
    generator.generate_commits(args.count, args.delay)

if __name__ == "__main__":
    main()