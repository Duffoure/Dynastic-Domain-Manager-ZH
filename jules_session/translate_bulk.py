import re
import json

# Read english file lines
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

pattern = re.compile(r'^(\s*)([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$')

# We can construct automatic translated strings or precise dictionary mapping for all keys
# Let's write a translator python dictionary generator that maps english string patterns to chinese!

