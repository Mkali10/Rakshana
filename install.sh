#!/bin/bash

MODE="offline"

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --mode) MODE="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

echo "Starting Rakshana installation in $MODE mode..."

sudo apt update && sudo apt install -y python3 python3-pip python3-venv suricata git

# Setup Python virtual environment
python3 -m venv rakshana_env
source rakshana_env/bin/activate

pip install flask pandas scikit-learn joblib

# Create folders
mkdir -p backend/templates data models

echo "Installation complete."

if [ "$MODE" == "online" ]; then
    echo "Setting up Suricata IDS for online mode..."
    sudo systemctl enable suricata
    sudo systemctl start suricata
fi

echo "To run the admin UI:"
echo "1. Activate virtualenv: source rakshana_env/bin/activate"
echo "2. Run: python backend/app.py"
echo "3. Access UI at http://localhost:5000"
