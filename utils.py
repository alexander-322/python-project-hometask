"""
Utility functions
"""
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
