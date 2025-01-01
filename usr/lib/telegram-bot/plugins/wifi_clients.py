#!/usr/bin/env python3

import subprocess

def parse_dhcp_leases(file_path):
    try:
        with open(file_path, 'r') as file:
            leases = file.readlines()

        valid_leases = []

        for lease in leases:
            parts = lease.strip().split()
            if len(parts) >= 4:
                mac_address = parts[1].upper()
                ip_address = parts[2]
                hostname = parts[3]

                try:
                    result = subprocess.run(["ping", "-c", "1", "-W", "1", ip_address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    if result.returncode == 0:
                        valid_leases.append((hostname, ip_address, mac_address))
                except Exception as e:
                    continue

        for hostname, ip_address, mac_address in valid_leases:
            print(f"‣ {hostname}, IP: {ip_address} MAC: {mac_address}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    dhcp_leases_file = "/tmp/dhcp.leases"
    parse_dhcp_leases(dhcp_leases_file)
