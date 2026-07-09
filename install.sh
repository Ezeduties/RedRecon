#!/bin/bash

####################################################
# RedRecon Installer
# Version: 1.0
# Author: Jossy Jos
####################################################

echo
echo "========================================"
echo "      RedRecon Installation Script"
echo "========================================"
echo

# --------------------------------------------
# Check Python
# --------------------------------------------

echo "[*] Checking Python3..."

if ! command -v python3 &> /dev/null
then
    echo "[ERROR] Python3 is not installed."
    exit 1
fi

echo "[OK] Python3 Found."

# --------------------------------------------
# Check pip
# --------------------------------------------

echo
echo "[*] Checking pip..."

if ! command -v pip3 &> /dev/null
then
    echo "[ERROR] pip3 is not installed."
    exit 1
fi

echo "[OK] pip Found."

# --------------------------------------------
# Check Nmap
# --------------------------------------------

echo
echo "[*] Checking Nmap..."

if ! command -v nmap &> /dev/null
then
    echo "[ERROR] Nmap is not installed."
    echo "Install using:"
    echo "sudo apt install nmap"
    exit 1
fi

echo "[OK] Nmap Found."

# --------------------------------------------
# Create Virtual Environment
# --------------------------------------------

echo
echo "[*] Creating Virtual Environment..."

python3 -m venv venv

echo "[OK] Virtual Environment Created."

# --------------------------------------------
# Activate Environment
# --------------------------------------------

source venv/bin/activate

# --------------------------------------------
# Upgrade pip
# --------------------------------------------

echo
echo "[*] Upgrading pip..."

pip install --upgrade pip

# --------------------------------------------
# Install Requirements
# --------------------------------------------

echo
echo "[*] Installing Python Packages..."

pip install -r requirements.txt

# --------------------------------------------
# Create Reports Directory
# --------------------------------------------

echo
echo "[*] Creating Reports Directory..."

mkdir -p reports

echo "[OK] Reports Directory Ready."

# --------------------------------------------
# Finished
# --------------------------------------------

echo
echo "========================================"
echo "RedRecon Installed Successfully!"
echo "========================================"
echo
echo "Activate Environment:"
echo
echo "source venv/bin/activate"
echo
echo "Run:"
echo
echo "python3 redrecon.py"
echo
