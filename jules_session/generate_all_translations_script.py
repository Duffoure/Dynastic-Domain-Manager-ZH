import re
import json

# Read English lines
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# Extract key-value list
pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$')

keys_list = []
for i, line in enumerate(lines[1:], start=2):
    if not line.strip() or line.strip().startswith('#'):
        continue
    m = pattern.match(line)
    if m:
        keys_list.append((m.group(1), m.group(2), m.group(3), m.group(4)))

print(f"Total entries: {len(keys_list)}")

