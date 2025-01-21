#!/usr/bin/env python3

# Import libraries
import pyfiglet
import argparse
import sys
import socket
from datetime import datetime
import time
from colorama import Fore, Style, init
import requests

# Initialize colorama
init(autoreset=True)

# xpl0it3r banner
banner = pyfiglet.figlet_format('xpl0it3r')
print(Fore.MAGENTA + banner)
print(Fore.CYAN + "Choose your tool below:")

# Tool menu
print(Fore.YELLOW + """
[1] Porty : A port scanner
[2] Subby : A subdomain enumerator
""")

# Input for tool selection
choice = input(Fore.GREEN + "Enter your choice (1/porty or 2/subby): ").strip().lower()

if choice in ['1', 'porty']:
    # PORTY TOOL - Display usage and wait for parameters
    print(Fore.CYAN + pyfiglet.figlet_format('PORTY'))
    print(Fore.YELLOW + """
Porty: Your open-port finding friend :)

Usage:
    porty <target> [-T <intensity>] [-p <ports>]

Options:
    <target>           Target IP Address or hostname
    -T, --intensity    Scan intensity (1=slow, 5=fast) [default: 5]
    -p, --ports        Ports to scan (e.g., 22,80,1-1000) [default: 1-1000]

Example:
    porty 192.168.1.1 -T 3 -p 22,80,443
""")

    # Wait for user input to run Porty
    command = input(Fore.GREEN + "Enter your Porty command: ").strip()
    if command.startswith("porty"):
        try:
            # Parse the command
            args = command.split()
            target = args[1] if len(args) > 1 else None
            intensity = '5'
            ports = "1-1000"
            if "-T" in args:
                intensity = args[args.index("-T") + 1]
            if "-p" in args:
                ports = args[args.index("-p") + 1]

            # Intensity mapper
            intensity_map = {'5': 0.0005, '4': 0.005, '3': 0.05, '2': 0.5, '1': 1, '0': 5}

            # Parse ports
            def parse_ports(port_input):
                port_set = set()
                ranges = port_input.split(',')
                for r in ranges:
                    if '-' in r:
                        start, end = map(int, r.split('-'))
                        port_set.update(range(start, end + 1))
                    else:
                        port_set.add(int(r))
                return sorted(port_set)

            ports = parse_ports(ports)

            print(Fore.CYAN + '_' * 50)
            print(Fore.YELLOW + 'Scanning Target: ' + target)
            start_time = time.time()
            print(Fore.YELLOW + 'Scanning started at: ' + str(datetime.now().time().strftime("%H:%M")))
            print(Fore.CYAN + '_' * 50)
            print(Fore.CYAN + f'PORT\tSTATE\t\tSERVICE')
            print(Fore.CYAN + '_' * 50)

            try:
                scanned_ports = 0
                for port in ports:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(intensity_map[intensity])
                    result = s.connect_ex((target, port))
                    scanned_ports += 1
                    if result == 0:
                        try:
                            service = socket.getservbyport(port, 'tcp')
                        except OSError:
                            service = 'unknown'
                        print(f'{port}/tcp\topen\t\t{service}')
                    s.close()

                elapsed_time = time.time() - start_time
                print('_' * 50)
                print(f"Porty done: Scanned {scanned_ports} ports in {elapsed_time:.2f} seconds")

            except KeyboardInterrupt:
                print(Fore.RED + "\nPorty interrupted. Exiting...")
                sys.exit()

            except socket.error as e:
                print(f'\nHost is not responding: {e}')
                sys.exit()

        except KeyboardInterrupt:
            print(Fore.RED + "\nPorty interrupted. Exiting...")
            sys.exit()
    else:
        print(Fore.RED + "Invalid command. Please type 'porty' followed by valid arguments.")

elif choice in ['2', 'subby']:
    # SUBBY TOOL - Display usage and wait for parameters
    print(Fore.CYAN + pyfiglet.figlet_format('SUBBY'))
    print(Fore.YELLOW + """
Subby: Your subdomain enumeration friend :)

Usage:
    subby <domain> -w <wordlist>

Options:
    <domain>        Target domain (e.g., example.com)
    -w, --wordlist  Path to the subdomain wordlist

Example:
    subby example.com -w subdomains.txt
""")

    # Wait for user input to run Subby
    command = input(Fore.GREEN + "Enter your Subby command: ").strip()
    if command.startswith("subby"):
        try:
            # Parse the command
            args = command.split()
            domain = args[1] if len(args) > 1 else None
            wordlist = None
            if "-w" in args:
                wordlist = args[args.index("-w") + 1]

            # Validate inputs
            if not domain or not wordlist:
                print(Fore.RED + "Error: Missing required arguments. Use the usage instructions above.")
                sys.exit()

            # Enumerate subdomains
            print(Fore.CYAN + '_' * 50)
            print(Fore.YELLOW + f"Enumerating subdomains for: {domain}")
            print(Fore.CYAN + '_' * 50)
            try:
                with open(wordlist, 'r') as file:
                    subdomains = file.read().splitlines()
            except FileNotFoundError:
                print(Fore.RED + f"Error: Wordlist file '{wordlist}' not found.")
                sys.exit()

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
        except KeyboardInterrupt:
            print(Fore.RED + "\nSubby interrupted. Exiting...")
            sys.exit()

    else:
        print(Fore.RED + "Invalid command. Please type 'subby' followed by valid arguments.")

else:
    print(Fore.RED + "Invalid choice. Please restart and select a valid option.")
