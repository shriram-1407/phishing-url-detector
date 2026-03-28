# phishing-url-detector
A Python tool to detect phishing URLs using basic security checks

# Phishing URL Detection System

## Description
This project is a Python-based tool that checks whether a given URL could be a phishing link or not. It uses simple rules to identify patterns commonly found in malicious or fake websites.

## Features
- Checks for HTTP vs HTTPS
- Looks for suspicious keywords like "login", "verify", "bank"
- looks for special characters
- Checks the length of URL
- Detects unusual URL structures
- Logs the analyzed URLs and their results for reference

## Technologies Used
- Python

## How to Run
1. Download the file
2. Run the script:
   python main.py

## Example Output
Enter URL: example-login.xyz  
Warning: This URL may be a phishing site

## What I Learned
- Basic understanding of phishing attacks  
- How URLs can be used to mislead users  
- Implementing simple detection logic in Python  
