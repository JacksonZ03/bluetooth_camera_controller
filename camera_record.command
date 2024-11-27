#!/bin/bash
# This script is used as a wrapper to run the camera_record.py script so that the Terminal window auto closes

# Get the terminal window ID
TERMINAL_WINDOW_ID=$(osascript -e 'tell application "Terminal" to id of front window')

set -e # Exit if anything fails

# Change working directory to the directory where the script is located
cd "$(dirname "$0")"

./camera-record

# Close the Terminal after pressing Enter
osascript -e "tell application \"Terminal\" to close (every window whose id is $TERMINAL_WINDOW_ID)" & exit 0