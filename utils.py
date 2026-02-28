"""
Utility functions
"""
from rich.console import Console
from rich.table import Table

console = Console()

def format_output(text, format_type='plain'):
    if format_type == 'uppercase':
        return text.upper()
    elif format_type == 'lowercase':
        return text.lower()
    elif format_type == 'title':
        return text.title()
    else:
        return text

def calculate_sum(a, b):
    return a + b

def print_table(data):
    """Print data as a rich table"""
    table = Table(title="Data Table")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="magenta")
    
    for key, value in data.items():
        table.add_row(str(key), str(value))
    
    console.print(table)

def print_success(message):
    """Print success message in green"""
    console.print(f"✅ {message}", style="green")

def print_error(message):
    """Print error message in red"""
    console.print(f"❌ {message}", style="red")
