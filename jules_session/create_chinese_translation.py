import re
import sys

# Read English file
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    english_lines = f.readlines()

# Extract keys and values
pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$')

items = []
for line in english_lines[1:]:
    if not line.strip() or line.strip().startswith('#'):
        continue
    m = pattern.match(line)
    if m:
        items.append((m.group(1), m.group(2), m.group(3), m.group(4)))

print(f"Total entries: {len(items)}")
