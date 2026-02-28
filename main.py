#!/usr/bin/env python3
"""
Main entry point for the application
"""
import click
from utils import format_output
from config import load_config

@click.command()
@click.option('--name', '-n', default='World', help='Name to greet')
@click.option('--format', '-f', type=click.Choice(['plain', 'uppercase', 'lowercase', 'title'], case_sensitive=False))
def main(name, format):
    """Simple CLI program that greets NAME."""
    config = load_config()
    if format:
        config['format'] = format
    message = f"Hello, {name}!"
    formatted = format_output(message, config.get('format', 'plain'))
    print(formatted)
    
if __name__ == "__main__":
    main(
