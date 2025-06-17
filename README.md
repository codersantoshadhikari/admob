#!/bin/bash

# Configuration
REPO_DIR="/path/to/your/repo"  # Change this
INTERVAL_MINUTES=20

cd "$REPO_DIR" || exit 1

while true; do
    # Run your system
    echo "System running at $(date)" >> system.log
    
    # Example command (replace with your actual system):
    # python your_script.py >> output.log 2>&1
    
    # Git operations
    git add .
    git commit -m "Auto-commit: $(date +'%Y-%m-%d %H:%M:%S')"
    git push origin main
    
    # Wait for next interval
    sleep $((INTERVAL_MINUTES * 60))
done
