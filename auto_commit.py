#!/usr/bin/env python3
"""
Automated Daily Commit Generator
Runs daily to generate 15-25 commits with realistic messages and timing distribution.
"""

import os
import sys
import subprocess
import random
import datetime
import time
import json
from pathlib import Path

class AutoCommitGenerator:
    def __init__(self, repo_path=None, config_file="commit_config.json"):
        self.repo_path = Path(repo_path) if repo_path else Path.cwd()
        self.config_file = self.repo_path / config_file
        self.load_config()
        
        # Expanded realistic commit messages
        self.commit_messages = [
            "Fix typo in documentation",
            "Update README formatting", 
            "Refactor code structure",
            "Add error handling",
            "Improve performance optimization",
            "Update dependencies to latest versions",
            "Fix bug in main function",
            "Add new feature implementation",
            "Remove unused code and imports",
            "Update configuration settings",
            "Enhance user experience",
            "Fix security vulnerability",
            "Optimize algorithm efficiency",
            "Add comprehensive unit tests",
            "Update inline comments",
            "Clean up code formatting",
            "Fix linting issues",
            "Add robust logging functionality",
            "Bump version number",
            "Merge feature branch updates",
            "Implement code review feedback",
            "Add input validation",
            "Fix memory leak issue",
            "Update API documentation",
            "Improve error messages",
            "Add configuration validation",
            "Fix race condition bug",
            "Optimize database queries",
            "Add retry mechanism",
            "Update test coverage",
            "Fix edge case handling",
            "Improve code readability",
            "Add progress indicators",
            "Fix timezone handling",
            "Update logging levels",
            "Add cache invalidation",
            "Fix string formatting",
            "Improve exception handling",
            "Add health check endpoint",
            "Update build configuration",
            "Fix null pointer exception",
            "Add request timeout handling",
            "Improve data validation",
            "Fix concurrent access issue",
            "Update environment variables",
            "Add monitoring metrics",
            "Fix resource cleanup",
            "Improve startup performance",
            "Add graceful shutdown",
            "Fix character encoding issue"
        ]
        
        self.target_file = "activity_log.txt"
        self.base_content = "# Daily Activity Log\n\nThis file tracks automated daily development activity.\n\n"

    def load_config(self):
        """Load configuration from JSON file or create default."""
        default_config = {
            "min_commits": 15,
            "max_commits": 25,
            "min_delay_minutes": 5,
            "max_delay_minutes": 45,
            "work_hours_start": 9,
            "work_hours_end": 18,
            "enable_random_timing": True
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
                # Merge with defaults for any missing keys
                for key, value in default_config.items():
                    if key not in self.config:
                        self.config[key] = value
            except:
                self.config = default_config
        else:
            self.config = default_config
            self.save_config()

    def save_config(self):
        """Save current configuration to JSON file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

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
            return False
        return True

    def modify_activity_file(self):
        """Modify the single activity log file."""
        filepath = self.repo_path / self.target_file
        
        if not filepath.exists():
            with open(filepath, 'w') as f:
                f.write(self.base_content)
        
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
            "User interface improved",
            "Database query optimized",
            "API endpoint updated",
            "Memory usage optimized",
            "Code coverage increased",
            "Build process improved"
        ]
        
        activity = random.choice(activities)
        new_entry = f"[{timestamp}] {activity}\n"
        
        with open(filepath, 'a') as f:
            f.write(new_entry)

    def make_commit(self, message=None):
        """Make a single commit."""
        self.modify_activity_file()
        
        self.run_git_command(f"git add {self.target_file}")
        
        if not message:
            message = random.choice(self.commit_messages)
        
        commit_msg = f'"{message}"'
        result = self.run_git_command(f"git commit -m {commit_msg}")
        
        if result is not None:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] ✓ Committed: {message}")
            return True
        else:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] ✗ Failed to commit: {message}")
            return False

    def generate_commit_times(self, num_commits):
        """Generate realistic commit times throughout the day."""
        if not self.config["enable_random_timing"]:
            # Simple even distribution
            return [i * (self.config["max_delay_minutes"] // num_commits) for i in range(num_commits)]
        
        times = []
        work_start = self.config["work_hours_start"] * 60  # Convert to minutes
        work_end = self.config["work_hours_end"] * 60
        work_duration = work_end - work_start
        
        # Generate more commits during work hours
        work_commits = int(num_commits * 0.7)  # 70% during work hours
        off_commits = num_commits - work_commits
        
        # Work hour commits
        for _ in range(work_commits):
            time_offset = random.randint(0, work_duration)
            times.append(work_start + time_offset)
        
        # Off-hour commits (early morning, evening)
        for _ in range(off_commits):
            if random.choice([True, False]):
                # Early morning (6 AM - 9 AM)
                time_offset = random.randint(6 * 60, work_start)
            else:
                # Evening (6 PM - 11 PM)
                time_offset = random.randint(work_end, 23 * 60)
            times.append(time_offset)
        
        return sorted(times)

    def run_daily_commits(self):
        """Run the daily commit generation process."""
        if not self.ensure_git_repo():
            print("❌ No remote repository configured. Please set up your remote first:")
            print("git remote add origin https://github.com/yourusername/your-repo.git")
            return False

        # Generate random number of commits for today
        num_commits = random.randint(self.config["min_commits"], self.config["max_commits"])
        
        print(f"🚀 Starting daily commit generation...")
        print(f"📊 Target commits for today: {num_commits}")
        print(f"⏰ Started at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        successful_commits = 0
        commit_times = self.generate_commit_times(num_commits)
        
        for i, _ in enumerate(commit_times):
            if self.make_commit():
                successful_commits += 1
            
            # Add realistic delay between commits (except for the last one)
            if i < len(commit_times) - 1:
                delay = random.randint(
                    self.config["min_delay_minutes"] * 60,  # Convert to seconds
                    self.config["max_delay_minutes"] * 60
                )
                next_commit_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)
                print(f"⏳ Next commit in {delay//60} minutes at {next_commit_time.strftime('%H:%M:%S')}")
                time.sleep(delay)
        
        print(f"\n📈 Daily Summary:")
        print(f"✅ Completed: {successful_commits}/{num_commits} commits")
        print(f"⏰ Finished at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Auto push to remote
        if successful_commits > 0:
            print("🔄 Pushing to remote repository...")
            result = self.run_git_command("git push")
            if result is not None:
                print("✅ Successfully pushed to remote!")
                return True
            else:
                print("❌ Failed to push. Check your remote configuration.")
                return False
        
        return successful_commits > 0

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        # Test mode - generate a few commits quickly
        generator = AutoCommitGenerator()
        generator.config["min_commits"] = 3
        generator.config["max_commits"] = 5
        generator.config["min_delay_minutes"] = 0
        generator.config["max_delay_minutes"] = 1
        print("🧪 Running in test mode...")
        generator.run_daily_commits()
    else:
        # Normal daily mode
        generator = AutoCommitGenerator()
        generator.run_daily_commits()

if __name__ == "__main__":
    main()