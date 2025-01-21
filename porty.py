# run with python
#!/usr/bin/env python3

# import libraries
import pyfiglet
import sys
import socket
import argparse
from datetime import datetime
import time
from colorama import Fore, Style, init

# initialize colorama
init(autoreset=True)

# porty art !
porty_banner = pyfiglet.figlet_format('PORTY')
print(Fore.YELLOW + porty_banner)

# argument parser to handle command line inputs
parser = argparse.ArgumentParser(description='Porty: Your open-port finding friend :)')
parser.add_argument('target', help='Target IP Address')
parser.add_argument('-T', '--intensity', help='Specify scan intensity (e.g., 5 (fast) - 1 (slow))', default='5')
parser.add_argument('-p', '--ports', help='Specify ports (e.g., 22, 80, 5-123)', default="1-1000")

# grab and store input fields
args = parser.parse_args()
target = args.target
port_input = args.ports
intensity_input = str(args.intensity)

# intensity mapper
intensity = {
    
    '5' : 0.0005,
    '4' : 0.005,
    '3' : 0.05,
    '2' : 0.5,
    '1' : 1,
    '0' : 5
     
}

# parse the ports
def parse_ports(port_input):
    ports = set()
    ranges = port_input.split(',')
    for r in ranges:
        if '-' in r:
                start, end = map(int, r.split('-'))
                ports.update(range(start, end + 1))
        else:
                ports.add(int(r))
    return sorted(ports)

ports = parse_ports(port_input)

# aesthetics and time info
print(Fore.CYAN + '_' * 50)
print(Fore.YELLOW + 'Scanning Target: ' + target)
start_time = time.time()
print(Fore.YELLOW + 'Scanning started at: ' + str(datetime.now().time().strftime("%H:%M")))
print(Fore.CYAN + '_' * 50)
print(Fore.CYAN + f'PORT\tSTATE\t\tSERVICE')
print(Fore.CYAN + '_' * 50)

# scan for open ports
try:
    # count port scans
    scanned_ports = 0

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(intensity[intensity_input])
    # return open ports
        result = s.connect_ex((target, port))
        scanned_ports += 1
        if result == 0:
            try:
                service = socket.getservbyport(port, 'tcp')
            except OSError:
                service = 'unknown'
            print(f'{port}/tcp\topen\t\t{service}')
        s.close()

    # Summary after scanning
    elapsed_time = time.time() - start_time
    print('_' * 50)
    print(f"Porty done: Scanned {scanned_ports} ports in {elapsed_time:.2f} seconds")

except KeyboardInterrupt:
        print('\nExiting')
        sys.exit()

except socket.error as e:
        print('\nHost is not responding: {e}')
        sys.exit()