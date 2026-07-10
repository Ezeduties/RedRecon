"""
===========================================================
RedRecon v1.0

Professional Network Reconnaissance Framework

Author:
Ezeduties

===========================================================
"""

import os

import time
from banner import print_banner
from banner import success
from banner import warning
from banner import error

from validator import (
    is_valid_ip,
    validate_targets,
    is_valid_network,
    expand_network,
)

from scanner import Scanner
from reports import ReportGenerator

# ---------------------------------------------------------
# Clear Screen
# ---------------------------------------------------------

def clear_screen():
    """
    Clear the terminal screen.
    """

    os.system("clear")


# ---------------------------------------------------------
# About
# ---------------------------------------------------------

def about():
    """
    Display information about RedRecon.
    """

    print("\n")
    print("=" * 60)
    print("ABOUT REDRECON")
    print("=" * 60)

    print("Version : 1.0")
    print("Author  : Ezeduties")
    print("GitHub  : https://github.com/Ezeduties")
    print()

    print("Professional Network Reconnaissance Framework")
    print("Built with Python for Cybersecurity Learning.")
    print()

    input("Press ENTER to return to the menu...")

# ---------------------------------------------------------
# Scan Single Host
# ---------------------------------------------------------

def scan_single_host():
    """
    Scan a single target host.
    """

    clear_screen()
    print_banner()

    print("\nSingle Host Scan\n")

    target = input("Enter Target IP Address: ").strip()


    if not is_valid_ip(target):

        error("Invalid IP Address.")

        input("\nPress ENTER to continue...")

        return

    success("Target validated.")

    print("\nScanning... Please wait...\n")

    scanner = Scanner()

    results = scanner.scan_host(target)

    report = ReportGenerator(results)

    reports = report.export_all()

    success("Scan Completed.")

    print()

    print("=" * 60)
    print("REPORTS GENERATED")
    print("=" * 60)

    print(f"CSV  : {reports['csv']}")
    print(f"JSON : {reports['json']}")
    print(f"TXT  : {reports['txt']}")

    print("=" * 60)

    input("\nPress ENTER to return to the menu...")

# ---------------------------------------------------------
# Multiple Host Scan
# ---------------------------------------------------------

def scan_multiple_hosts():
    """
    Scan multiple hosts entered by the user.
    """

    clear_screen()

    print_banner()

    print("\n" + "=" * 60)
    print("MULTIPLE HOST SCAN")
    print("=" * 60)

    user_input = input(
        "\nEnter IP addresses separated by commas:\n\n> "
    ).strip()

    valid_targets, invalid_targets = validate_targets(user_input)

    # ------------------------------------------------
    # Display invalid targets
    # ------------------------------------------------

    if invalid_targets:

        warning("\nInvalid Targets:")

        for target in invalid_targets:

            print(f"   - {target}")

    # ------------------------------------------------
    # Ensure we have valid targets
    # ------------------------------------------------

    if not valid_targets:

        error("\nNo valid targets to scan.")

        input("\nPress ENTER to return...")

        return

    success(f"\n{len(valid_targets)} valid target(s) found.")

    scanner = Scanner()

    all_results = []

    hosts_up = 0

    hosts_down = 0

    print()

    # ------------------------------------------------
    # Scan each target
    # ------------------------------------------------

    for index, target in enumerate(valid_targets, start=1):

        print(f"[{index}/{len(valid_targets)}] Scanning {target}...")

        try:

            result = scanner.scan_host(target)

            all_results.append(result)

            if result.get("state") == "up":

                hosts_up += 1

            else:

                hosts_down += 1

        except Exception as e:

            error(f"Failed to scan {target}")

            print(e)

            hosts_down += 1

    success("\nMultiple host scan completed.")

    # ------------------------------------------------
    # Generate Reports
    # ------------------------------------------------

    report = ReportGenerator(all_results)

    reports = report.export_all()

    # ------------------------------------------------
    # Scan Summary
    # ------------------------------------------------

    print("\n" + "=" * 60)
    print("SCAN SUMMARY")
    print("=" * 60)

    print(f"Hosts Scanned : {len(valid_targets)}")
    print(f"Hosts Up      : {hosts_up}")
    print(f"Hosts Down    : {hosts_down}")

    print("\nREPORTS GENERATED")
    print("-" * 60)

    print(f"CSV  : {reports['csv']}")
    print(f"JSON : {reports['json']}")
    print(f"TXT  : {reports['txt']}")

    print("=" * 60)

    input("\nPress ENTER to return to the menu...")

# ---------------------------------------------------------
# Display Menu
# ---------------------------------------------------------

def scan_network_range():
    """
    Scan every host inside a network range.
    """

    clear_screen()

    print_banner()

    print("\n" + "=" * 60)
    print("NETWORK RANGE SCAN")
    print("=" * 60)

    network = input(
        "\nEnter Network (Example: 10.0.9.0/24)\n\n> "
    ).strip()

    # ---------------------------------------------
    # Validate Network
    # ---------------------------------------------

    if not is_valid_network(network):

        error("\nInvalid network.")

        input("\nPress ENTER to return...")

        return

    hosts = expand_network(network)

    success("\nNetwork validated.")

    print()

    print("=" * 60)
    print("NETWORK INFORMATION")
    print("=" * 60)

    print(f"Network      : {network}")
    print(f"Total Hosts  : {len(hosts)}")

    start_time = time.time()

    scanner = Scanner()

    all_results = []

    hosts_up = 0

    hosts_down = 0

    print("\nStarting scan...\n")

    for index, host in enumerate(hosts, start=1):

        print(f"[{index}/{len(hosts)}] Scanning {host}...")

        try:

            result = scanner.scan_host(host)

            all_results.append(result)

            if result.get("state") == "up":

                hosts_up += 1

            else:

                hosts_down += 1

        except Exception as e:

            error(f"Failed to scan {host}")

            print(e)

            hosts_down += 1

    success("\nNetwork scan completed.")

    elapsed_time = time.time() - start_time

    report = ReportGenerator(all_results)

    reports = report.export_all()

    print("\n" + "=" * 60)
    print("NETWORK RANGE SUMMARY")
    print("=" * 60)

    print(f"Network       : {network}")
    print(f"Hosts Total   : {len(hosts)}")
    print(f"Hosts Up      : {hosts_up}")
    print(f"Hosts Down    : {hosts_down}")
    print(f"Elapsed Time  : {elapsed_time:.2f} seconds")

    print("\nREPORTS GENERATED")
    print("-" * 60)

    print(f"CSV  : {reports['csv']}")
    print(f"JSON : {reports['json']}")
    print(f"TXT  : {reports['txt']}")

    print("=" * 60)

    input("\nPress ENTER to return to the menu...")

def display_menu():
    """
    Display the main menu.
    """

    print("\n")
    print("=" * 60)
    print("REDRECON MAIN MENU")
    print("=" * 60)

    print("1. Scan Single Host")
    print("2. Scan Multiple Hosts")
    print("3. Scan Network Range")
    print("4. About")
    print("5. Exit")

    print("=" * 60)

    return input("Select an option: ")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    while True:

        clear_screen()

        print_banner()

        choice = display_menu()

        if choice == "1":

            scan_single_host()

        elif choice == "2":

            scan_multiple_hosts()

        elif choice == "3":

            scan_network_range()

        elif choice == "4":

            clear_screen()

            print_banner()

            about()

        elif choice == "5":

            print("\nThank you for using RedRecon.")
            print("Goodbye.\n")

            break

        else:

            print("\nInvalid option.")

            input("Press ENTER to continue...")


# ---------------------------------------------------------
# Program Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:

        print("\n")
        print("=" * 60)
        print("Interrupted by user.")
        print("Thank you for using RedRecon.")
        print("=" * 60)

    except Exception as error:

        print("\n")
        print("=" * 60)
        print("Unexpected Error")
        print("=" * 60)
        print(error)
