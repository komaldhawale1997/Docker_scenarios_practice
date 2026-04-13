import json

with open('/config/settings.json') as f:
    data = json.load(f)

print("Config loaded:", data)
