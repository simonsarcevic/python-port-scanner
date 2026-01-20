#!/usr/bin/env python3
import platform
import sys
import socket
import subprocess
import argparse
from datetime import datetime

def get_local_info():
    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    platform_info = platform.platform()
    
    print('*------------------------------------------*')
    print('          LOCALE SYSTEM')
    print('*------------------------------------------*')
    print('')
    print(f'OS Name: {os_name}')
    print(f'OS Release: {os_release}')
    print(f'OS Version: {os_version}')
    print(f'Platform Info: {platform_info}')
    print('')
    print('*------------------------------------------*\n')

def scan_target(target_ip):
    print(f'*------------------------------------------*')
    print('')
    print(f'          TARGET SCAN: {target_ip}')
    print(f'          Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('')
    print('*------------------------------------------*')
    
    try:
        common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 1723, 3389, 5900, 8080]
        open_ports = []
        
        print("TCP Port Scan (Common Ports)...")
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
                service = identify_service(target_ip, port)
                print(f"  PORT {port}/tcp open  {service}")
            sock.close()
        
        if not open_ports:
            print("  No open ports found")
        
        print("\nHostname Resolution...")
        try:
            hostname = socket.gethostbyaddr(target_ip)[0]
            print(f"  Hostname: {hostname}")
        except:
            print("  Cannot reach hostname")
        
        print("\nNmap Scan...")
        try:
            result = subprocess.run(['nmap', '-sV', '-sC', target_ip], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print("NMAP OUTPUT:")
                print(result.stdout)
            else:
                print("Nmap not available")
        except:
            print("Nmap not installed")
        
        if 445 in open_ports:
            print("\nSMB Enumeration...")
            enum_smb(target_ip)
        
    except KeyboardInterrupt:
        print("\n[!] Scan canceled")
    except Exception as e:
        print(f"[!] Scan error: {e}")

def identify_service(ip, port):
    services = {
        21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp",
        53: "domain", 80: "http", 110: "pop3", 135: "msrpc",
        139: "netbios-ssn", 443: "https", 445: "microsoft-ds",
        3389: "ms-wbt-server", 8080: "http-proxy"
    }
    return services.get(port, "unknown")

def enum_smb(target_ip):
    try:
        print("  Null Session SMB Enum...")
        result = subprocess.run(['smbclient', '-L', target_ip, '-N'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print("  SMB Null Session failed")
    except:
        print("  smbclient not available")

def main():
    parser = argparse.ArgumentParser(description='System Scanner')
    parser.add_argument(
        'target',
        nargs='?',
        help='Target IP/Hostname (optional if --local is used)'
    )
    parser.add_argument(
        '-l', '--local',
        action='store_true',
        help='Show local system info'
    )

    args = parser.parse_args()

    if args.local and not args.target:
        get_local_info()
        return

    if not args.target:
        parser.print_help()
        print("\nExamples:")
        print("  python3 os_scanner.py -l")
        print("  python3 os_scanner.py 192.168.0.12")
        print("  python3 os_scanner.py 192.168.0.12 -l")
        return

    if args.local:
        get_local_info()

    scan_target(args.target)


if __name__ == "__main__":
    main()
