import re
import json

with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# We will build a helper script that translates every line based on key-lookup or dictionary mappings
print(f"Total lines in source: {len(lines)}")
