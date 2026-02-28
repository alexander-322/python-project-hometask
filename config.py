"""
Configuration module
"""
import json
import os

def load_config():
    """Load configuration with enhanced options"""
    config = {
        'app_name': 'Python Team Project',
        'version': '1.0.0',
        'format': 'plain',
        'debug': False,
        'theme': 'dark',
        'language': 'en',
        'max_items': 100
    }
    
    # Попробуем загрузить из файла, если существует
    if os.path.exists('config.json'):
        try:
            with open('config.json', 'r') as f:
                file_config = json.load(f)
                config.update(file_config)
        except:
            pass
    
    return config

def update_config(key, value):
    """Update configuration value"""
    config = load_config()
    config[key] = value
    return config

def save_config(config):
    """Save configuration to file"""
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)
