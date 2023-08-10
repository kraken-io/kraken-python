#!/bin/bash

# Cache clear
rm -rf ./tests/__pycache__
# Set logs dir
logsDir="/kraken/logs/$(date +"%b%d-%Y-%H-%M-%S")"
# Create logs dir
mkdir -p $logsDir
# General log
genLog="$logsDir.log"
# Activate pyenv
eval "$(pyenv init --path)"
# Set system python as current for step (2)
pyenv global system

if [ "$1" == "--colored" ] || [ "$1" == "-c" ]; then
    # Colors
    GREEN='\033[0;32m'
    RED='\033[0;31m'
    NC='\033[0m'
    LPURPLE='\033[1;35m'
else
    # No colors (default)
    GREEN=''
    RED=''
    NC=''
    LPURPLE=''
fi

FAIL="${RED}FAIL${NC}"
PASS="${GREEN}PASS${NC}"

# 1. Get python versions from pyenv
# 2. Remove '* system' line
# 3. Convert new lines to spaces
# 4. For each python versions
for version in $(pyenv versions | grep -Eiv 'system' | tr '\n' ' '); do
    # Set logfile
    logFile="$logsDir/$version.log"
    coloredLogFile="${LPURPLE}${logFile}${NC}"
    error=""

    # Set python version
    if ! pyenv global $version; then
        echo "$version -> ${FAIL}: pyenv global $version' command fail" |& tee -a $genLog
        continue
    fi

    # Manual install dependencies
    if ! python -m pip install requests pytest >> $logFile 2>&1; then
        echo "$version -> ${FAIL}: Dependencies install fail. Log: $coloredLogFile" |& tee -a $genLog
        continue
    fi

    # Install kraken package
    if ! python -m pip install -e . >> $logFile 2>&1; then
        echo "$version -> ${FAIL}: Krakenio package install fail. Log: $coloredLogFile" |& tee -a $genLog
        continue
    fi

    # Test package
    if ! python -m pytest >> $logFile 2>&1; then
        echo "$version -> ${FAIL}: Tests fail. Log: $coloredLogFile" |& tee -a $genLog
        continue
    fi

    echo "$version -> ${PASS}" |& tee -a $genLog
    rm -rf ./tests/__pycache__
done
