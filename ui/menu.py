"""
=========================================================
EZENOX

Console Menu
=========================================================
"""
from rich.console import Console

console = Console()


def show_menu(stealth_mode=False):
    """
    Display the EZENOX main menu.
    """

    state = (
        "[bold green]ON[/bold green]"
        if stealth_mode
        else "[bold red]OFF[/bold red]"
    )

    console.print()

    console.print("1. Single Host Scan (IP or Domain)")
    console.print("2. Multiple Host Scan")
    console.print("3. Network Range Scan")
    console.print(f"4. Stealth Mode                     [State: {state}]")
    console.print("5. About")
    console.print("0. Exit")

    console.print()

    return console.input("[bold cyan]Select option:[/bold cyan] ").strip()
