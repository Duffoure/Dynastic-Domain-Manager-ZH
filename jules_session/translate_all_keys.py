import re

# Read English file
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# Let's inspect all keys and make sure every key has an accurate Simplified Chinese translation.
# We will build a complete translation dictionary in python.

pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+)(:\d*)\s*"(.*)"\s*$')

entries = []
for i, line in enumerate(lines):
    if i == 0:
        continue
    m = pattern.match(line)
    if m:
        indent, key, ver, val = m.group(1), m.group(2), m.group(3), m.group(4)
        entries.append((indent, key, ver, val))

print(f"Total entries to translate: {len(entries)}")
