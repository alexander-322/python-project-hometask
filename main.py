#!/usr/bin/env python3
"""
Main entry point for the application
"""
import sys
from utils import format_output
from config import load_config

def main():
    config = load_config()
    message = "Hello from Python Team Project!"
    formatted = format_output(message, config.get('format', 'plain'))
    print(formatted)
    
if __name__ == "__main__":
    main()
