import re
import sys

# Read english/ddm_l_english.yml
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# Ensure we have the structure
print(f"Header: {lines[0].strip()}")
print(f"Total lines: {len(lines)}")
