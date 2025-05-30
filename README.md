# Threat Intelligence Feed Aggregator 🕵️‍♂️

A beginner-friendly Python tool that simulates a basic Threat Intelligence Feed Aggregator. It pulls blacklisted IPs from threat feeds, scans local log files for matches, and generates reports of suspicious activity — helping SOC teams identify potential security threats quickly.

## Features

- Loads blacklisted IP addresses from a threat feed file
- Reads local authentication logs to find IP matches
- Outputs a report of suspicious IP activity detected in logs
- Simple Python script with no external dependencies

## Why This Project?

This project helps you understand key SOC workflows, including:

- Threat intelligence feeds and indicators of compromise (IOCs)
- Log analysis and IOC matching
- Python file handling and string searching

## Project Structure
threat-intel-aggregator/
│
├── feeds/
│ └── blacklisted_ips.txt # Threat feed of blacklisted IPs
│
├── logs/
│ └── auth.log # Sample authentication log file
│
├── output/
│ └── matched_iocs.txt # Output report with matched IOCs
│
├── src/
│ └── check_iocs.py # Main Python script


## How to Run

1. Make sure you have Python 3 installed:
   ```bash
   python --version
2. Navigate to the src directory:
   ```bash
   cd src
3. Run the script:
   ```bash
   python check_iocs.py
4. Check the output file. 
