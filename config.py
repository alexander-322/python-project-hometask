"""
Configuration module
"""
def load_config():
    return {
        'app_name': 'Python Team Project',
        'version': '1.0.0',
        'format': 'plain'
    }

def update_config(key, value):
    config = load_config()
    config[key] = value
    return config
