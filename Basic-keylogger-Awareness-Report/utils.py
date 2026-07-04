"""Helper functions for rendering UI components, clearing the screen, and saving outputs."""

import os
import json
from typing import Dict, Any, List
from tabulate import tabulate
from colorama import init, Fore, Style

# Initialize colorama for cross-platform color support
init(autoreset=True)

def clear_screen() -> None:
    """Clears the terminal screen securely based on the host OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_print(text: str, level: str = "INFO") -> None:
    """Prints text with corresponding Colorama formatting based on severity levels."""
    mapping = {
        "HEADER": Fore.MAGENTA + Style.BRIGHT,
        "INFO": Fore.BLUE + Style.BRIGHT,
        "SUCCESS": Fore.GREEN + Style.BRIGHT,
        "WARNING": Fore.YELLOW + Style.BRIGHT,
        "FAIL": Fore.RED + Style.BRIGHT,
    }
    color = mapping.get(level.upper(), Fore.WHITE)
    print(f"{color}{text}{Style.RESET_ALL}")

def print_banner(title: str) -> None:
    """Renders a standard structured visual header banner for the interactive CLI."""
    print("=" * 60)
    colored_print(f" {title} ", "HEADER")
    print("=" * 60)

def format_table(data: List[List[Any]], headers: List[str]) -> str:
    """Formats tabular datasets neatly using the tabulate processing engine."""
    return tabulate(data, headers=headers, tablefmt="grid")

def save_json(filepath: str, data: Dict[str, Any]) -> bool:
    """Safely serializes and records a data structure into a formatted JSON document."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError as e:
        colored_print(f"File System Write Exception: {e}", "FAIL")
        return False

def export_text(filepath: str, content: str) -> bool:
    """Safely records standard string outputs into a human-readable text file."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except IOError as e:
        colored_print(f"File System Write Exception: {e}", "FAIL")
        return False