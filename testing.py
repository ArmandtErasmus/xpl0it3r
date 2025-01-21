def run_test():
    import os

    print("\n--- xpl0it3r Testing ---\n")

    print("Run xpl0it3r")
    os.system('python xpl0it3r.py')

    print("\nTest Porty - Single IP Scan")
    os.system('porty 192.168.1.1 -T 3 -p 22,80,443')

    print("\nTest Porty - Range Scan")
    os.system('porty 192.168.1.1 -T 2 -p 1-1000')

    print("\nTest Subby - Single Domain")
    os.system('subby example.com -w Subdomains.txt')

    print("\nTest Subby - Custom Wordlist")
    os.system('subby example.com -w custom_wordlist.txt')

    print("\nTest Error Handling - Invalid IP")
    os.system('porty 999.999.999.999 -T 3 -p 22,80')

    print("\nKeyboard Interrupt (Ctrl+C)")
    try:
        os.system('porty 192.168.1.1 -T 1 -p 1-65535')
    except KeyboardInterrupt:
        print("\nCaught KeyboardInterrupt")

    print("\n--- Testing Completed ---\n")

if __name__ == "__main__":
    run_test()
