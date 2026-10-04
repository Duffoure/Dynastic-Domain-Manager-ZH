import re
import json

# Read english file
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# Extract all keys and english strings
pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$')

items = []
for line in lines[1:]:
    if not line.strip() or line.strip().startswith('#'):
        continue
    m = pattern.match(line)
    if m:
        items.append((m.group(1), m.group(2), m.group(3), m.group(4)))

print(f"Items to translate: {len(items)}")

