import re
import sys

# Read English file
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    english_content = f.read()

english_lines = english_content.splitlines()

# Extract all keys and their English values
key_pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$')

english_keys = []
for line in english_lines[1:]:
    if not line.strip() or line.strip().startswith('#'):
        continue
    m = key_pattern.match(line)
    if m:
        indent = m.group(1)
        key = m.group(2)
        version = m.group(3)
        val = m.group(4)
        english_keys.append((indent, key, version, val))

print(f"Total English keys: {len(english_keys)}")
