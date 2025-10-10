#!/bin/bash
# Setup cron job for daily commits at 6 AM
# Usage: ./setup_cron.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/auto_commit.py"

echo "Setting up cron job for daily GitHub commits..."
echo "Script location: $PYTHON_SCRIPT"

# Create cron job entry
CRON_ENTRY="0 6 * * * cd $SCRIPT_DIR && /usr/bin/python3 auto_commit.py >> daily_commit_log.txt 2>&1"

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "auto_commit.py"; then
    echo "⚠️  Cron job already exists. Removing old entry..."
    crontab -l 2>/dev/null | grep -v "auto_commit.py" | crontab -
fi

# Add new cron job
(crontab -l 2>/dev/null; echo "$CRON_ENTRY") | crontab -

if [ $? -eq 0 ]; then
    echo "✅ Successfully created cron job!"
    echo "⏰ Task will run daily at 6:00 AM"
    echo "📁 Working directory: $SCRIPT_DIR"
    echo ""
    echo "To verify the cron job:"
    echo "crontab -l | grep auto_commit"
    echo ""
    echo "To remove the cron job later:"
    echo "crontab -l | grep -v auto_commit.py | crontab -"
    echo ""
    echo "To view logs:"
    echo "tail -f $SCRIPT_DIR/daily_commit_log.txt"
else
    echo "❌ Failed to create cron job"
fi