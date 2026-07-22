"""
=========================================================
EZENOX

Professional Network Reconnaissance &
Vulnerability Assessment Framework

Main Entry Point

Author : Ezeduties
=========================================================
"""

from core.scanner import CoreScanner
from ui.banner import print_banner
from ui.menu import show_menu
from version import (
    APP_NAME,
    VERSION,
    AUTHOR,
    DESCRIPTION,
)


def about():
    """
    Display application information.
    """

    print()
    print("=" * 70)
    print(APP_NAME)
    print("=" * 70)
    print(DESCRIPTION)
    print()
    print(f"Version : {VERSION}")
    print(f"Author  : {AUTHOR}")

    print()
    print("Features")
    print("-" * 70)

    features = [
        "Service Discovery",
        "Banner Collection",
        "Fingerprinting",
        "Vendor Detection",
        "CPE Generation",
        "Confidence Scoring",
        "NVD Vulnerability Lookup",
        "TXT Reports",
        "HTML Reports",
        "JSON Reports",
        "CSV Reports",
    ]

    for feature in features:
        print(f"✓ {feature}")

    print("=" * 70)
    print()


def single_host_scan(stealth_mode):
    """
    Execute a single host scan.
    """

    target = input("\nTarget (IP or Domain): ").strip()

    if not target:
        print("No target supplied.")
        input("\nPress Enter to return to the Main Menu...")
        return

    scanner = CoreScanner()

    scanner.run(
        target,
        stealth=stealth_mode
    )

    input("\nPress Enter to return to the Main Menu...")


def main():

    stealth_mode = False

    while True:

        print_banner()

        choice = show_menu(stealth_mode)

        if choice == "1":

            single_host_scan(stealth_mode)
            print()
            print("=" * 70)
            print("SCAN COMPLETE")
            print("=" * 70)
            input("\nPress Enter to return to the main Menu...")

        elif choice == "2":

            print("\nMultiple Host Scan")
            print("Coming in EZENOX v1.4.0\n")

            input("Press Enter to continue...")

        elif choice == "3":

            print("\nNetwork Range Scan")
            print("Coming in EZENOX v1.4.0\n")

            input("Press Enter to continue...")

        elif choice == "4":

            stealth_mode = not stealth_mode

            if stealth_mode:

                print("\n[+] Stealth Mode Enabled")
                print("Stealth engine will be available in EZENOX v1.4.0\n")

            else:

                print("\n[-] Stealth Mode Disabled\n")

            input("Press Enter to continue...")

        elif choice == "5":

            about()

            input("Press Enter to continue...")

        elif choice == "0":

            print("\nThank you for using EZENOX.\n")

            break

        else:

            print("\nInvalid option.\n")

            input("Press Enter to continue...")


if __name__ == "__main__":

    main()
