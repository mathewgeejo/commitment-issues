#!/usr/bin/env python3
"""
GitHub Commit Generator GUI
A simple GUI to configure and control automated commit generation.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import os
import subprocess
import threading
from pathlib import Path

class CommitGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Commit Generator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        self.config_file = "commit_config.json"
        self.load_config()
        self.setup_gui()
        
    def load_config(self):
        """Load configuration from JSON file or create default."""
        default_config = {
            "min_commits": 15,
            "max_commits": 25,
            "min_delay_minutes": 5,
            "max_delay_minutes": 45,
            "work_hours_start": 9,
            "work_hours_end": 18,
            "enable_random_timing": True,
            "custom_messages": [
                "Fix typo in documentation",
                "Update README formatting",
                "Refactor code structure",
                "Add error handling",
                "Improve performance"
            ]
        }
        
        if os.path.exists(self.config_file):
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
            
    def save_config(self):
        """Save current configuration to JSON file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
        messagebox.showinfo("Success", "Configuration saved!")
        
    def setup_gui(self):
        """Setup the GUI components."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="GitHub Commit Generator", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Commit Count Settings
        count_frame = ttk.LabelFrame(main_frame, text="Daily Commit Count", padding="10")
        count_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(count_frame, text="Minimum commits per day:").grid(row=0, column=0, sticky=tk.W)
        self.min_commits_var = tk.StringVar(value=str(self.config["min_commits"]))
        min_commits_spin = ttk.Spinbox(count_frame, from_=1, to=50, width=10, textvariable=self.min_commits_var)
        min_commits_spin.grid(row=0, column=1, sticky=tk.E, padx=(5, 0))
        
        ttk.Label(count_frame, text="Maximum commits per day:").grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
        self.max_commits_var = tk.StringVar(value=str(self.config["max_commits"]))
        max_commits_spin = ttk.Spinbox(count_frame, from_=1, to=100, width=10, textvariable=self.max_commits_var)
        max_commits_spin.grid(row=1, column=1, sticky=tk.E, padx=(5, 0), pady=(5, 0))
        
        # Timing Settings
        timing_frame = ttk.LabelFrame(main_frame, text="Timing Settings", padding="10")
        timing_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(timing_frame, text="Min delay between commits (minutes):").grid(row=0, column=0, sticky=tk.W)
        self.min_delay_var = tk.StringVar(value=str(self.config["min_delay_minutes"]))
        min_delay_spin = ttk.Spinbox(timing_frame, from_=0, to=120, width=10, textvariable=self.min_delay_var)
        min_delay_spin.grid(row=0, column=1, sticky=tk.E, padx=(5, 0))
        
        ttk.Label(timing_frame, text="Max delay between commits (minutes):").grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
        self.max_delay_var = tk.StringVar(value=str(self.config["max_delay_minutes"]))
        max_delay_spin = ttk.Spinbox(timing_frame, from_=0, to=300, width=10, textvariable=self.max_delay_var)
        max_delay_spin.grid(row=1, column=1, sticky=tk.E, padx=(5, 0), pady=(5, 0))
        
        # Add info label about no delay
        info_label = ttk.Label(timing_frame, text="Set both to 0 for no delay between commits", 
                              font=("Arial", 8), foreground="gray")
        info_label.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(5, 0))
        
        # Work Hours
        hours_frame = ttk.LabelFrame(main_frame, text="Work Hours", padding="10")
        hours_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(hours_frame, text="Work day start (24hr format):").grid(row=0, column=0, sticky=tk.W)
        self.start_hour_var = tk.StringVar(value=str(self.config["work_hours_start"]))
        start_hour_spin = ttk.Spinbox(hours_frame, from_=0, to=23, width=10, textvariable=self.start_hour_var)
        start_hour_spin.grid(row=0, column=1, sticky=tk.E, padx=(5, 0))
        
        ttk.Label(hours_frame, text="Work day end (24hr format):").grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
        self.end_hour_var = tk.StringVar(value=str(self.config["work_hours_end"]))
        end_hour_spin = ttk.Spinbox(hours_frame, from_=0, to=23, width=10, textvariable=self.end_hour_var)
        end_hour_spin.grid(row=1, column=1, sticky=tk.E, padx=(5, 0), pady=(5, 0))
        
        # Random Timing Checkbox
        self.random_timing_var = tk.BooleanVar(value=self.config["enable_random_timing"])
        random_check = ttk.Checkbutton(hours_frame, text="Enable realistic timing distribution", 
                                     variable=self.random_timing_var)
        random_check.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(10, 0))
        
        # Custom Messages
        messages_frame = ttk.LabelFrame(main_frame, text="Custom Commit Messages", padding="10")
        messages_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(messages_frame, text="Add custom messages (one per line):").grid(row=0, column=0, sticky=tk.W)
        
        self.messages_text = scrolledtext.ScrolledText(messages_frame, width=50, height=8)
        self.messages_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # Load custom messages
        if "custom_messages" in self.config:
            self.messages_text.insert(tk.END, "\n".join(self.config["custom_messages"]))
        
        # Buttons Frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=5, column=0, columnspan=2, pady=(20, 0))
        
        # Save Config Button
        save_btn = ttk.Button(buttons_frame, text="Save Configuration", command=self.save_configuration)
        save_btn.grid(row=0, column=0, padx=(0, 10))
        
        # Test Run Button
        test_btn = ttk.Button(buttons_frame, text="Test Run (3-5 commits)", command=self.test_run)
        test_btn.grid(row=0, column=1, padx=(0, 10))
        
        # Manual Run Frame
        manual_frame = ttk.Frame(main_frame)
        manual_frame.grid(row=6, column=0, columnspan=2, pady=(10, 0))
        
        ttk.Label(manual_frame, text="Manual commit count:").grid(row=0, column=0)
        self.manual_count_var = tk.StringVar(value="10")
        manual_spin = ttk.Spinbox(manual_frame, from_=1, to=100, width=10, textvariable=self.manual_count_var)
        manual_spin.grid(row=0, column=1, padx=(5, 10))
        
        manual_btn = ttk.Button(manual_frame, text="Generate Now", command=self.manual_run)
        manual_btn.grid(row=0, column=2)
        
        # Setup Automation Frame
        setup_frame = ttk.Frame(main_frame)
        setup_frame.grid(row=7, column=0, columnspan=2, pady=(20, 0))
        
        setup_btn = ttk.Button(setup_frame, text="Setup Daily Automation (6 AM)", command=self.setup_automation)
        setup_btn.grid(row=0, column=0, padx=(0, 10))
        
        daily_btn = ttk.Button(setup_frame, text="Run Daily Commits Now", command=self.run_daily_now)
        daily_btn.grid(row=0, column=1)
        
        # Status Label
        self.status_label = ttk.Label(main_frame, text="Ready", foreground="green")
        self.status_label.grid(row=8, column=0, columnspan=2, pady=(10, 0))
        
    def save_configuration(self):
        """Save current GUI settings to config file."""
        try:
            # Update config with GUI values
            self.config["min_commits"] = int(self.min_commits_var.get())
            self.config["max_commits"] = int(self.max_commits_var.get())
            self.config["min_delay_minutes"] = int(self.min_delay_var.get())
            self.config["max_delay_minutes"] = int(self.max_delay_var.get())
            self.config["work_hours_start"] = int(self.start_hour_var.get())
            self.config["work_hours_end"] = int(self.end_hour_var.get())
            self.config["enable_random_timing"] = self.random_timing_var.get()
            
            # Get custom messages
            messages_content = self.messages_text.get(1.0, tk.END).strip()
            if messages_content:
                self.config["custom_messages"] = [msg.strip() for msg in messages_content.split("\n") if msg.strip()]
            
            # Validate settings
            if self.config["min_commits"] > self.config["max_commits"]:
                messagebox.showerror("Error", "Minimum commits cannot be greater than maximum commits")
                return
                
            if self.config["min_delay_minutes"] > self.config["max_delay_minutes"]:
                messagebox.showerror("Error", "Minimum delay cannot be greater than maximum delay")
                return
            
            # Allow 0 delay for instant commits
            if self.config["min_delay_minutes"] == 0 and self.config["max_delay_minutes"] == 0:
                messagebox.showinfo("Info", "No delay mode: Commits will be generated instantly")
                
            if self.config["work_hours_start"] >= self.config["work_hours_end"]:
                messagebox.showerror("Error", "Work start hour must be before end hour")
                return
            
            self.save_config()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields")
            
    def update_status(self, message, color="black"):
        """Update status label."""
        self.status_label.config(text=message, foreground=color)
        self.root.update()
        
    def run_command(self, command, success_msg, error_msg):
        """Run a command in a separate thread."""
        def run():
            try:
                self.update_status("Running...", "orange")
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                
                if result.returncode == 0:
                    self.update_status(success_msg, "green")
                    messagebox.showinfo("Success", success_msg)
                else:
                    self.update_status(error_msg, "red")
                    messagebox.showerror("Error", f"{error_msg}\n\nDetails: {result.stderr}")
                    
            except Exception as e:
                self.update_status("Error occurred", "red")
                messagebox.showerror("Error", f"Failed to run command: {str(e)}")
                
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()
        
    def test_run(self):
        """Run a test with 3-5 commits."""
        self.save_configuration()
        self.run_command("python auto_commit.py --test", 
                        "Test completed successfully!", 
                        "Test failed")
        
    def manual_run(self):
        """Run manual commit generation."""
        try:
            count = int(self.manual_count_var.get())
            self.run_command(f"python commit_generator.py {count}",
                           f"Generated {count} commits successfully!",
                           f"Failed to generate {count} commits")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for commit count")
            
    def run_daily_now(self):
        """Run daily automation now."""
        self.save_configuration()
        self.run_command("python auto_commit.py",
                        "Daily commits completed successfully!",
                        "Daily commits failed")
        
    def setup_automation(self):
        """Setup daily automation."""
        import platform
        
        if platform.system() == "Windows":
            self.run_command("setup_scheduler.bat",
                           "Windows Task Scheduler setup completed!",
                           "Failed to setup Windows Task Scheduler")
        else:
            self.run_command("./setup_cron.sh",
                           "Cron job setup completed!",
                           "Failed to setup cron job")

def main():
    root = tk.Tk()
    app = CommitGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()