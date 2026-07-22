"""
=============================================================
validator.py

EZENOX v1.0.0
Professional Network Reconnaissance Framework

Author      : Ezeduties
Version     : 1.0.0
Python      : 3.x

Purpose:
--------
This module validates all user-supplied targets before
they are passed to the Nmap scanning engine.

Supported Targets
-----------------
• Single IPv4 Address
• Multiple IPv4 Addresses
• CIDR Networks

Examples
--------
10.0.9.5

10.0.9.5,10.0.9.6

10.0.9.0/24

Responsibilities
----------------
✓ Validate IPv4 addresses
✓ Validate CIDR networks
✓ Remove duplicate hosts
✓ Ignore invalid targets
✓ Return only valid targets

=============================================================
"""

# ============================================================
# IMPORTS
# ============================================================

import ipaddress

# ============================================================
# VALIDATE A SINGLE IPv4 ADDRESS
# ============================================================

def is_valid_ip(ip):
    """
    Determines whether a string is a valid IPv4 address.

    Parameters
    ----------
    ip : str

    Returns
    -------
    True  -> Valid IPv4
    False -> Invalid IPv4
    """

    try:
        ipaddress.IPv4Address(ip)
        return True

    except ValueError:
        return False


# ============================================================
# VALIDATE A CIDR NETWORK
# ============================================================

def is_valid_network(network):
    """
    Determines whether a string is a valid IPv4 network.

    Example

    10.0.9.0/24

    Returns
    -------
    True
    False
    """

    try:
        ipaddress.IPv4Network(network, strict=False)
        return True

    except ValueError:
        return False


# ============================================================
# REMOVE DUPLICATE HOSTS
# ============================================================

def remove_duplicates(targets):
    """
    Removes duplicate IP addresses.

    Example

    Input

    10.0.9.5
    10.0.9.5
    10.0.9.6

    Output

    10.0.9.5
    10.0.9.6
    """

    return list(dict.fromkeys(targets))


# ============================================================
# EXPAND A NETWORK INTO HOSTS
# ============================================================

def expand_network(network):
    """
    Converts

    10.0.9.0/24

    into

    10.0.9.1
    10.0.9.2
    ...
    10.0.9.254
    """

    net = ipaddress.IPv4Network(network, strict=False)

    return [str(ip) for ip in net.hosts()]


# ============================================================
# PROCESS USER INPUT
# ============================================================

def validate_targets(user_input):
    """
    Accepts user input and returns only valid hosts.

    Supported Input

    Single Host

    10.0.9.5

    Multiple Hosts

    10.0.9.5,10.0.9.6

    Network

    10.0.9.0/24
    """

    user_input = user_input.strip()

    valid_targets = []

    invalid_targets = []

    # --------------------------------------------------------
    # CIDR Network
    # --------------------------------------------------------

    if "/" in user_input:

        if is_valid_network(user_input):

            valid_targets = expand_network(user_input)

        else:

            invalid_targets.append(user_input)

    # --------------------------------------------------------
    # Multiple Hosts
    # --------------------------------------------------------

    elif "," in user_input:

        hosts = user_input.split(",")

        for host in hosts:

            host = host.strip()

            if is_valid_ip(host):

                valid_targets.append(host)

            else:

                invalid_targets.append(host)

    # --------------------------------------------------------
    # Single Host
    # --------------------------------------------------------

    else:

        if is_valid_ip(user_input):

            valid_targets.append(user_input)

        else:

            invalid_targets.append(user_input)

    valid_targets = remove_duplicates(valid_targets)
    
    return valid_targets, invalid_targets
