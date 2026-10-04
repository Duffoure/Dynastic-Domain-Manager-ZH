import re

# Read english file
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# Regex to parse key and value
pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$')

# We can define a translation dictionary for exact keys, and fallback to context-aware translation logic
# Let's verify all entries get accurate Chinese translation!

