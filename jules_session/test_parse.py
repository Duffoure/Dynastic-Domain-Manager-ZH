import re

with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+)(:\d*)\s*"(.*)"\s*$')

matched = 0
for i, line in enumerate(lines[1:], start=2):
    if not line.strip() or line.strip().startswith('#'):
        continue
    m = pattern.match(line)
    if m:
        matched += 1
    else:
        print(f"Line {i} failed: {line}")

print(f"Total matched: {matched}")
