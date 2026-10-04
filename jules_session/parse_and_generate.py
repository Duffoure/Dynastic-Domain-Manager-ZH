import re

with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

print(f"Read {len(lines)} lines")
