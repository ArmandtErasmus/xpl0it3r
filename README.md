# xpl0it3r: A Comprehensive Guide
xpl0it3r is a multi-purpose CLI tool that is used for port scanning and subdomain enumeration.

### Table of Contents
1. [Introduction](#1.-Introduction)
2. [Features](#2.-Features)
3. [Installation](#3.-Installation)
4. [Usage](#4.-Usage)
5. [Arguments and Options](#5.Arguments-and-Options)
6. [Contributing](#6.Contributing)
7. [License](#7.License)

### 1. Introduction

xpl0it3r is a comprehensive multi-purpose CLI (Command Line Interface) tool designed for cybersecurity enthusiasts and professionals. It combines functionalities of port scanning (Porty) and subdomain enumeration (Subby) into a unified interface, offering seamless interaction and flexibility.

This tool is built in Python and utilizes various libraries such as pyfiglet, colorama, and requests. It provides a simple and intuitive way to perform security assessments by scanning ports and discovering subdomains for a target.

### 2. Features

- Port Scanner (Porty):
  - Scan a range or specific ports for open services.
  - Customize scan intensity (speed) from 1 (slow) to 5 (fast).
    
- Subdomain Enumerator (Subby):
  - Enumerate subdomains for a given domain using a wordlist.
  - Fetch HTTP status codes for discovered subdomains.
 
### 3. Installation

To install the xpl0it3r tool, follow these steps:

#### Prerequisites
Ensure you have the following installed on your system:

- Python 3/above
- colorama
- pyfiglet
- requests

OR install them by copying and pasting the command below into your terminal:
```
pip install colorama pyfiglet requests
```
#### Step-by-Step Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/xpl0it3r
   cd xpl0it3r
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### 4. Usage

After installation, you can run the tool using:
    ```
    python xpl0it3r.py
    ```
You will be greeted with a tool menu that allows you to choose between Porty and Subby functionalities.  

### 5. Arguments and Options

Once xpl0it3r is running you can choose between Porty and Subby by entering a 1 or a 2, or the respective tool name.

#### 5.1 Port Scanner (Porty)
To use Porty, you can pass the following options:

porty <target> <parameters>

   - Target: target IP address or hostname (required)
   - Intensity: -T or --intensity (default: 5, range: 0 to 5; 5 is the fastest)
   - Ports: -p or --ports (default 1-1000)

Example command:
  ```
  porty 192.168.1.1 -T 3 -p 22,80,443
  ```

#### 5.2 Subdomain Enumerator (Subby)
To use Subby, you can pass the following options:

subby <domain> <parameters>

  - Domain: domain (e.g., example.com)
  - Wordlist: -w or --wordlist (path to wordlist file)

Example command:
  ```
  subby example.com -w /path/to/file/subdomains.txt
  ```
### 6. Contributing
Contributions to xpl0it3r are welcome! If you encounter bugs or would like to add new features, please feel free to submit issues or pull requests.

#### Steps to contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make changes and commit (git commit -m 'Add some feature').
4. Push changes (git push origin feature-branch).
5. Submit a pull request.

### 7. License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/ArmandtErasmus/xpl0it3r/blob/main/LICENSE) file for more details.
