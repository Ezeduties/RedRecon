"""
=========================================================
EZENOX Utility Module

Common helper functions used throughout the framework.

Author : Ezeduties
Version: 1.0
=========================================================
"""

# -----------------------------
# Standard Library Imports
# -----------------------------
from datetime import datetime
from pathlib import Path

# --------------------------------------------------------
# Print a horizontal separator line
# --------------------------------------------------------

def print_line(length=60):
    """
    Print a horizontal separator line.

    Parameters:
        length (int): Number of '=' characters.
    """

    print("=" * length)

# --------------------------------------------------------
# Get Current Date
# --------------------------------------------------------

def get_current_date():
    """
    Returns today's date.

    Example:
        08-07-2026
    """

    return datetime.now().strftime("%d-%m-%Y")


# --------------------------------------------------------
# Get Current Time
# --------------------------------------------------------

def get_current_time():
    """
    Returns the current time.

    Example:
        16:45:31
    """

    return datetime.now().strftime("%H:%M:%S")


# --------------------------------------------------------
# Get Timestamp
# --------------------------------------------------------

def get_timestamp():
    """
    Returns a filename-safe timestamp.

    Example:
        20260708_164531
    """

    return datetime.now().strftime("%Y%m%d_%H%M%S")

# --------------------------------------------------------
# Create Reports Directory
# --------------------------------------------------------

def create_reports_directory():
    """
    Create the reports directory if it does not exist.

    Returns:
        Path object pointing to the reports directory.
    """

    reports_dir = Path("reports", "scan_reports")

    reports_dir.mkdir(exist_ok=True)

    return reports_dir

# --------------------------------------------------------
# Save Text File
# --------------------------------------------------------

def save_text_file(filename, content):
    """
    Save text content to a file inside the reports directory.

    Parameters:
        filename (str): Name of the file.
        content (str): Text to write.

    Returns:
        Path object of the saved file.
    """

    reports_dir = create_reports_directory()

    file_path = reports_dir / filename

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return file_path
