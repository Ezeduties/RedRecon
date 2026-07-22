"""
=========================================================
EZENOX

Professional Console Banner

Author : Ezeduties
=========================================================
"""

from rich.console import Console

from version import (
    APP_NAME,
    VERSION,
    AUTHOR,
    DESCRIPTION,
)

console = Console()


def print_banner():
    """
    Display the EZENOX application banner.
    """

    console.print("[bold red]" + "=" * 70 + "[/bold red]")

    console.print(
        r"""
███████╗███████╗███████╗███╗   ██╗ ██████╗ ██╗  ██╗
██╔════╝╚══███╔╝██╔════╝████╗  ██║██╔═══██╗╚██╗██╔╝
█████╗    ███╔╝ █████╗  ██╔██╗ ██║██║   ██║ ╚███╔╝
██╔══╝   ███╔╝  ██╔══╝  ██║╚██╗██║██║   ██║ ██╔██╗
███████╗███████╗███████╗██║ ╚████║╚██████╔╝██╔╝ ██╗
╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
""",
        style="bold red",
    )

    console.print(f"[bold bright_green]{APP_NAME}[/bold bright_green]")
    console.print(f"[bold bright_white]{DESCRIPTION}[/bold bright_white]")
    console.print()

    console.print(
        f"[bold cyan]Version :[/bold cyan] [bold bright_white]{VERSION}[/bold bright_white]"
    )

    console.print(
        f"[bold green]Author  :[/bold green] [bold bright_white]{AUTHOR}[/bold bright_white]"
    )

    console.print("[bold red]" + "=" * 70 + "[/bold red]")
    console.print()
