"""
============================================================
banner.py

RedRecon v1.0.0
Professional Network Reconnaissance Framework

Author      : Ezeduties
Version     : 1.0.0
Python      : 3.x

This module is responsible for:

• Initializing terminal colors
• Printing the application banner
• Displaying colored status messages

Nothing related to scanning should exist here.
============================================================
"""
from datetime import datetime
from colorama import Fore, Style, init

# ----------------------------------------------------------
# Initialize Colorama
#
# autoreset=True automatically resets the terminal color
# after every print() call.
# ----------------------------------------------------------

init(autoreset=True)

# ----------------------------------------------------------
# Version Information
# ----------------------------------------------------------

VERSION = "1.0"

AUTHOR = "Ezeduties"

# ----------------------------------------------------------
# Banner
# ----------------------------------------------------------

TODAY = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")

def print_banner():

    print(Fore.RED + r"""
██████╗ ███████╗██████╗ ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║  ██║██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║  ██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║  ██║███████╗██████╔╝██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
""")

    print(
        Fore.CYAN +
        "Professional Network Reconnaissance Framework"
    )

    print(
        Fore.YELLOW +
        f"Version {VERSION}"
    )

    print(
        Fore.GREEN +
        f"Author : {AUTHOR}"
    )

    print(
        Fore.MAGENTA +
        f"Date   : {TODAY}"
    )

    print(Fore.BLUE + "=" * 65)


# ----------------------------------------------------------
# Status Messages
#
# These helper functions allow every module to print
# standardized messages.
# ----------------------------------------------------------

def info(message):

    print(Fore.CYAN + "[*] " + message)


def success(message):

    print(Fore.GREEN + "[+] " + message)


def warning(message):

    print(Fore.YELLOW + "[!] " + message)


def error(message):

    print(Fore.RED + "[-] " + message)
