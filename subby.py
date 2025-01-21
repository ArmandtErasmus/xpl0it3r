# run with python
#!/usr/bin/env python3

# import libraries
import pyfiglet
import sys
import argparse
from datetime import datetime
import time
from colorama import Fore, Style, init
import requests

# initialize colorama
init(autoreset=True)

# porty art !
porty_banner = pyfiglet.figlet_format('SUBBY')
print(Fore.YELLOW + porty_banner)

# argument parser to handle command line inputs
parser = argparse.ArgumentParser(description="Subby: Enumerates subdomains for a target domain")
parser.add_argument('domain', help='Target domain (e.g., example.com)')
parser.add_argument('-w', '--wordlist', help='Path to subdomain wordlist', required=True)

# parse arguments
args = parser.parse_args()
domain = args.domain
wordlist = args.wordlist

# function to enumerate subdomains
def enumerate_subdomains(domain, wordlist):
    print(Fore.YELLOW + f"Enumerating subdomains for: {domain}")
    try:
        with open(wordlist, 'r') as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + f"Error: Wordlist file '{wordlist}' not found.")
        return

    print(Fore.CYAN + f"{'Subdomain':<30} | {'Status Code'}")
    print(Fore.CYAN + '-' * 50)

    for subdomain in subdomains:
        full_url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(full_url, timeout=3)
            print(f"{subdomain:<30} | {response.status_code}")
        except requests.ConnectionError:
            pass
        except requests.RequestException as e:
            print(Fore.RED + f"Error connecting to {full_url}: {e}")

# run subdomain enumeration

try:
    enumerate_subdomains(domain, wordlist)

except KeyboardInterrupt:
        print('\nExiting')
        sys.exit()

except requests.error as e:
        print('\nRequest Error: {e}')
        sys.exit()