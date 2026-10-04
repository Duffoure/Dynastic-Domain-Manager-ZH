import re

with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    content = f.read()

lines = content.splitlines()
print(f"Header: {lines[0]}")

entries = []
pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$')

matched = 0
unmatched = 0
for i, line in enumerate(lines[1:], start=2):
    if not line.strip() or line.strip().startswith('#'):
        continue
    m = pattern.match(line)
    if m:
        matched += 1
    else:
        unmatched += 1
        print(f"Line {i} unmatched: {line}")

print(f"Matched: {matched}, Unmatched: {unmatched}")
