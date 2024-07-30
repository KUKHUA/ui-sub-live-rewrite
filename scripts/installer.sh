#!/bin/bash

# Create the directory if it doesn't exist
mkdir -p ~/.ui-sub-live/
cd ~/.ui-sub-live/

# Clone the repository
git clone https://github.com/KUKHUA/ui-sub-live-rewrite.git

# Move the contents of the cloned repository to the current directory
mv ui-sub-live-rewrite/* .
rm -rf ui-sub-live-rewrite

# Create a python virtual environment named "ui-sub-venv"
python3 -m venv ui-sub-venv

# Activate the virtual environment
source ui-sub-venv/bin/activate

# Install the required packages
pip install -r requirements-linux.txt

# Create a desktop entry for ~/.ui-sub-live/scripts/run.sh
cat <<EOF > ~/.local/share/applications/ui-sub-live.desktop
[Desktop Entry]
Name=UI Sub Live
Comment=UI Sub Live
Exec=$HOME/.ui-sub-live/scripts/run.sh
Terminal=false
Type=Application
Categories=Utility;Application;
EOF