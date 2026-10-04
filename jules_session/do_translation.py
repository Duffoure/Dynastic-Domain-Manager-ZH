import re

# Read english file
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# Match entries
pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$')

# We'll load our dictionary of translations
from translations_data import tr_map

out_lines = ["l_simp_chinese:\n"]

missing_keys = []
for line in lines[1:]:
    if not line.strip():
        out_lines.append(line)
        continue
    if line.strip().startswith('#'):
        out_lines.append(line)
        continue
    m = pattern.match(line)
    if m:
        indent = m.group(1)
        key = m.group(2)
        version = m.group(3)
        eng_val = m.group(4)
        
        if key in tr_map:
            zh_val = tr_map[key]
            out_lines.append(f'{indent}{key}:{version} "{zh_val}"\n')
        else:
            missing_keys.append(key)
            out_lines.append(f'{indent}{key}:{version} "{eng_val}"\n')
    else:
        out_lines.append(line)

print(f"Total lines written: {len(out_lines)}")
print(f"Missing keys count: {len(missing_keys)}")
if missing_keys:
    print(f"First 10 missing: {missing_keys[:10]}")

