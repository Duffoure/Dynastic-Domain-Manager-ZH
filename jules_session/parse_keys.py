import re

with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

keys = []
pattern = re.compile(r'^\s*([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$')
for line in lines:
    m = pattern.match(line)
    if m:
        keys.append((m.group(1), m.group(2), m.group(3)))

print(f"Total keys found: {len(keys)}")
