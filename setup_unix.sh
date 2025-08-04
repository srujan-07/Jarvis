#!/bin/bash

# Jarvis Quick Setup Script for Linux/Mac
# Getting Started in Under 5 Minutes

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "==============================================================================="
echo "                      JARVIS - Linux/Mac Quick Setup"
echo "                     Getting Started in Under 5 Minutes"
echo "==============================================================================="
echo -e "${NC}"

# Check Python installation
echo -e "${YELLOW}Checking Python installation...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR] Python 3 is not installed!${NC}"
    echo "Please install Python 3.8+ from: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo -e "${GREEN}[OK] Python $PYTHON_VERSION found!${NC}"

# Check if we're in the right directory
if [ ! -f "Jarvismain.py" ]; then
    echo -e "${RED}[ERROR] Please run this script from the Jarvis directory!${NC}"
    exit 1
fi

echo
echo -e "${YELLOW}Running Jarvis setup...${NC}"
python3 quick_setup.py

echo
echo -e "${GREEN}"
echo "==============================================================================="
echo "Setup complete!"
echo
echo "To start Jarvis, run:"
echo "    python3 Jarvismain.py"
echo
echo "Say 'Wake up' to activate your assistant!"
echo "==============================================================================="
echo -e "${NC}"
