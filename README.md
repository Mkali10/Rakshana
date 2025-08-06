# Rakshana - AI-Powered Cyber Wall

## Overview
Rakshana is an AI-powered cybersecurity platform combining network IDS, AI threat detection, SIEM logging, and a secure admin dashboard.

## Features
- AI-based anomaly detection with Isolation Forest  
- Multi-layer security: authentication, rate limiting, encrypted models  
- Unique watermark embedded for ownership protection  
- Installer script for easy setup on Ubuntu 22.04  
- Flask-based admin UI with secure login  

## Installation

### Requirements
- Ubuntu 22.04 or compatible Linux  
- Python 3.8+  
- Minimum 4 CPU cores, 8GB RAM, 100GB storage  

### Automatic Setup (Online Mode)
# Step 1: Clone the repo
git clone https://github.com/Mkali10/Rakshana.git
cd Rakshana
# Step 2: Make the script executable
chmod +x install.sh
# Step 3: Run installer in online mode
sudo ./install.sh --mode online

### This will:
Install all required packages (Python, NGINX, Certbot)
Set up virtual environment and install Python dependencies
Create systemd service for Rakshana backend
Set up NGINX reverse proxy
Optionally set up SSL with Let's Encrypt
Enable the Rakshana service to start on boot

### Option 2: Manual Setup

# Step 1: Clone the repository
git clone https://github.com/Mkali10/Rakshana.git
cd Rakshana

# Step 2: Create a virtual environment
python3 -m venv env
source env/bin/activate

# Step 3: Install Python dependencies
pip install -r requirements.txt
# Or manually:
pip install flask pandas scikit-learn joblib

# Step 4: Train the AI model
python offline_ai_detection.py train data/train_logs.csv

# Step 5: Start the backend
python backend/app.py


Access in browser:
👉 http://localhost:5000

Login credentials:

Username: admin

Password: ChangeThisStrongPassword!


